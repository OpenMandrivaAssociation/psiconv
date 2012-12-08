%define major 6
%define libname %mklibname %{name} %major
%define develname %mklibname -d %{name}

Summary: PSION 5(MX) file format data conversion utilities
Name: psiconv
Version: 0.9.8
Release: 21
License: GPL
Group: File tools
Url: http://software.frodo.looijaard.name/psiconv/
Source0: http://software.frodo.looijaard.name/psiconv/files/%{name}-%{version}.tar.bz2

BuildRequires: pkgconfig(ImageMagick)
BuildRequires: bc

%description
The Psion 5 has several built-in applications. They use their own file
formats to save data files. Psion has written file conversion
utilities for Windows 95, in the form of their PsiWin program. But
there are no conversion utilities for other operating systems. Also,
Psion is not able to or does not want to release enough data for
others to write their own conversion programs. At least, that is what
I have gathered through the newsgroups and from other sources.

%package -n %{libname}
Group: System/Libraries
Summary: PSION 5(MX) file format data conversion library

%description -n %{libname}
The Psion 5 has several built-in applications. They use their own file
formats to save data files. Psion has written file conversion
utilities for Windows 95, in the form of their PsiWin program. But
there are no conversion utilities for other operating systems. Also,
Psion is not able to or does not want to release enough data for
others to write their own conversion programs. At least, that is what
I have gathered through the newsgroups and from other sources.

This contains a shared library that can be used by programs to convert
PSION files.

%package -n %{develname}
Group: Development/C
Summary: PSION 5(MX) file format data conversion library
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{mklibname -d psiconv 6}

%description -n %{develname}
The Psion 5 has several built-in applications. They use their own file
formats to save data files. Psion has written file conversion
utilities for Windows 95, in the form of their PsiWin program. But
there are no conversion utilities for other operating systems. Also,
Psion is not able to or does not want to release enough data for
others to write their own conversion programs. At least, that is what
I have gathered through the newsgroups and from other sources.

Install this if you want to compile an application that uses psiconv
to convert PSION files.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/psiconv-config

rm -rf %{buildroot}%{_datadir}/psiconv/xhtml

%files
%doc TODO README NEWS AUTHORS ChangeLog
%dir %{_sysconfdir}/psiconv/
%config(noreplace) %{_sysconfdir}/psiconv/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}

%files -n %{libname}
%{_libdir}/libpsiconv.so.%{major}*

%files -n %{develname}
%{_libdir}/libpsiconv.so
%{_includedir}/%{name}
%{_bindir}/psiconv-config
%{multiarch_bindir}/psiconv-config
%{_mandir}/man1/psiconv-config.1*



%changelog
* Sat Dec 24 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.9.8-20
+ Revision: 745063
- rebuild for new imagemagick
- cleaned up spec

* Mon May 09 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.8-19
+ Revision: 672724
- fix devel name
- fix major

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.8-17
+ Revision: 667894
- mass rebuild
- multiarch fixes

* Thu Jul 15 2010 Funda Wang <fwang@mandriva.org> 0.9.8-16mdv2011.0
+ Revision: 553567
- rebuild for new imagemagick

* Thu Jan 14 2010 Funda Wang <fwang@mandriva.org> 0.9.8-15mdv2010.1
+ Revision: 491142
- rebuild for new imagemagick

* Thu Jan 14 2010 Funda Wang <fwang@mandriva.org> 0.9.8-14mdv2010.1
+ Revision: 491132
- rebuild for new imagemagick

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.8-13mdv2010.0
+ Revision: 426786
- rebuild

* Thu Dec 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.8-12mdv2009.1
+ Revision: 312959
- lowercase ImageMagick

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9.8-12mdv2009.0
+ Revision: 225101
- rebuild
- fix spacing at top of description

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 11 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.8-11mdv2008.1
+ Revision: 165133
- rebuild for new libmagick

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.9.8-10mdv2008.1
+ Revision: 140737
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 07 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.9.8-10mdv2008.0
+ Revision: 24905
- Rebuild with new libjasper.


* Sun Feb 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.8-9mdv2007.0
+ Revision: 122350
- rebuild for new ImageMagick

* Tue Jan 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.8-8mdv2007.1
+ Revision: 103067
- Import psiconv

* Tue Jan 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.8-8mdv2007.1
- Rebuild

* Fri Sep 01 2006 Götz Waschk <waschk@mandriva.org> 0.9.8-7mdv2007.0
- fix buildrequires
- rebuild for new Magick

* Fri Aug 04 2006 Frederic Crozat <fcrozat@mandriva.com> 0.9.8-6mdv2007.0
- Rebuild with latest dbus

* Fri Jun 09 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.8-5mdk
- rebuild for new Magick

* Wed Mar 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.8-4mdk
- rebuild for new Magick

* Mon Jan 30 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.8-3mdk
- rebuild for new Magick

* Wed Dec 28 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.8-2mdk
- rebuild for new Magick
- use mkrel

* Mon Nov 28 2005 Götz Waschk <waschk@mandriva.org> 0.9.8-1mdk
- drop patch
- new url
- New release 0.9.8

* Thu Aug 25 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-6mdk
- rebuilt against new Magick libs

* Tue Aug 16 2005 Marcel Pol <mpol@mandriva.org> 0.9.6-5mdk
- rebuild for new xorg

* Sat Aug 06 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-4mdk
- rebuilt against latest libMagick

* Sat Apr 02 2005 Nicolas Lécureuil <neoclust@mandrake.org> 0.9.6-3mdk
- rebuild

* Mon Jan 31 2005 Götz Waschk <waschk@linux-mandrake.com> 0.9.6-2mdk
- multiarch support

* Fri Sep 10 2004 Götz Waschk <waschk@linux-mandrake.com> 0.9.6-1mdk
- initial package

