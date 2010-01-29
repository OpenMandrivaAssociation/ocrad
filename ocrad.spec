%define name ocrad
%define version 0.19
%define release %mkrel 1

Version: 	%{version}
Summary: 	Optical Character Recognition
Name: 		%{name}
Release: 	%{release}
License: 	GPLv3+
Group: 		Publishing
Source: 	http://ftp.gnu.org/gnu/ocrad/%{name}-%{version}.tar.gz
URL: 		http://www.gnu.org/software/ocrad/ocrad.html
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	info-install

%description
Ocrad is an OCR (Optical Character Recognition) program implemented 
as a filter and based on a feature extraction method. It reads a 
bitmap image in PBM format and outputs text in the ISO-8859-1 
(Latin-1) charset. It includes a layout analyser that is able to 
separate the columns or blocks of text normally found on printed 
pages. Ocrad can be used as a stand-alone console application, or as 
a backend to other programs

%package devel
Group: Publishing
Summary: Header files needed for ocard development

%description devel
This package contains header files needed for ocard development.

%prep
%setup -q

%build
./configure --prefix=%_prefix --libdir=%_libdir CFLAGS="%optflags" CXXFLAGS="%optflags" CPPFLAGS="%optflags" LDFLAGS="%{?ldflags}"
%make

%install
rm -fr %buildroot
export PATH=$PATH:/sbin
%makeinstall_std

%post
%_install_info %name.info

%postun
%_remove_install_info %name.info

%clean
rm -rf %buildroot

%files
%defattr (-,root,root)
%doc README COPYING INSTALL TODO ChangeLog
%_bindir/*
%_infodir/*
%_mandir/man1/*.1.*

%files devel
%defattr (-,root,root)
%{_includedir}/ocradlib.h
%{_libdir}/libocrad.a
