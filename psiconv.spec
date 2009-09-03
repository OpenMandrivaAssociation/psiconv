%define name psiconv
%define version 0.9.8
%define release %mkrel 13
%define libname %mklibname %name 6

Summary: PSION 5(MX) file format data conversion utilities
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://software.frodo.looijaard.name/psiconv/files/%{name}-%{version}.tar.bz2
License: GPL
Group: File tools
Url: http://software.frodo.looijaard.name/psiconv/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: imagemagick-devel
BuildRequires: bc

%description
The Psion 5 has several built-in applications. They use their own file
formats to save data files. Psion has written file conversion
utilities for Windows 95, in the form of their PsiWin program. But
there are no conversion utilities for other operating systems. Also,
Psion is not able to or does not want to release enough data for
others to write their own conversion programs. At least, that is what
I have gathered through the newsgroups and from other sources.

%package -n %libname
Group: System/Libraries
Summary: PSION 5(MX) file format data conversion library

%description -n %libname
The Psion 5 has several built-in applications. They use their own file
formats to save data files. Psion has written file conversion
utilities for Windows 95, in the form of their PsiWin program. But
there are no conversion utilities for other operating systems. Also,
Psion is not able to or does not want to release enough data for
others to write their own conversion programs. At least, that is what
I have gathered through the newsgroups and from other sources.

This contains a shared library that can be used by programs to convert
PSION files.

%package -n %libname-devel
Group: Development/C
Summary: PSION 5(MX) file format data conversion library
Requires: %libname = %version
Provides: libpsiconv-devel = %version-%release

%description -n %libname-devel
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
%configure2_5x
%make
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%multiarch_binaries %buildroot%_bindir/psiconv-config
rm -rf %buildroot%_datadir/psiconv/xhtml

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc TODO README NEWS AUTHORS ChangeLog
%dir %_sysconfdir/psiconv/
%config(noreplace) %_sysconfdir/psiconv/*
%_bindir/%name
%_mandir/man1/%name.1*
%_datadir/%name

%files -n %libname
%defattr(-,root,root)
%_libdir/libpsiconv.so.*

%files -n %libname-devel
%defattr(-,root,root)
%_libdir/libpsiconv.so
%attr(644,root,root) %_libdir/libpsiconv.la
%_libdir/libpsiconv.a
%_includedir/%name
%_bindir/psiconv-config
%_bindir/*/psiconv-config
%_mandir/man1/psiconv-config.1*


