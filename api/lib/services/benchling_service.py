from unlimiter.data.api import BenchlingV2APIConnection

import pprint

def get_all_projects():
  with BenchlingV2APIConnection() as benchling:
    projects = benchling.projects.list_projects()
    return projects

class BenchlingSerivce:
  def __init__(self):
    self.benchling = BenchlingV2APIConnection()

  def get_all_projects(self):
    projects = self.benchling.projects.list_projects()
    return projects