Summary:	Filtering proxy for D-Bus connections
Summary(pl.UTF-8):	Proxy filtrujące dla połączeń D-Bus
Name:		xdg-dbus-proxy
Version:	0.1.4
Release:	1
License:	LGPL v2+
Group:		Applications/System
#Source0Download: https://github.com/flatpak/xdg-dbus-proxy/releases
Source0:	https://github.com/flatpak/xdg-dbus-proxy/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	89d166170e871b3288e8980aee599ae4
URL:		https://github.com/flatpak/xdg-dbus-proxy/
BuildRequires:	glib2-devel >= 1:2.40
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.40
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdg-dbus-proxy is a filtering proxy for D-Bus connections. It was
originally part of the flatpak project, but it has been broken out as
a standalone module to facilitate using it in other contexts.

%description -l pl.UTF-8
xdg-dbus-proxy to proxy filtrujące dla połączeń D-Bus. Pierwotnie było
częścią projektu flatpak, ale zostało wydzielone jako samodzielny
moduł, aby ułatwić używanie go w innych kontekstach.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/xdg-dbus-proxy
%{_mandir}/man1/xdg-dbus-proxy.1*
