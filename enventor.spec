%define		efl_ver		1.9.0
%define		elementary_ver	1.9.0

Summary:	Enventor - EDC editor with some convenient functions
Summary(pl.UTF-8):	Enventor - edytor EDC z kilkoma wygodnymi funkcjami
Name:		enventor
Version:	0.3.0
Release:	1
License:	BSD
Group:		Applications/Network
Source0:	http://download.enlightenment.org/rel/apps/enventor/%{name}-%{version}.tar.bz2
# Source0-md5:	8566e8f6a95a1708d4142e1ec9590a7b
URL:		http://enlightenment.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	ecore-devel >= %{efl_ver}
BuildRequires:	ecore-ipc-devel >= %{efl_ver}
BuildRequires:	edje >= %{efl_ver}
BuildRequires:	edje-devel >= %{efl_ver}
BuildRequires:	eet-devel >= %{efl_ver}
BuildRequires:	eina-devel >= %{efl_ver}
BuildRequires:	eio-devel >= %{efl_ver}
BuildRequires:	elementary-devel >= %{elementary_ver}
BuildRequires:	eo-devel >= %{efl_ver}
BuildRequires:	evas-devel >= %{efl_ver}
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	ecore >= %{efl_ver}
Requires:	ecore-ipc >= %{efl_ver}
Requires:	edje-libs >= %{efl_ver}
Requires:	eet >= %{efl_ver}
Requires:	eina >= %{efl_ver}
Requires:	eio >= %{efl_ver}
Requires:	elementary >= %{elementary_ver}
Requires:	eo >= %{efl_ver}
Requires:	evas >= %{efl_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enventor is an EDC editor with some convenient functions.

%description -l pl.UTF-8
Enventor to edytor EDC z kilkoma wygodnymi funkcjami.

%prep
%setup -q

# non-themed icons go to pixmapsdir
%{__sed} -i -e 's,/icons$,/pixmaps,' data/icon/Makefile.am

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/enventor
%{_datadir}/enventor
%{_desktopdir}/enventor.desktop
%{_pixmapsdir}/enventor.png
