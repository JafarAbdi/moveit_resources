from moveit_helpers.get_parameters_module import load_file, load_yaml

def get_parameters(load_robot_description=False, robot_description='robot_description'):
    """
    robot_description: The name of the parameter under which the URDF is loaded
    """
    parameters = {}
    # Load universal robot description format (URDF)
    if load_robot_description:
        parameters[robot_description] = load_file('moveit_resources', 'panda_description/urdf/panda.urdf')
    # The semantic description that corresponds to the URDF
    parameters[robot_description + '_semantic'] = load_file('moveit_resources', 'panda_moveit_config/config/panda.srdf')
    # Load updated joint limits (override information from URDF)
    parameters[robot_description + '_planning'] = load_yaml('moveit_resources', 'panda_moveit_config/config/joint_limits.yaml')
    # Load default settings for kinematics; these settings are overridden by settings in a node's namespace
    # parameters[robot_description + '_kinematics'] = load_yaml('moveit_resources', 'panda_moveit_config/config/kinematics.yaml')
    parameters.update(load_yaml('moveit_resources', 'panda_moveit_config/config/kinematics.yaml'))
    return parameters
