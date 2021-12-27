# Rosbag update
Updates topic data types on ROS bags, solves checksum errors.
Doesn't need any migration file.


# Requirements
Requires the new ros message to be imported and following the structure of `{package}/msg/{messagename}.msg` for example you should be able to import message in python with `from mypackage.msg import MyMessage`

# Installation
```
pip install rosbag-update
```
# Run
```
rosbag_update -b [bag-path]
```

