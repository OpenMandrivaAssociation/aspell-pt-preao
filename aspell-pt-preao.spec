%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define langglazy Portuguese
%define langcode pt-preao
%define lc_ctype pt_PT-preao
%define intname aspell6
%define intver 20110410-0


Summary:	%{langglazy} files previous to 1990 orthography agreement for aspell
Name:		aspell-%{langcode}
Version:	0.60.0
Release:	%mkrel 1
Group:		System/Internationalization
License:	GPL
URL:		http://aspell.sourceforge.net/
# http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
Source0:	http://natura.di.uminho.pt/download/sources/Dictionaries/aspell6/LATEST/%{intname}.%{langcode}-latest.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	aspell >= 0.60
BuildRequires:	make
Requires:	aspell >= 0.60
# Mandriva Stuff
Requires:	locales-pt
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	%{intname}-%{lc_ctype}
Provides:	%{intname}-%{langcode}
Obsoletes:	ispell-pt
Provides:	ispell-pt

%description
A %{langglazy} dictionary previous to the orthography agreement made in 1990
to use with aspell, a spelling checker.
Version %{intver}.

%prep
%setup -qn %{intname}-%{lc_ctype}-%{intver}

%build
# don't use configure macro
./configure
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc README Copyright COPYING
%{_libdir}/aspell-0.60


