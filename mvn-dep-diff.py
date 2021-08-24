#!/usr/bin/env python3

import os
import sys
from typing import Optional

# dcd

def read_file(filename: str) -> list[str]:
    with open(filename) as f:
        contents = [x.rstrip() for x in f.readlines()]
    return contents

NodeKey = tuple[str, str]
class Node:
    def __init__(self, line) -> None:
        idx = 0
        while idx < len(line) and not line[idx].isalpha():
            idx += 1

        if idx == len(line):
            raise Exception('expected lib, found nothing, for {}'.format(line))

        self.prefix = line[0:idx]
        vstr = line[idx:]
        split = vstr.split(':')

        self.os = None
        # `${group}:${artifact}:${type}:${version}:${scope}`
        if len(split) == 5:
            (m_group, m_artifact, m_type, m_version, m_scope) = split
        elif len(split) == 6:
            # guessing m_os idk what this is
            (m_group, m_artifact, m_type, m_os, m_version, m_scope) = split
            self.os = m_os
        else:
            raise Exception("invalid split size {}, for {}".format(len(split), split))

        self.group = m_group
        self.artifact = m_artifact
        self.type = m_type
        self.version = m_version
        self.scope = m_scope

    def format(self) -> str:
        if self.os is not None:
            vstr = '{}:{}:{}:{}:{}:{}'.format(self.group, self.artifact, self.type, self.os, self.version, self.scope)
        else:
            vstr = '{}:{}:{}:{}:{}'.format(self.group, self.artifact, self.type, self.version, self.scope)
        return vstr
    
    def key(self) -> NodeKey:
        return (self.group, self.artifact)

def read_lib(line: str) -> Optional[Node]:
    if len(line) == 0:
        return None
    
    first_char = line[0]
    if first_char not in ['+', '\\', '|']:
        return None

    return Node(line)

def main(base_file: str, dep_addition_file: str):
    base = read_file(base_file)
    dep = read_file(dep_addition_file)

    new_versions: dict[NodeKey, Node] = {}

    # start reading dep_file
    for line in dep:
        lib = read_lib(line)
        if lib is not None:
            new_versions[lib.key()] = lib

    print('--- /base')
    print('+++ /dependency')

    # start reading base_file
    for line in base:
        lib = read_lib(line)
        if lib is None:
            print(' {}'.format(line))
        else:
            ver_delta = False
            if lib.key() in new_versions:
                dep_lib = new_versions[lib.key()]
                if lib.version != dep_lib.version:
                    ver_delta = True

                    # haha hack.
                    if dep_lib.scope == 'test':
                        if lib.scope == 'compile':
                            ver_delta = False
            
            if ver_delta:
                print('-{}'.format(line))
                print('+{}{}'.format(lib.prefix, dep_lib.format()))
            else:
                print(' {}'.format(line))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
