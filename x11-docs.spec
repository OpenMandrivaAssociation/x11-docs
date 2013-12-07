Name:		x11-docs
Version:	1.7
Release:	4
Summary:	Xorg X11 documentation
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/doc/xorg-docs-%{version}.tar.bz2
License:	MIT
BuildRequires:	x11-util-macros >= 1.0.1
BuildArch:	noarch

%description
Xorg X11 documentation

%prep
%setup -q -n xorg-docs-%{version}

%build
%configure2_5x	\
		--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}
%make

%install
%makeinstall_std

%files
%{_datadir}/doc/xorg-docs/
%{_mandir}/man7/Consortium.7.*
%{_mandir}/man7/Standards.7.*
%{_mandir}/man7/X.7.*
%{_mandir}/man7/XOrgFoundation.7.*
%{_mandir}/man7/XProjectTeam.7.*
%{_mandir}/man7/Xsecurity.7.*
