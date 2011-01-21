%define		qtver	4.6.3

Summary:	Polkit-qt-1 - Qt API wrapper library around polkit
Summary(pl.UTF-8):	Polkit-qt-1 - obudowanie bibliotek polkit w API w stylu Qt
Name:		polkit-qt-1
Version:	0.99.0
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/apps/KDE4.x/admin/%{name}-%{version}.tar.bz2
# Source0-md5:	1c5b4113a2a167624b5f716b4f03a219
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
Requires:	QtCore >= %{qtver}
Requires:	QtDBus >= %{qtver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polkit-qt-1 is a wrapper library around polkit libraries, which lets
developers write easily applications using polkit-1, and even write
custom authentication agents.

%description -l pl.UTF-8
Polkit-qt-1 to biblioteka obudowująca biblioteki polkit, pozwalająca
programistom w łatwy sposób tworzyć aplikacje korzystające z bibliotek
polkit-1, a nawet pisać własnych agentów uwierzytelniających.

%package devel
Summary:	Development files for Polkit-qt-1 core library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Polkit-qt-1
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= %{qtver}
Requires:	QtDBus-devel >= %{qtver}

%description devel
Development files for Polkit-qt-1 core library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki Polkit-qt-1.

%package agent
Summary:	Qt API wrapper arount polkit-agent library
Summary(pl.UTF-8):	Obudowanie biblioteki polkit-agent w API w stylu Qt
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description agent
Qt API wrapper arount polkit-agent library.

%description agent -l pl.UTF-8
Obudowanie biblioteki polkit-agent w API w stylu Qt.

%package agent-devel
Summary:	Development files for Polkit-qt-1 Agent library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Polkit-qt-1 Agent
Group:		Development/Libraries
Requires:	%{name}-agent = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description agent-devel
Development files for Polkit-qt-1 Agent library.

%description agent-devel -l pl.UTF-8
Pliki programistyczne biblioteki Polkit-qt-1 Agent.

%package gui
Summary:	Qt API wrapper arount polkit library - GUI functions
Summary(pl.UTF-8):	Obudowanie biblioteki polkit w API w stylu Qt - funkcje GUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtGui >= %{qtver}

%description gui
Qt API wrapper arount polkit library - GUI functions.

%description gui -l pl.UTF-8
Obudowanie biblioteki polkit w API w stylu Qt - funkcje GUI.

%package gui-devel
Summary:	Development files for Polkit-qt-1 GUI library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Polkit-qt-1 GUI
Group:		Development/Libraries
Requires:	%{name}-gui = %{version}-%{release}
# polkit-qt-agent-1 is required by polkit-qt-1.pc
Requires:	%{name}-agent-devel = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	QtGui >= %{qtver}

%description gui-devel
Development files for Polkit-qt-1 GUI library.

%description gui-devel -l pl.UTF-8
Pliki programistyczne biblioteki Polkit-qt-1 GUI.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DLIB_INSTALL_DIR=%{_libdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	-DQT_QMAKE_EXECUTABLE=/usr/bin/qmake-qt4

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	agent -p /sbin/ldconfig
%postun	agent -p /sbin/ldconfig

%post	gui -p /sbin/ldconfig
%postun	gui -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README README.porting TODO
%attr(755,root,root) %{_libdir}/libpolkit-qt-core-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt-core-1.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt-core-1.so
%dir %{_includedir}/polkit-qt-1
%dir %{_includedir}/polkit-qt-1/PolkitQt1
%{_includedir}/polkit-qt-1/PolkitQt1/ActionDescription
%{_includedir}/polkit-qt-1/PolkitQt1/Authority
%{_includedir}/polkit-qt-1/PolkitQt1/Details
%{_includedir}/polkit-qt-1/PolkitQt1/Identity
%{_includedir}/polkit-qt-1/PolkitQt1/Subject
%{_includedir}/polkit-qt-1/PolkitQt1/TemporaryAuthorization
%{_includedir}/polkit-qt-1/polkitqt1-actiondescription.h
%{_includedir}/polkit-qt-1/polkitqt1-authority.h
%{_includedir}/polkit-qt-1/polkitqt1-details.h
%{_includedir}/polkit-qt-1/polkitqt1-export.h
%{_includedir}/polkit-qt-1/polkitqt1-identity.h
%{_includedir}/polkit-qt-1/polkitqt1-subject.h
%{_includedir}/polkit-qt-1/polkitqt1-temporaryauthorization.h
%{_includedir}/polkit-qt-1/polkitqt1-version.h
%{_pkgconfigdir}/polkit-qt-core-1.pc
%{_libdir}/cmake/PolkitQt-1

%files agent
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt-agent-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt-agent-1.so.1

%files agent-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt-agent-1.so
%{_includedir}/polkit-qt-1/PolkitQt1/Agent
%{_includedir}/polkit-qt-1/polkitqt1-agent-*.h
%{_pkgconfigdir}/polkit-qt-agent-1.pc

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt-gui-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt-gui-1.so.1

%files gui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt-gui-1.so
%{_includedir}/polkit-qt-1/PolkitQt1/Gui
%{_includedir}/polkit-qt-1/polkitqt1-gui-*.h
%{_pkgconfigdir}/polkit-qt-gui-1.pc
%{_pkgconfigdir}/polkit-qt-1.pc
