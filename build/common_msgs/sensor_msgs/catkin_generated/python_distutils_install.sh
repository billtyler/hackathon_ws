#!/bin/sh -x

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

cd "/home/hackathon_ws/src/common_msgs/sensor_msgs"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
/usr/bin/env \
    PYTHONPATH="/home/hackathon_ws/install/lib/python2.7/dist-packages:/home/hackathon_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/hackathon_ws/build" \
    "/usr/bin/python" \
    "/home/hackathon_ws/src/common_msgs/sensor_msgs/setup.py" \
    build --build-base "/home/hackathon_ws/build/common_msgs/sensor_msgs" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/hackathon_ws/install" --install-scripts="/home/hackathon_ws/install/bin"
