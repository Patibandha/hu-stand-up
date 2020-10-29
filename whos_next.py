#!/usr/bin/python3
import yaml


def get_all_members():
    with open('members.yml','r') as m:
        member_yaml = yaml.safe_load(m)

    members = []
    for member in member_yaml['standup_members']:
        members.append([str(member['name']), str(member['url'])])
    return members
