#
# Conditional build:
%bcond_without	qt4	# Qt 4.x version
%bcond_without	qt5	# Qt 5.x version

%define		qt4_ver	4.7.4
%define		qt5_ver	5.1.0

Summary:	Polkit-qt-1 - Qt 4 API wrapper library around polkit
Summary(pl.UTF-8):	Polkit-qt-1 - obudowanie bibliotek polkit w API Qt 4
Name:		polkit-qt-1
Version:	0.112.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/apps/KDE4.x/admin/%{name}-%{version}.tar.bz2
# Source0-md5:	bee71b71c12797e6fc498540a06c829b
URL:		https://techbase.kde.org/Projects/KAuth/Polkit-Qt-1
BuildRequires:	cmake >= 2.8.11
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel >= 0.96
BuildRequires:	rpmbuild(macros) >= 1.605
%if %{with qt4}
BuildRequires:	QtCore-devel >= %{qt4_ver}
BuildRequires:	QtDBus-devel >= %{qt4_ver}
BuildRequires:	QtGui-devel >= %{qt4_ver}
BuildRequires:	QtTest-devel >= %{qt4_ver}
BuildRequires:	QtXml-devel >= %{qt4_ver}
BuildRequires:	qt4-build >= %{qt4_ver}
BuildRequires:	qt4-qmake >= %{qt4_ver}
%endif
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= %{qt5_ver}
BuildRequires:	Qt5DBus-devel >= %{qt5_ver}
BuildRequires:	Qt5Gui-devel >= %{qt5_ver}
BuildRequires:	Qt5Test-devel >= %{qt5_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt5_ver}
BuildRequires:	Qt5Xml-devel >= %{qt5_ver}
BuildRequires:	qt5-build >= %{qt5_ver}
BuildRequires:	qt5-qmake >= %{qt5_ver}
%endif
Requires:	QtCore >= %{qt4_ver}
Requires:	QtDBus >= %{qt4_ver}
Provides:	polkit-qt = %{version}-%{release}
Obsoletes:	polkit-qt < 0.103.0-1
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
Requires:	QtCore-devel >= %{qt4_ver}
Requires:	QtDBus-devel >= %{qt4_ver}
Provides:	polkit-qt-devel = %{version}-%{release}
Obsoletes:	polkit-qt-devel < 0.103.0-1

%description devel
Development files for Polkit-qt-1 core library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki Polkit-qt-1.

%package agent
Summary:	Qt 4 API wrapper arount polkit-agent library
Summary(pl.UTF-8):	Obudowanie biblioteki polkit-agent w API Qt 4
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description agent
Qt 4 API wrapper arount polkit-agent library.

%description agent -l pl.UTF-8
Obudowanie biblioteki polkit-agent w API Qt 4.

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
Summary:	Qt 4 API wrapper arount polkit library - GUI functions
Summary(pl.UTF-8):	Obudowanie biblioteki polkit w API Qt 4 - funkcje GUI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtGui >= %{qt4_ver}
Provides:	polkit-qt-gui = %{version}-%{release}
Obsoletes:	polkit-qt-gui < 0.103.0-1

%description gui
Qt 4 API wrapper arount polkit library - GUI functions.

%description gui -l pl.UTF-8
Obudowanie biblioteki polkit w API Qt 4 - funkcje GUI.

%package gui-devel
Summary:	Development files for Polkit-qt-1 GUI library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Polkit-qt-1 GUI
Group:		Development/Libraries
Requires:	%{name}-gui = %{version}-%{release}
# polkit-qt-agent-1 is required by polkit-qt-1.pc
Requires:	%{name}-agent-devel = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	QtGui >= %{qt4_ver}
Provides:	polkit-qt-gui-devel = %{version}-%{release}
Obsoletes:	polkit-qt-gui-devel < 0.103.0-1

%description gui-devel
Development files for Polkit-qt-1 GUI library.

%description gui-devel -l pl.UTF-8
Pliki programistyczne biblioteki Polkit-qt-1 GUI.

%package -n polkit-qt5-1
Summary:	Polkit-qt-1 - Qt 5 API wrapper library around polkit
Summary(pl.UTF-8):	Polkit-qt-1 - obudowanie bibliotek polkit w API Qt 5
Group:		Libraries
Requires:	Qt5Core >= %{qt5_ver}
Requires:	Qt5DBus >= %{qt5_ver}

%description -n polkit-qt5-1
Polkit-qt5-1 is a wrapper library around polkit libraries, which lets
developers write easily applications using polkit-1, and even write
custom authentication agents.

%description -n polkit-qt5-1 -l pl.UTF-8
Polkit-qt5-1 to biblioteka obudowująca biblioteki polkit, pozwalająca
programistom w łatwy sposób tworzyć aplikacje korzystające z bibliotek
polkit-1, a nawet pisać własnych agentów uwierzytelniających.

%package -n polkit-qt5-1-devel
Summary:	Development files for Polkit-qt5-1 core library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Polkit-qt5-1
Group:		Development/Libraries
Requires:	polkit-qt5-1 = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qt5_ver}
Requires:	Qt5DBus-devel >= %{qt5_ver}

%description -n polkit-qt5-1-devel
Development files for Polkit-qt5-1 core library.

%description -n polkit-qt5-1-devel -l pl.UTF-8
Pliki programistyczne biblioteki Polkit-qt5-1.

%package -n polkit-qt5-1-agent
Summary:	Qt 5 API wrapper arount polkit-agent library
Summary(pl.UTF-8):	Obudowanie biblioteki polkit-agent w API Qt 5
Group:		Libraries
Requires:	polkit-qt5-1 = %{version}-%{release}
Requires:	Qt5Gui >= %{qt5_ver}

%description -n polkit-qt5-1-agent
Qt 5 API wrapper arount polkit-agent library.

%description -n polkit-qt5-1-agent -l pl.UTF-8
Obudowanie biblioteki polkit-agent w API Qt 5.

%package -n polkit-qt5-1-agent-devel
Summary:	Development files for Polkit-qt5-1 Agent library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Polkit-qt5-1 Agent
Group:		Development/Libraries
Requires:	polkit-qt5-1-agent = %{version}-%{release}
Requires:	polkit-qt5-1-devel = %{version}-%{release}
Requires:	Qt5Gui-devel >= %{qt5_ver}

%description -n polkit-qt5-1-agent-devel
Development files for Polkit-qt5-1 Agent library.

%description -n polkit-qt5-1-agent-devel -l pl.UTF-8
Pliki programistyczne biblioteki Polkit-qt5-1 Agent.

%package -n polkit-qt5-1-gui
Summary:	Qt 5 API wrapper arount polkit library - GUI functions
Summary(pl.UTF-8):	Obudowanie biblioteki polkit w API Qt 5 - funkcje GUI
Group:		Libraries
Requires:	polkit-qt5-1 = %{version}-%{release}
Requires:	Qt5Gui >= %{qt5_ver}

%description -n polkit-qt5-1-gui
Qt 5 API wrapper arount polkit library - GUI functions.

%description -n polkit-qt5-1-gui -l pl.UTF-8
Obudowanie biblioteki polkit w API Qt 5 - funkcje GUI.

%package -n polkit-qt5-1-gui-devel
Summary:	Development files for Polkit-qt5-1 GUI library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Polkit-qt5-1 GUI
Group:		Development/Libraries
Requires:	polkit-qt5-1-gui = %{version}-%{release}
# polkit-qt5-agent-1 is required by polkit-qt5-1.pc
Requires:	polkit-qt5-1-agent-devel = %{version}-%{release}
Requires:	polkit-qt5-1-devel = %{version}-%{release}
Requires:	Qt5Gui-devel >= %{qt5_ver}

%description -n polkit-qt5-1-gui-devel
Development files for Polkit-qt5-1 GUI library.

%description -n polkit-qt5-1-gui-devel -l pl.UTF-8
Pliki programistyczne biblioteki Polkit-qt5-1 GUI.

%prep
%setup -q

%build
%if %{with qt4}
install -d build-qt4
cd build-qt4
%cmake .. \
	-DQT_QMAKE_EXECUTABLE=%{_bindir}/qmake-qt4 \
	-DUSE_QT4=ON

%{__make}
cd ..
%endif

%if %{with qt5}
install -d build-qt5
cd build-qt5
%cmake .. \
	-DQT_QMAKE_EXECUTABLE=%{_bindir}/qmake-qt4 \
	-DUSE_QT5=ON

%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with qt4}
%{__make} -C build-qt4 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with qt5}
%{__make} -C build-qt5 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	agent -p /sbin/ldconfig
%postun	agent -p /sbin/ldconfig

%post	gui -p /sbin/ldconfig
%postun	gui -p /sbin/ldconfig

%post	-n polkit-qt5-1 -p /sbin/ldconfig
%postun	-n polkit-qt5-1 -p /sbin/ldconfig

%post	-n polkit-qt5-1-agent -p /sbin/ldconfig
%postun	-n polkit-qt5-1-agent -p /sbin/ldconfig

%post	-n polkit-qt5-1-gui -p /sbin/ldconfig
%postun	-n polkit-qt5-1-gui -p /sbin/ldconfig

%if %{with qt4}
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
%endif

%if %{with qt5}
%files -n polkit-qt5-1
%defattr(644,root,root,755)
%doc AUTHORS README README.porting TODO
%attr(755,root,root) %{_libdir}/libpolkit-qt5-core-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt5-core-1.so.1

%files -n polkit-qt5-1-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt5-core-1.so
%dir %{_includedir}/polkit-qt5-1
%dir %{_includedir}/polkit-qt5-1/PolkitQt1
%{_includedir}/polkit-qt5-1/PolkitQt1/ActionDescription
%{_includedir}/polkit-qt5-1/PolkitQt1/Authority
%{_includedir}/polkit-qt5-1/PolkitQt1/Details
%{_includedir}/polkit-qt5-1/PolkitQt1/Identity
%{_includedir}/polkit-qt5-1/PolkitQt1/Subject
%{_includedir}/polkit-qt5-1/PolkitQt1/TemporaryAuthorization
%{_includedir}/polkit-qt5-1/polkitqt1-actiondescription.h
%{_includedir}/polkit-qt5-1/polkitqt1-authority.h
%{_includedir}/polkit-qt5-1/polkitqt1-details.h
%{_includedir}/polkit-qt5-1/polkitqt1-export.h
%{_includedir}/polkit-qt5-1/polkitqt1-identity.h
%{_includedir}/polkit-qt5-1/polkitqt1-subject.h
%{_includedir}/polkit-qt5-1/polkitqt1-temporaryauthorization.h
%{_includedir}/polkit-qt5-1/polkitqt1-version.h
%{_pkgconfigdir}/polkit-qt5-core-1.pc
%{_libdir}/cmake/PolkitQt5-1

%files -n polkit-qt5-1-agent
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt5-agent-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt5-agent-1.so.1

%files -n polkit-qt5-1-agent-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt5-agent-1.so
%{_includedir}/polkit-qt5-1/PolkitQt1/Agent
%{_includedir}/polkit-qt5-1/polkitqt1-agent-*.h
%{_pkgconfigdir}/polkit-qt5-agent-1.pc

%files -n polkit-qt5-1-gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt5-gui-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpolkit-qt5-gui-1.so.1

%files -n polkit-qt5-1-gui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpolkit-qt5-gui-1.so
%{_includedir}/polkit-qt5-1/PolkitQt1/Gui
%{_includedir}/polkit-qt5-1/polkitqt1-gui-*.h
%{_pkgconfigdir}/polkit-qt5-gui-1.pc
%{_pkgconfigdir}/polkit-qt5-1.pc
%endif
