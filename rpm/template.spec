Name:           ros-hydro-hector-quadrotor-gazebo-plugins
Version:        0.3.5
Release:        0%{?dist}
Summary:        ROS hector_quadrotor_gazebo_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_quadrotor_gazebo_plugins
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-gazebo-ros
Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-hector-gazebo-plugins
Requires:       ros-hydro-hector-quadrotor-model
Requires:       ros-hydro-hector-uav-msgs
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-std-srvs
BuildRequires:  gazebo-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-hector-gazebo-plugins
BuildRequires:  ros-hydro-hector-quadrotor-model
BuildRequires:  ros-hydro-hector-uav-msgs
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-std-srvs

%description
hector_quadrotor_gazebo_plugins provides gazebo plugins for using quadrotors in
gazebo. The hector_gazebo_ros_baro sensor plugin simulates an altimeter based on
barometric pressure. hector_quadrotor_simple_controller is a simple controller
allowing to command the quadrotor's velocity using a geometry_msgs/Twist message
for teleoperation just by means of applying forces and torques to the model.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sat Mar 28 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.5-0
- Autogenerated by Bloom

* Sun Feb 22 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.4-0
- Autogenerated by Bloom

* Mon Sep 01 2014 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.3-0
- Autogenerated by Bloom

