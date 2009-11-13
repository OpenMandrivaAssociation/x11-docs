Name: x11-docs
Version: 1.5
Release: %mkrel 2
Summary: Xorg X11 documentation
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/doc/xorg-docs-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros >= 1.0.1

# This package was used in the transition to modular:
Obsoletes: xorg-x11-doc

%description
Xorg X11 documentation

%prep
%setup -q -n xorg-docs-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/X11/doc/*sgml
%{_datadir}/X11/doc/core/*.sgml
%{_datadir}/X11/doc/fonts/*.sgml
%{_datadir}/X11/doc/graphics/*.sgml
%{_datadir}/X11/doc/input/*.sgml
%{_datadir}/X11/doc/platforms/*.sgml
%{_datadir}/X11/doc/security/*.sgml
%{_datadir}/X11/doc/MAINTAINERS
%{_mandir}/man7/Consortium.7.*
%{_mandir}/man7/Standards.7.*
%{_mandir}/man7/X.7.*
%{_mandir}/man7/XOrgFoundation.7.*
%{_mandir}/man7/XProjectTeam.7.*
%{_mandir}/man7/Xsecurity.7.*
