"""
Base Python code for a script
"""

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Description")
    parser.add_argument('--src', help='directory', default='./default')

    print('Done')
