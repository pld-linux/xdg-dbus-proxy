Summary:	Filtering proxy for D-Bus connections
Name:		xdg-dbus-proxy
Version:	0.1.1
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	https://github.com/flatpak/xdg-dbus-proxy/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	e889380bb8c07dce97b118cda11d09d5
URL:		https://github.com/flatpak/xdg-dbus-proxy/
BuildRequires:	glib2-devel >= 2.40.0
BuildRequires:	libxslt-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdg-dbus-proxy is a filtering proxy for D-Bus connections. It was
originally part of the flatpak project, but it has been broken out as
a standalone module to facilitate using it in other contexts.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/xdg-dbus-proxy
%{_mandir}/man1/xdg-dbus-proxy.1*
