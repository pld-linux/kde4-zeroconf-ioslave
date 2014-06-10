#
%define		_state		stable
%define		orgname		zeroconf-ioslave
%define		qtver		4.8.0

Summary:	K Desktop Environment - Zeroconf IO Slave
Name:		kde4-zeroconf-ioslave
Version:	4.13.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	2a824507ca6408277a9ea039ab15adfd
URL:		http://www.kde.org/
Obsoletes:	kde4-kdenetwork-kdnssd
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zeroconf IO Slave.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kded_dnssdwatcher.so
%attr(755,root,root) %{_libdir}/kde4/kio_zeroconf.so
%{_datadir}/apps/remoteview/zeroconf.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kdnssd.xml
%{_datadir}/kde4/services/kded/dnssdwatcher.desktop
%{_datadir}/kde4/services/zeroconf.protocol

