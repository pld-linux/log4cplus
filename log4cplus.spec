Summary:	Logging Framework for C++
Name:		log4cplus
Version:	1.1.0
Release:	1
License:	ASL 2.0
URL:		http://sourceforge.net/projects/log4cplus
Source0:	http://downloads.sourceforge.net/log4cplus/%{name}-%{version}.tar.xz
# Source0-md5:	8f04a7b2db55384440b0ab83b6362d5d
Group:		Libraries
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
log4cplus is a simple to use C++ logging API providing thread-safe,
flexible, and arbitrarily granular control over log management and
configuration. It is modeled after the Java log4j API.

%package devel
Summary:	Development files for log4cplus C++ logging framework
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains headers and libraries needed to develop
applications using log4cplus logging framework.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_libdir}/liblog4cplus.{a,la}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README ChangeLog
%attr(755,root,root) %{_libdir}/liblog4cplus-*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblog4cplus-*.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblog4cplus.so
%{_includedir}/log4cplus
%{_pkgconfigdir}/log4cplus.pc
