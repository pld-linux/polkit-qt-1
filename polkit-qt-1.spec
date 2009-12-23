%define		qtver	4.6.0

Summary:	Polkit-qt-1 wrapper library around polkit-gobject and polkit-agent
Name:		polkit-qt-1
Version:	0.95.1
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	b5c5017058ab0f3bc7eb337a7c66e0bc
URL:		http://www.kde.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	polkit-devel >= 0.95
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polkit-qt-1 is a wrapper library around polkit-gobject and polkit-agent, which lets developers write easily applications using polkit-1, and even write custom authentication agents.

%package devel
Summary:	Polkit-qt-1 development files
License:	GPL v2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-gui = %{version}-%{release}

%description devel
Polkit-qt-1 header files.

%package gui
Summary:	Polkit-qt-1 use the PolicyKit API through Qt-styled API
License:	GPL v2
Group:		Libraries

%description gui
Polkit-qt-1 gui.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt-core.so.?
%attr(755,root,root) %{_libdir}/libpolkit-qt-core.so.*.*.*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt-gui.so.?
%attr(755,root,root) %{_libdir}/libpolkit-qt-gui.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt-core.so
%attr(755,root,root) %{_libdir}/libpolkit-qt-gui.so
%{_includedir}/PolicyKit/polkit-qt
%{_libdir}/pkgconfig/*.pc
