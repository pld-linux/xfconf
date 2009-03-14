#
%include	/usr/lib/rpm/macros.perl
#
Summary:	Simple configuration storage and query system
Summary(pl.UTF-8):	Prosty system przechowywania i odpytywania konfiguracji
Name:		xfconf
Version:	4.6.0
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	38595f78379eb1f456e97b393fdafd20
URL:		http://www.xfce.org/projects/xfconf/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	dbus-glib-devel >= 0.72
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool
BuildRequires:	libxfce4util-devel >= %{version}
BuildRequires:	perl-ExtUtils-Depends >= 0.3
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.0
BuildRequires:	perl-Glib >= 1.020
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	xfce4-dev-tools >= %{version}
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
Requires:	dbus-devel >= 1.0.0
Requires:	dbus-glib-devel >= 0.72
Requires:	glib2-devel >= 1:2.12.0
Obsoletes:	libxfce4mcs-devel
Obsoletes:	xfce-mcs-manager-devel

%description devel
Header files for Xfconf library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Xfconf.

%package static
Summary:	Static Xfconf library
Summary(pl.UTF-8):	Statyczna biblioteka Xfconf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libxfce4mcs-static

%description static
Static Xfconf library.

%description static -l pl.UTF-8
Statyczna biblioteka Xfconf.

%package apidocs
Summary:	Xfconf API documentation
Summary(pl.UTF-8):	Dokumentacja API Xfconf
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	libxfce4mcs-apidocs

%description apidocs
Xfconf API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Xfconf.

%package -n perl-Xfce4-Xfconf
Summary:	Perl interface to the Xfce4 Xfconf
Summary(pl.UTF-8):	Interfejs perlowy do Xfce4 Xfconf
Group:		Development/Languages/Perl
Requires:	perl-Glib >= 1.020

%description -n perl-Xfce4-Xfconf
Perl interface to the Xfce4 Xfconf.

%description -n perl-Xfce4-Xfconf -l pl.UTF-8
Interfejs perlowy do Xfce4 Xfconf.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
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
%attr(755,root,root) %{_libdir}/xfconfd
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%{_datadir}/dbus-1/services/org.xfce.Xfconf.service

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfconf-0.so
%{_libdir}/libxfconf-0.la
%{_includedir}/xfce4/xfconf-0
%{_pkgconfigdir}/libxfconf-0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxfconf-0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/xfconf

%files -n perl-Xfce4-Xfconf
%defattr(644,root,root,755)
%attr(755,root,root) %{perl_vendorarch}/auto/Xfce4/Xfconf/Xfconf.so
%dir %{perl_vendorarch}/Xfce4
%{perl_vendorarch}/Xfce4/Xfconf.pm
%dir %{perl_vendorarch}/Xfce4/Xfconf
%{perl_vendorarch}/Xfce4/Xfconf/Install
%dir %{perl_vendorarch}/auto/Xfce4
%dir %{perl_vendorarch}/auto/Xfce4/Xfconf
%{perl_vendorarch}/auto/Xfce4/Xfconf/*.bs
%{_mandir}/man3/Xfce4::Xfconf.3pm*
