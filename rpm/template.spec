Name:           ros-hydro-hector-quadrotor-gazebo
Version:        0.3.4
Release:        0%{?dist}
Summary:        ROS hector_quadrotor_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_quadrotor_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-gazebo-plugins
Requires:       ros-hydro-hector-gazebo-plugins
Requires:       ros-hydro-hector-quadrotor-controller-gazebo
Requires:       ros-hydro-hector-quadrotor-description
Requires:       ros-hydro-hector-quadrotor-gazebo-plugins
Requires:       ros-hydro-hector-quadrotor-model
Requires:       ros-hydro-hector-quadrotor-pose-estimation
Requires:       ros-hydro-hector-quadrotor-teleop
Requires:       ros-hydro-hector-sensors-gazebo
Requires:       ros-hydro-hector-uav-msgs
Requires:       ros-hydro-message-to-tf
Requires:       ros-hydro-robot-state-publisher
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-gazebo-plugins
BuildRequires:  ros-hydro-hector-gazebo-plugins
BuildRequires:  ros-hydro-hector-quadrotor-controller-gazebo
BuildRequires:  ros-hydro-hector-quadrotor-gazebo-plugins
BuildRequires:  ros-hydro-hector-sensors-gazebo
BuildRequires:  ros-hydro-message-to-tf
BuildRequires:  ros-hydro-robot-state-publisher

%description
hector_quadrotor_gazebo provides a quadrotor model for the gazebo simulator. It
can be commanded using geometry_msgs/Twist messages.

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
* Sun Feb 22 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.4-0
- Autogenerated by Bloom

* Mon Sep 01 2014 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.3-0
- Autogenerated by Bloom

