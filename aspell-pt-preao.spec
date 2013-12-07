%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define intname aspell6
%define intver 20110424

%define languageglazy Portuguese
%define languagecode pt-preao
%define lc_ctype pt_PT-preao


Summary:	%{languageglazy} files previous to 1990 orthography agreement for aspell
Name:		aspell-%{languagecode}
Version:	0.60.0
Release:	8
Group:		System/Internationalization
License:	GPL
URL:		http://aspell.sourceforge.net/
# http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
Source0:	http://natura.di.uminho.pt/download/sources/Dictionaries/aspell6/%{intname}.%{languagecode}-%{intver}.tar.bz2
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
Provides:	%{intname}-%{languagecode}
Obsoletes:	ispell-pt
Provides:	ispell-pt

%description
A %{languageglazy} dictionary previous to the orthography agreement made in 1990
to use with aspell, a spelling checker.
Version %{intver}.

%prep
%setup -qn %{intname}-%{lc_ctype}-%{intver}-0

%build
# don't use configure macro
./configure
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Copyright COPYING doc/LEIAME-preao.txt
%{_libdir}/aspell-0.60




%changelog
* Tue May 10 2011 José Melo <ze@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 673204
- 20110424-0

* Tue Apr 12 2011 José Melo <ze@mandriva.org> 0.60.0-1
+ Revision: 652768
- imported package aspell-pt-preao

