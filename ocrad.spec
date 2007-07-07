%define name ocrad
%define version 0.17
%define release %mkrel 1


Version: 	%{version}
Summary: 	Optical Character Recognition
Name: 		%{name}
Release: 	%{release}
License: 	GPL
Group: 		Publishing
Source: 	http://ftp.gnu.org/gnu/ocrad/%{name}-%{version}.tar.bz2
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

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
./configure --prefix=%_prefix CFLAGS="%optflags" CXXFLAGS="%optflags" CPPFLAGS="%optflags"
%make

%install
export PATH=$PATH:/sbin
%makeinstall

%post
%_install_info %name.info

%postun
%_remove_install_info %name.info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README COPYING INSTALL TODO ChangeLog
%_bindir/*
%_infodir/*
