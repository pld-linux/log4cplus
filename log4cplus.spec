#
# Conditional build:
%bcond_without	python		# Python/SWIG bindings (any)
%bcond_without	python2		# CPython 2.x bindings
%bcond_without	python3		# CPython 3.x bindings
%bcond_without	qt4		# liblog4cplusqt4debugappender library
%bcond_without	qt5		# liblog4cplusqt5debugappender library
%bcond_without	static_libs	# static libraries

%if %{without python}
%undefine	with_python2
%undefine	with_python3
%endif
Summary:	Logging Framework for C++
Summary(pl.UTF-8):	Szkielet logowania dla C++
Name:		log4cplus
Version:	2.1.1
Release:	2
License:	BSD or Apache v2.0
Group:		Libraries
Source0:	https://downloads.sourceforge.net/log4cplus/%{name}-%{version}.tar.xz
# Source0-md5:	6ee2555be39cd269086cc871c834e43f
Patch0:		%{name}-amfix.patch
Patch1:		%{name}-swig.patch
Patch2:		%{name}-link.patch
URL:		https://sourceforge.net/projects/log4cplus/
%{?with_qt4:BuildRequires:	QtCore-devel >= 4.0.0}
%{?with_qt5:BuildRequires:	Qt5Core-devel >= 5.0.0}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.14
BuildRequires:	libatomic-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2.4.2
BuildRequires:	pkgconfig
%{?with_python2:BuildRequires:	python-devel >= 1:2.3}
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
BuildRequires:	rpmbuild(macros) >= 1.219
%{?with_python:BuildRequires:	swig-python >= 2.0.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration. It is modeled after the Java log4j API.

%description -l pl.UTF-8
log4cplus to proste w użyciu API C++ do logowania, pozwalające na
elastyczne, bezpieczne wątkowo zarządzanie i konfigurowanie logowania
z dowolną kontrolą szczegółowości. Powstało w oparciu o API Javy
log4j.

%package devel
Summary:	Development files for log4cplus C++ logging framework
Summary(pl.UTF-8):	Pliki programistyczne szkieletu C++ do logowania log4cplus
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libatomic-devel
Requires:	libstdc++-devel >= 6:4.7

%description devel
This package contains the header files needed to develop applications
using log4cplus logging framework.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia aplikacji
wykorzystujących szkielet logowania log4cplus.

%package static
Summary:	Static log4cplus library
Summary(pl.UTF-8):	Statyczna biblioteka log4cplus
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static log4cplus library.

%description static -l pl.UTF-8
Statyczna biblioteka log4cplus.

%package qt4
Summary:	Qt4 interface to log4cplus
Summary(pl.UTF-8):	Interfejs Qt4 do log4cplus
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description qt4
Qt4 interface to log4cplus.

%description qt4 -l pl.UTF-8
Interfejs Qt4 do log4cplus.

%package qt4-devel
Summary:	Header file for log4cplusqt4debugappender library
Summary(pl.UTF-8):	Plik nagłówkowy do biblioteki log4cplusqt4debugappender
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt4 = %{version}-%{release}
Requires:	QtCore-devel >= 4.0.0

%description qt4-devel
Header file for log4cplusqt4debugappender library.

%description qt4-devel -l pl.UTF-8
Plik nagłówkowy do biblioteki log4cplusqt4debugappender.

%package qt4-static
Summary:	Static log4cplusqt4debugappender library
Summary(pl.UTF-8):	Biblioteka statyczna log4cplusqt4debugappender
Group:		Development/Libraries
Requires:	%{name}-qt4-devel = %{version}-%{release}

%description qt4-static
Static log4cplusqt4debugappender library.

%description qt4-static -l pl.UTF-8
Biblioteka statyczna log4cplusqt4debugappender.

%package qt5
Summary:	Qt5 interface to log4cplus
Summary(pl.UTF-8):	Interfejs Qt5 do log4cplus
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description qt5
Qt5 interface to log4cplus.

%description qt5 -l pl.UTF-8
Interfejs Qt5 do log4cplus.

%package qt5-devel
Summary:	Header file for log4cplusqt5debugappender library
Summary(pl.UTF-8):	Plik nagłówkowy do biblioteki log4cplusqt5debugappender
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-qt5 = %{version}-%{release}
Requires:	Qt5Core-devel >= 5.0.0

%description qt5-devel
Header file for log4cplusqt5debugappender library.

%description qt5-devel -l pl.UTF-8
Plik nagłówkowy do biblioteki log4cplusqt5debugappender.

%package qt5-static
Summary:	Static log4cplusqt5debugappender library
Summary(pl.UTF-8):	Biblioteka statyczna log4cplusqt5debugappender
Group:		Development/Libraries
Requires:	%{name}-qt5-devel = %{version}-%{release}

%description qt5-static
Static log4cplusqt5debugappender library.

%description qt5-static -l pl.UTF-8
Biblioteka statyczna log4cplusqt5debugappender.

%package -n python-log4cplus
Summary:	Python/SWIG bindings for log4cplus library
Summary(pl.UTF-8):	Wiązania Pythona/SWIG do biblioteki log4cplus
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-log4cplus
Python/SWIG bindings for log4cplus library.

%description -n python-log4cplus -l pl.UTF-8
Wiązania Pythona/SWIG do biblioteki log4cplus.

%package -n python3-log4cplus
Summary:	Python/SWIG bindings for log4cplus library
Summary(pl.UTF-8):	Wiązania Pythona/SWIG do biblioteki log4cplus
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-log4cplus
Python/SWIG bindings for log4cplus library.

%description -n python3-log4cplus -l pl.UTF-8
Wiązania Pythona/SWIG do biblioteki log4cplus.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%if %{with python2}
install -d build-python2
cd build-python2
../%configure \
	PYTHON=%{__python} \
	--with-python
%{__make}
cd ..
%endif

install -d build
cd build
# note: qt5 requires PIC code (see /usr/include/qt5/QtCore/qglobal.h)
../%configure \
	PYTHON=%{__python3} \
	%{?with_static_libs:--enable-static --with-pic} \
	%{?with_python3:--with-python} \
	%{?with_qt4:--with-qt} \
	%{?with_qt5:--with-qt5}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build-python2 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# non-Linux
%{__rm} $RPM_BUILD_ROOT%{_includedir}/log4cplus/nteventlogappender.h \
	$RPM_BUILD_ROOT%{_includedir}/log4cplus/win32*.h \
	$RPM_BUILD_ROOT%{_includedir}/log4cplus/config/{macosx,win32,windowsh-inc}.h \
	$RPM_BUILD_ROOT%{_includedir}/log4cplus/internal/cygwin-win32.h

%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblog4cplus*.la

%if %{with python2}
%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/log4cplus/_log4cplus*.la
%endif

%if %{with python3}
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/log4cplus/_log4cplus*.la
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	qt4 -p /sbin/ldconfig
%postun	qt4 -p /sbin/ldconfig

%post	qt5 -p /sbin/ldconfig
%postun	qt5 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE NEWS README.md TODO
%attr(755,root,root) %{_libdir}/liblog4cplus-2.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblog4cplus-2.1.so.9
%attr(755,root,root) %{_libdir}/liblog4cplusU-2.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblog4cplusU-2.1.so.9

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblog4cplus.so
%attr(755,root,root) %{_libdir}/liblog4cplusU.so
%dir %{_includedir}/log4cplus
%{_includedir}/log4cplus/appender.h
%{_includedir}/log4cplus/asyncappender.h
%{_includedir}/log4cplus/callbackappender.h
%{_includedir}/log4cplus/clfsappender.h
%{_includedir}/log4cplus/clogger.h
%{_includedir}/log4cplus/config.hxx
%{_includedir}/log4cplus/configurator.h
%{_includedir}/log4cplus/consoleappender.h
%{_includedir}/log4cplus/exception.h
%{_includedir}/log4cplus/fileappender.h
%{_includedir}/log4cplus/fstreams.h
%{_includedir}/log4cplus/hierarchy*.h
%{_includedir}/log4cplus/initializer.h
%{_includedir}/log4cplus/log4cplus.h
%{_includedir}/log4cplus/layout.h
%{_includedir}/log4cplus/log4judpappender.h
%{_includedir}/log4cplus/logger.h
%{_includedir}/log4cplus/loggingmacros.h
%{_includedir}/log4cplus/loglevel.h
%{_includedir}/log4cplus/mdc.h
%{_includedir}/log4cplus/msttsappender.h
%{_includedir}/log4cplus/ndc.h
%{_includedir}/log4cplus/nullappender.h
%{_includedir}/log4cplus/socketappender.h
%{_includedir}/log4cplus/streams.h
%{_includedir}/log4cplus/syslogappender.h
%{_includedir}/log4cplus/tchar.h
%{_includedir}/log4cplus/tracelogger.h
%{_includedir}/log4cplus/tstring.h
%{_includedir}/log4cplus/version.h
%{_includedir}/log4cplus/boost
%{_includedir}/log4cplus/config
%{_includedir}/log4cplus/helpers
%{_includedir}/log4cplus/internal
%{_includedir}/log4cplus/spi
%{_includedir}/log4cplus/thread
%{_pkgconfigdir}/log4cplus.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/liblog4cplus.a
%{_libdir}/liblog4cplusU.a
%endif

%if %{with qt4}
%files qt4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblog4cplusqt4debugappender-2.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblog4cplusqt4debugappender-2.1.so.9
%attr(755,root,root) %{_libdir}/liblog4cplusqt4debugappenderU-2.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblog4cplusqt4debugappenderU-2.1.so.9

%files qt4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblog4cplusqt4debugappender.so
%attr(755,root,root) %{_libdir}/liblog4cplusqt4debugappenderU.so
%{_includedir}/log4cplus/qt4debugappender.h

%if %{with static_libs}
%files qt4-static
%defattr(644,root,root,755)
%{_libdir}/liblog4cplusqt4debugappender.a
%{_libdir}/liblog4cplusqt4debugappenderU.a
%endif
%endif

%if %{with qt5}
%files qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblog4cplusqt5debugappender-2.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblog4cplusqt5debugappender-2.1.so.9
%attr(755,root,root) %{_libdir}/liblog4cplusqt5debugappenderU-2.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblog4cplusqt5debugappenderU-2.1.so.9

%files qt5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblog4cplusqt5debugappender.so
%attr(755,root,root) %{_libdir}/liblog4cplusqt5debugappenderU.so
%{_includedir}/log4cplus/qt5debugappender.h

%if %{with static_libs}
%files qt5-static
%defattr(644,root,root,755)
%{_libdir}/liblog4cplusqt5debugappender.a
%{_libdir}/liblog4cplusqt5debugappenderU.a
%endif
%endif

%if %{with python2}
%files -n python-log4cplus
%defattr(644,root,root,755)
%dir %{py_sitedir}/log4cplus
%attr(755,root,root) %{py_sitedir}/log4cplus/_log4cplus.so
%attr(755,root,root) %{py_sitedir}/log4cplus/_log4cplusU.so
%{py_sitescriptdir}/log4cplus
%endif

%if %{with python3}
%files -n python3-log4cplus
%defattr(644,root,root,755)
%dir %{py3_sitedir}/log4cplus
%attr(755,root,root) %{py3_sitedir}/log4cplus/_log4cplus.so
%attr(755,root,root) %{py3_sitedir}/log4cplus/_log4cplusU.so
%{py3_sitescriptdir}/log4cplus
%endif
