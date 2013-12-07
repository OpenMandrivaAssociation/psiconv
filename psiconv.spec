%define major 6
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	PSION 5(MX) file format data conversion utilities
Name:		psiconv
Version:	0.9.8
Release:	23
License:	GPLv2
Group:		File tools
Url:		http://software.frodo.looijaard.name/psiconv/
Source0:	http://software.frodo.looijaard.name/psiconv/files/%{name}-%{version}.tar.bz2
BuildRequires:	bc
BuildRequires:	pkgconfig(ImageMagick)

%description
The Psion 5 has several built-in applications. They use their own file
formats to save data files. Psion has written file conversion
utilities for Windows 95, in the form of their PsiWin program. But
there are no conversion utilities for other operating systems. Also,
Psion is not able to or does not want to release enough data for
others to write their own conversion programs. At least, that is what
I have gathered through the newsgroups and from other sources.

%package -n %{libname}
Summary:	PSION 5(MX) file format data conversion library
Group:		System/Libraries

%description -n %{libname}
This contains a shared library that can be used by programs to convert
PSION files.

%package -n %{devname}
Summary:	PSION 5(MX) file format data conversion library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
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

%files -n %{devname}
%{_libdir}/libpsiconv.so
%{_includedir}/%{name}
%{_bindir}/psiconv-config
%{multiarch_bindir}/psiconv-config
%{_mandir}/man1/psiconv-config.1*

