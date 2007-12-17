Name: x11-docs
Version: 1.4
Release: %mkrel 1
Summary: Xorg X11 documentation
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/doc/xorg-docs-%{version}.tar.bz2
License: MIT

BuildRequires: x11-util-macros >= 1.0.1

#Obsoletes: xorg-x11-doc < 7.0
#Provides: xorg-x11-doc = 7.0
Provides: X11-doc = 7.0

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
%{_datadir}/X11/doc/input/*.sgml
%{_datadir}/X11/doc/platforms/*.sgml
%{_datadir}/X11/doc/security/*.sgml
%{_datadir}/X11/doc/MAINTAINERS
%{_datadir}/X11/doc/hardcopy/BDF/bdf.PS.gz
%{_datadir}/X11/doc/hardcopy/CTEXT/ctext.PS.gz
%{_datadir}/X11/doc/hardcopy/FSProtocol/fsproto.PS.gz
%{_datadir}/X11/doc/hardcopy/ICCCM/icccm.PS.gz
%{_datadir}/X11/doc/hardcopy/ICCCM/icccm.idx.PS.gz
%{_datadir}/X11/doc/hardcopy/ICE/ICElib.PS.gz
%{_datadir}/X11/doc/hardcopy/ICE/ice.PS.gz
%{_datadir}/X11/doc/hardcopy/RX/RX.PS.gz
%{_datadir}/X11/doc/hardcopy/SM/SMlib.PS.gz
%{_datadir}/X11/doc/hardcopy/SM/xsmp.PS.gz
%{_datadir}/X11/doc/hardcopy/X11/xlib.PS.gz
%{_datadir}/X11/doc/hardcopy/X11/xlib.idx.PS.gz
%{_datadir}/X11/doc/hardcopy/XDMCP/xdmcp.PS.gz
%{_datadir}/X11/doc/hardcopy/XIM/xim.PS.gz
%{_datadir}/X11/doc/hardcopy/XKB/XKBlib.ps.gz
%{_datadir}/X11/doc/hardcopy/XKB/XKBproto.ps.gz
%{_datadir}/X11/doc/hardcopy/XLFD/xlfd.PS.gz
%{_datadir}/X11/doc/hardcopy/XPRINT/Xprint_FAQ.html
%{_datadir}/X11/doc/hardcopy/XPRINT/Xprint_FAQ.txt
%{_datadir}/X11/doc/hardcopy/XPRINT/Xprint_FAQ.xml
%{_datadir}/X11/doc/hardcopy/XPRINT/Xprint_old_FAQ.txt
%{_datadir}/X11/doc/hardcopy/XPRINT/dtprint_fspec.PS.gz
%{_datadir}/X11/doc/hardcopy/XPRINT/xp_library.PS.gz
%{_datadir}/X11/doc/hardcopy/XPRINT/xp_proto.PS.gz
%{_datadir}/X11/doc/hardcopy/XProtocol/proto.PS.gz
%{_datadir}/X11/doc/hardcopy/XProtocol/proto.idx.PS.gz
%{_datadir}/X11/doc/hardcopy/Xaw/widg.idx.PS.gz
%{_datadir}/X11/doc/hardcopy/Xaw/widgets.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/AppGroup.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/DPMS.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/DPMSLib.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/bigreq.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/buffer.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/dbe.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/dbelib.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/evi.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/lbx.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/lbx.html
%{_datadir}/X11/doc/hardcopy/Xext/lbxTOC.html
%{_datadir}/X11/doc/hardcopy/Xext/lbxalg.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/mit-shm.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/record.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/recordlib.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/security.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/shape.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/shapelib.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/sync.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/synclib.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/tog-cup.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/xc-misc.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/xtest.PS.gz
%{_datadir}/X11/doc/hardcopy/Xext/xtestlib.PS.gz
%{_datadir}/X11/doc/hardcopy/Xi/lib.PS.gz
%{_datadir}/X11/doc/hardcopy/Xi/port.PS.gz
%{_datadir}/X11/doc/hardcopy/Xi/proto.PS.gz
%{_datadir}/X11/doc/hardcopy/Xmu/xmu.PS.gz
%{_datadir}/X11/doc/hardcopy/Xserver/Xprt.PS.gz
%{_datadir}/X11/doc/hardcopy/Xserver/analysis.PS.gz
%{_datadir}/X11/doc/hardcopy/Xserver/appgroup.PS.gz
%{_datadir}/X11/doc/hardcopy/Xserver/ddx.PS.gz
%{_datadir}/X11/doc/hardcopy/Xserver/fontlib.PS.gz
%{_datadir}/X11/doc/hardcopy/Xserver/secint.PS.gz
%{_datadir}/X11/doc/hardcopy/Xt/intr.idx.PS.gz
%{_datadir}/X11/doc/hardcopy/Xt/intrinsics.PS.gz
%{_datadir}/X11/doc/hardcopy/Xv/video
%{_datadir}/X11/doc/hardcopy/Xv/xv-protocol-v2.PS
%{_datadir}/X11/doc/hardcopy/i18n/Framework.PS.gz
%{_datadir}/X11/doc/hardcopy/i18n/LocaleDB.PS.gz
%{_datadir}/X11/doc/hardcopy/i18n/Trans.PS.gz
%{_datadir}/X11/doc/hardcopy/man/man.PS.gz
%{_datadir}/X11/doc/hardcopy/rstart/rstart.PS.gz
%{_datadir}/X11/doc/hardcopy/saver/saver.PS.gz
%{_datadir}/X11/doc/hardcopy/xfs/design.PS.gz
%{_datadir}/X11/doc/hardcopy/xtrans/Xtrans.PS.gz
%{_mandir}/man7/Consortium.7.*
%{_mandir}/man7/Standards.7.*
%{_mandir}/man7/X.7.*
%{_mandir}/man7/XOrgFoundation.7.*
%{_mandir}/man7/XProjectTeam.7.*
%{_mandir}/man7/Xprint.7.*
%{_mandir}/man7/security.7.*
