%define name ocrad
%define version 0.21
%define release  2

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


%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.21-1mdv2011.0
+ Revision: 645353
- update to new version 0.21

* Tue Jul 20 2010 Funda Wang <fwang@mandriva.org> 0.20-1mdv2011.0
+ Revision: 555065
- update to new version 0.20

* Fri Jan 29 2010 Funda Wang <fwang@mandriva.org> 0.19-1mdv2010.1
+ Revision: 497883
- New version 0.19

* Mon May 11 2009 Funda Wang <fwang@mandriva.org> 0.18-1mdv2010.0
+ Revision: 374118
- New version 0.18

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.17-1mdv2008.1
+ Revision: 136634
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jul 07 2007 Austin Acton <austin@mandriva.org> 0.17-1mdv2008.0
+ Revision: 49287
- new version
- enforce build flags


* Wed Oct 25 2006 Lenny Cartier <lenny@mandriva.com> 0.16-1mdv2007.0
+ Revision: 72336
- Import ocrad

