from unlimiter.data.api import BenchlingV2APIConnection
import timeit

def get_all_projects():
  with BenchlingV2APIConnection() as benchling:
    projects = benchling.projects.list_projects()
    project_list = []
    for project in projects['projects']:
     project_list.append(project['name'])
    return project_list