#!/usr/bin/python3

#import sys
#import os.path
import argparse
import pymongo
#import requests
from .models import Index
from .database import DB_NAME



def main():
  x = CONN.Index.find_random()
  print(x[''])
  print("hello")


def checkArgs(args):
  fails = False
  if args.contains and args.exact:
    print("ERROR: Too many arguments. Can only use either --contains or --exact.")
    fails = True
  if args.id is None and args.name is None:
    print("ERROR: Missing argument. Must supply either --name or --id.")
    fails = True
  if args.id and args.name:
    print("ERROR: Too many arguments. Must supply either --name or --id.")
    fails = True
  if fails:
    exit(1)


def defineArgs():
  parser = argparse.ArgumentParser(description='Search for 990 forms in XML format from Amazon S3 bucket')
  parser.add_argument('--id', nargs='?', type=str, help='Searches for a foundation by EIN.')
  parser.add_argument('--name', nargs='?', type=str, help='Foundation name to search for. Case insensitive.')
  parser.add_argument('--contains', dest='contains', help='Substring search on the name field. ', action='store_true')
  parser.add_argument('--exact', dest='exact', help='Searches for exact name of foundation.', action='store_true')
  parser.add_argument('--index', dest='index', help='Returns only the index entries of the search results.', action='store_true')
  args = parser.parse_args()
  return args


def initArgs():
  args = defineArgs()
  checkArgs(args)
  return args


if __name__ == '__main__':
  args = initArgs()
  print(args)
  main()
