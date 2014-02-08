Name:		x11-docs
Version:	1.6
Release:	5
Summary:	Xorg X11 documentation
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source:		http://xorg.freedesktop.org/releases/individual/doc/xorg-docs-%{version}.tar.bz2
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



%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6-2mdv2011.0
+ Revision: 671117
- mass rebuild

* Mon Dec 20 2010 Thierry Vignaud <tv@mandriva.org> 1.6-1mdv2011.0
+ Revision: 623285
- new release

* Fri Nov 12 2010 Thierry Vignaud <tv@mandriva.org> 1.5.99.901-1mdv2011.0
+ Revision: 596992
- new release
- adjust file list

* Fri Nov 13 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.5-2mdv2010.1
+ Revision: 465825
- Obsolete xorg-x11-doc
  Remove "Provides: X11-doc" since this is old and not required by any package

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.5-1mdv2010.1
+ Revision: 464159
- New version: 1.5

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.4-4mdv2009.1
+ Revision: 351426
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.4-3mdv2009.0
+ Revision: 225941
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4-2mdv2008.1
+ Revision: 179658
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4-1mdv2008.0
+ Revision: 55473
- new upstream version
- fix file list
- manpages are now compressed with lzma


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Thu May 11 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-11 17:06:57 (27120)
- incrementing release

* Thu May 11 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-11 16:42:39 (27111)
- do not obsolete xorg-x11-doc as we have a metapackage with
  exactly that name

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

