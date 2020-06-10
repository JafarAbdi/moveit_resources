from moveit_helpers.get_parameters_module import load_yaml

def get_parameters(moveit_controller_manager='moveit_simple_controller_manager/MoveItSimpleControllerManager'):
    parameters = {}
    # Set the param that trajectory_execution_manager needs to find the controller plugin
    parameters['moveit_controller_manager'] = moveit_controller_manager
    # load controller_list
    parameters['moveit_simple_controller_manager'] = load_yaml('run_moveit_cpp', 'config/controllers.yaml')
    return parameters
