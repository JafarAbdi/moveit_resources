# This file makes it easy to include different planning pipelines;
# It is assumed that all planning pipelines are named XXX_planning_pipeline.launch

from moveit_helpers.get_parameters_module import get_parameters_module


def get_parameters(pipeline='ompl'):
   return get_parameters_module('moveit_resources', '/panda_moveit_config/launch/' + pipeline + '_planning_pipeline.launch.py')()

