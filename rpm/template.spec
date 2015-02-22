Name:           ros-hydro-hector-quadrotor-teleop
Version:        0.3.4
Release:        0%{?dist}
Summary:        ROS hector_quadrotor_teleop package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_quadrotor_teleop
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-joy
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sensor-msgs

%description
hector_quadrotor_teleop enables quadrotor flying with a joystick by processing
joy/Joy messages and translating them to geometry_msgs/Twist.

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

