#!/usr/bin/env python3

import argparse
import os
import io

from babel.messages import pofile

PO_EXT = ".po"


def load_catalogs(top_dir):
    catalogs = {}
    for root, dirs, files in os.walk(top_dir, topdown=False):
        for file in files:
            if file.endswith(PO_EXT):
                path = os.path.join(root, file)
                rel_path = os.path.relpath(path, top_dir)
                with io.open(path, 'rb') as f:
                    catalogs[rel_path] = pofile.read_po(f)
            else:
                continue
    return catalogs


def main(args):
    # Load po files
    catalogs = load_catalogs(args.directory)

    # Format catalogs
    for rel_path in catalogs:
        catalog = catalogs[rel_path]
        path = os.path.join(args.directory, rel_path)
        catalog.fuzzy = True
        # Write po file
        with io.open(path, 'wb') as f:
            pofile.write_po(f, catalog, width=79)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Format po files')
    parser.add_argument('directory', nargs='?', default='./target',
                        help="A directory to format po files (default is './target')")
    args = parser.parse_args()
    main(args)
