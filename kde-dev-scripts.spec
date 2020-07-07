Summary:	Various scripts for KDE development
Name:		kde-dev-scripts
Version:	20.04.3
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires: 	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	docbook-dtd42-xml
Requires:	colorsvn
Conflicts:	kdesdk4-core < 1:4.11.0
Conflicts:	kdesdk4-scripts < 1:4.11.0
Obsoletes:	kdesdk4-scripts < 1:4.11.0
BuildArch:	noarch

%description
This package contains various scripts for KDE development.

%files -f %{name}.lang
%{_bindir}/adddebug
%{_bindir}/build-progress.sh
%{_bindir}/cheatmake
%{_bindir}/create_cvsignore
%{_bindir}/create_makefile
%{_bindir}/create_makefiles
%{_bindir}/create_svnignore
%{_bindir}/cvs-clean
%{_bindir}/cvsaddcurrentdir
%{_bindir}/cvsbackport
%{_bindir}/cvsblame
%{_bindir}/cvscheck
%{_bindir}/cvsforwardport
%{_bindir}/cvslastchange
%{_bindir}/cvslastlog
%{_bindir}/cvsrevertlast
%{_bindir}/cvsversion
%{_bindir}/cxxmetric
%{_bindir}/c++-copy-class-and-file
%{_bindir}/c++-rename-class-and-file
%{_bindir}/draw_lib_dependencies
%{_bindir}/extend_dmalloc
%{_bindir}/extractattr
%{_bindir}/extractrc
%{_bindir}/findmissingcrystal
%{_bindir}/fix-include.sh
%{_bindir}/fixkdeincludes
%{_bindir}/fixuifiles
%{_bindir}/grantlee_strings_extractor.py
%{_bindir}/includemocs
%{_bindir}/kde_generate_export_header
%{_bindir}/kdedoc
%{_bindir}/kdekillall
%{_bindir}/kdelnk2desktop.py
%{_bindir}/kdemangen.pl
%{_bindir}/krazy-licensecheck
%{_bindir}/makeobj
%{_bindir}/noncvslist
%{_bindir}/nonsvnlist
%{_bindir}/package_crystalsvg
%{_bindir}/png2mng.pl
%{_bindir}/pruneemptydirs
%{_bindir}/qtdoc
%{_bindir}/reviewboard-am
%{_bindir}/svn-clean
%{_bindir}/svnbackport
%{_bindir}/svnchangesince
%{_bindir}/svngettags
%{_bindir}/svnintegrate
%{_bindir}/svnforwardport
%{_bindir}/svnlastchange
%{_bindir}/svnlastlog
%{_bindir}/svnrevertlast
%{_bindir}/svnversions
%{_bindir}/uncrustify-kf5
%{_bindir}/zonetab2pot.py
%{_bindir}/optimizegraphics
%{_bindir}/wcgrep
%{_bindir}/kde-systemsettings-tree.py
%{_datadir}/uncrustify
%{_mandir}/man1/adddebug.1.*
%{_mandir}/man1/cheatmake.1.*
%{_mandir}/man1/create_cvsignore.1.*
%{_mandir}/man1/create_makefile.1.*
%{_mandir}/man1/create_makefiles.1.*
%{_mandir}/man1/cvscheck.1.*
%{_mandir}/man1/cvslastchange.1.*
%{_mandir}/man1/cvslastlog.1.*
%{_mandir}/man1/cvsrevertlast.1.*
%{_mandir}/man1/cxxmetric.1.*
%{_mandir}/man1/extend_dmalloc.1.*
%{_mandir}/man1/extractrc.1.*
%{_mandir}/man1/fixincludes.1.*
%{_mandir}/man1/pruneemptydirs.1.*
%{_mandir}/man1/qtdoc.1.*
%{_mandir}/man1/reportview.1.*
%{_mandir}/man1/transxx.1.*
%{_mandir}/man1/zonetab2pot.py.1.*

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build


# (nl) Prefer the file from colorsvn as it is more up to date
# and this fix a conflict between kde-dev-scripts and colorsvn
rm -f %{buildroot}%{_bindir}/colorsvn

%find_lang %{name} --all-name --with-man
