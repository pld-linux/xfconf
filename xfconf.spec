%define		xfce_version	4.16.0
Summary:	Simple configuration storage and query system
Summary(pl.UTF-8):	Prosty system przechowywania i odpytywania konfiguracji
Name:		xfconf
Version:	4.16.0
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	https://archive.xfce.org/src/xfce/xfconf/4.16/%{name}-%{version}.tar.bz2
# Source0-md5:	ac204fcc17fd4299d59e619aadbc6194
URL:		https://www.xfce.org/projects/xfconf
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.0
BuildRequires:	perl-Glib-devel >= 1.224-2
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	vala
BuildRequires:	xfce4-dev-tools >= 4.16.0
Requires:	glib2 >= 1:2.50.0
Requires:	libxfce4util >= %{xfce_version}
Obsoletes:	libxfce4mcs
Obsoletes:	perl-Xfce4-Xfconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfconf is a simple configuration storage and query system.

%description -l pl.UTF-8
Xfconf jest prostym systemem przechowywania i odpytywania
konfiguracji.

%package devel
Summary:	Header files for Xfconf library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Xfconf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.50.0
Obsoletes:	libxfce4mcs-devel
Obsoletes:	xfce-mcs-manager-devel

%description devel
Header files for Xfconf library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Xfconf.

%package apidocs
Summary:	Xfconf API documentation
Summary(pl.UTF-8):	Dokumentacja API Xfconf
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	libxfce4mcs-apidocs
BuildArch:	noarch

%description apidocs
Xfconf API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Xfconf.

%package -n bash-completion-xfconf-query
Summary:	bash-completion for xfconf-query command
Summary(pl.UTF-8):	bashowe uzupełnianie parametrów polecenia xfconf-query
Group:		Applications/Shells
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bash-completion >= 2.0
BuildArch:	noarch

%description -n bash-completion-xfconf-query
Bash-completion for xfconf-query command.

%description -n bash-completion-xfconf-query -l pl.UTF-8
Bashowe uzupełnianie parametrów polecenia xfconf-query.

%package -n vala-xfconf
Summary:	Vala API for Xfconf library
Summary(pl.UTF-8):	API języka Vala do biblioteki Xfconf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala

%description -n vala-xfconf
Vala API for Xfconf library.

%description -n vala-xfconf -l pl.UTF-8
API języka Vala do biblioteki Xfconf.

%prep
%setup -q

%build
%configure \
	--enable-gtk-doc \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gio/modules/libxfconfgsettingsbackend.la
# unify
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}
# just a copy or ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/hye

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/xfconf-query
%attr(755,root,root) %{_libdir}/libxfconf-0.so.*.*.*
%attr(755,root,root) %{_libdir}/gio/modules/libxfconfgsettingsbackend.so
%attr(755,root,root) %ghost %{_libdir}/libxfconf-0.so.3
%dir %{_libdir}/xfce4/xfconf
%attr(755,root,root) %{_libdir}/xfce4/xfconf/xfconfd
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%{_datadir}/dbus-1/services/org.xfce.Xfconf.service
%{_libdir}/girepository-1.0/Xfconf-0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfconf-0.so
%{_includedir}/xfce4/xfconf-0
%{_pkgconfigdir}/libxfconf-0.pc
%{_datadir}/gir-1.0/Xfconf-0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/xfconf

%files -n bash-completion-xfconf-query
%defattr(644,root,root,755)
%{bash_compdir}/xfconf-query

%files -n vala-xfconf
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libxfconf-0.deps
%{_datadir}/vala/vapi/libxfconf-0.vapi
