from api.lib.services import benchling_service

class LoupeController:
  def __init__(self):
    pass


  @classmethod
  def get_all_projects(self):
    result = benchling_service.get_all_projects()
    return result
  