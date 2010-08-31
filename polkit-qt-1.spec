%define		qtver	4.6.3

Summary:	Polkit-qt-1 wrapper library around polkit-gobject and polkit-agent
Name:		polkit-qt-1
Version:	0.96.1
Release:	4
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/apps/KDE4.x/admin//%{name}-%{version}.tar.bz2
# Source0-md5:	7d122aa67c6786ea7d0bb023701693a1
URL:		http://www.kde.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.96
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polkit-qt-1 is a wrapper library around polkit-gobject and
polkit-agent, which lets developers write easily applications using
polkit-1, and even write custom authentication agents.

%package agent
Summary:	Polkit-qt-1 Agent
License:	GPL v2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description agent
Polkit-qt-1 Agent.

%package devel
Summary:	Polkit-qt-1 development files
License:	GPL v2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-agent = %{version}-%{release}
Requires:	%{name}-gui = %{version}-%{release}
Requires:	polkit-devel

%description devel
Polkit-qt-1 header files.

%package gui
Summary:	Polkit-qt-1 GUI
License:	GPL v2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gui
Polkit-qt-1 GUI.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-LCMS_DIR=%{_libdir} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post   agent -p /sbin/ldconfig
%postun agent -p /sbin/ldconfig
%post   gui -p /sbin/ldconfig
%postun gui -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt-core-1.so.?
%attr(755,root,root) %{_libdir}/libpolkit-qt-core-1.so.*.*.*

%files agent
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt-agent-1.so.?
%attr(755,root,root) %{_libdir}/libpolkit-qt-agent-1.so.*.*.*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt-gui-1.so.?
%attr(755,root,root) %{_libdir}/libpolkit-qt-gui-1.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt-agent-1.so
%attr(755,root,root) %{_libdir}/libpolkit-qt-core-1.so
%attr(755,root,root) %{_libdir}/libpolkit-qt-gui-1.so
%{_includedir}/polkit-qt-1
%{_pkgconfigdir}/*.pc
