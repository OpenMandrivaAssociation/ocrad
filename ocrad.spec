Summary: 	Optical Character Recognition
Name: 		ocrad
Version: 	0.23
Release: 	1
License: 	GPLv3+
Group: 		Publishing
Source: 	http://ftp.gnu.org/gnu/ocrad/%{name}-%{version}.tar.xz
URL: 		http://www.gnu.org/software/ocrad/ocrad.html

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
./configure --prefix=%{_prefix} --libdir=%{_libdir} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" CPPFLAGS="%{optflags}" LDFLAGS="%{?ldflags}"
%make

%install
export PATH=$PATH:/sbin
%makeinstall_std

%files
%doc README COPYING INSTALL ChangeLog
%{_bindir}/*
%{_infodir}/*
%{_mandir}/man1/*.1.*

%files devel
%{_includedir}/ocradlib.h
%{_libdir}/libocrad.a
