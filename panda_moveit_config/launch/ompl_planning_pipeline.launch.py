from moveit_helpers.get_parameters_module import load_yaml

def get_parameters():
    parameters = {'ompl': {}}
    # OMPL Plugin for MoveIt
    parameters['ompl'].update({'planning_plugin': 'ompl_interface/OMPLPlanner'})
    # The request adapters (plugins) used when planning with OMPL. ORDER MATTERS
    parameters['ompl'].update({'request_adapters': ("default_planner_request_adapters/AddTimeParameterization "
                                                    "default_planner_request_adapters/FixWorkspaceBounds "
                                                    "default_planner_request_adapters/FixStartStateBounds "
                                                    "default_planner_request_adapters/FixStartStateCollision "
                                                    "default_planner_request_adapters/FixStartStatePathConstraints")})
    parameters['ompl'].update({'start_state_max_bounds_error': 0.1})

    parameters['ompl'].update(load_yaml('moveit_resources', 'panda_moveit_config/config/ompl_planning.yaml'))
    return parameters
