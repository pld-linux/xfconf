%define		xfce_version	4.12.0
%include	/usr/lib/rpm/macros.perl
Summary:	Simple configuration storage and query system
Summary(pl.UTF-8):	Prosty system przechowywania i odpytywania konfiguracji
Name:		xfconf
Version:	4.12.0
Release:	7
License:	LGPL v2
Group:		Libraries
Source0:	http://archive.xfce.org/xfce/4.12/src/%{name}-%{version}.tar.bz2
# Source0-md5:	8ebfac507b4d6ce3f4bac9d257c2853b
URL:		http://www.xfce.org/projects/xfconf
BuildRequires:	dbus-devel >= 1.1.0
BuildRequires:	dbus-glib-devel >= 0.84
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	perl-ExtUtils-Depends >= 0.3
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.0
BuildRequires:	perl-Glib-devel >= 1.224-2
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
Requires:	dbus-glib >= 0.84
Requires:	dbus-libs >= 1.1.0
Requires:	glib2 >= 1:2.30.0
Requires:	libxfce4util >= %{xfce_version}
Obsoletes:	libxfce4mcs
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
Requires:	dbus-devel >= 1.1.0
Requires:	dbus-glib-devel >= 0.84
Requires:	glib2-devel >= 1:2.30.0
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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Xfconf API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Xfconf.

%package -n perl-Xfce4-Xfconf
Summary:	Perl interface to the Xfce4 Xfconf
Summary(pl.UTF-8):	Interfejs perlowy do Xfce4 Xfconf
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	perl-Glib >= 1.020

%description -n perl-Xfce4-Xfconf
Perl interface to the Xfce4 Xfconf.

%description -n perl-Xfce4-Xfconf -l pl.UTF-8
Interfejs perlowy do Xfce4 Xfconf.

%prep
%setup -q

%build
%configure \
	--enable-gtk-doc \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir} \
	--with-perl-options="INSTALLDIRS=vendor"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Xfce4/Xfconf/.packlist

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
# just a copy or ur
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

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
%attr(755,root,root) %ghost %{_libdir}/libxfconf-0.so.2
%dir %{_libdir}/xfce4/xfconf
%attr(755,root,root) %{_libdir}/xfce4/xfconf/xfconfd
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%{_datadir}/dbus-1/services/org.xfce.Xfconf.service

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfconf-0.so
%{_includedir}/xfce4/xfconf-0
%{_pkgconfigdir}/libxfconf-0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/xfconf

%files -n perl-Xfce4-Xfconf
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/Xfce4
%{perl_vendorarch}/Xfce4/Xfconf.pm
%dir %{perl_vendorarch}/Xfce4/Xfconf
%{perl_vendorarch}/Xfce4/Xfconf/Install
%dir %{perl_vendorarch}/auto/Xfce4
%dir %{perl_vendorarch}/auto/Xfce4/Xfconf
%attr(755,root,root) %{perl_vendorarch}/auto/Xfce4/Xfconf/Xfconf.so
%{_mandir}/man3/Xfce4::Xfconf.3pm*
