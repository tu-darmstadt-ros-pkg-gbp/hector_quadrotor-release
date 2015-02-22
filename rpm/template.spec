Name:           ros-indigo-hector-quadrotor-controller-gazebo
Version:        0.3.4
Release:        0%{?dist}
Summary:        ROS hector_quadrotor_controller_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_quadrotor_controller_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-gazebo-ros-control >= 2.3.4
Requires:       ros-indigo-hector-quadrotor-controller
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-gazebo-ros-control >= 2.3.4
BuildRequires:  ros-indigo-hector-quadrotor-controller

%description
The hector_quadrotor_controller_gazebo package implements the ros_control
RobotHWSim interface for the quadrotor controller in package
hector_quadrotor_controller.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Feb 22 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.4-0
- Autogenerated by Bloom

* Mon Sep 01 2014 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.3-0
- Autogenerated by Bloom

