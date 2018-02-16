Summary:	Various scripts for KDE development
Name:		kde-dev-scripts
Version:	 17.12.2
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel >= 5:4.14.8
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
%{_kde_bindir}/adddebug
%{_kde_bindir}/build-progress.sh
%{_kde_bindir}/cheatmake
%{_kde_bindir}/create_cvsignore
%{_kde_bindir}/create_makefile
%{_kde_bindir}/create_makefiles
%{_kde_bindir}/create_svnignore
%{_kde_bindir}/cvs-clean
%{_kde_bindir}/cvsaddcurrentdir
%{_kde_bindir}/cvsbackport
%{_kde_bindir}/cvsblame
%{_kde_bindir}/cvscheck
%{_kde_bindir}/cvsforwardport
%{_kde_bindir}/cvslastchange
%{_kde_bindir}/cvslastlog
%{_kde_bindir}/cvsrevertlast
%{_kde_bindir}/cvsversion
%{_kde_bindir}/cxxmetric
%{_kde_bindir}/c++-copy-class-and-file
%{_kde_bindir}/c++-rename-class-and-file
%{_kde_bindir}/draw_lib_dependencies
%{_kde_bindir}/extend_dmalloc
%{_kde_bindir}/extractattr
%{_kde_bindir}/extractrc
%{_kde_bindir}/findmissingcrystal
%{_kde_bindir}/fix-include.sh
%{_kde_bindir}/fixkdeincludes
%{_kde_bindir}/fixuifiles
%{_kde_bindir}/grantlee_strings_extractor.py
%{_kde_bindir}/includemocs
%{_kde_bindir}/kde_generate_export_header
%{_kde_bindir}/kdedoc
%{_kde_bindir}/kdekillall
%{_kde_bindir}/kdelnk2desktop.py
%{_kde_bindir}/kdemangen.pl
%{_kde_bindir}/krazy-licensecheck
%{_kde_bindir}/makeobj
%{_kde_bindir}/noncvslist
%{_kde_bindir}/nonsvnlist
%{_kde_bindir}/package_crystalsvg
%{_kde_bindir}/png2mng.pl
%{_kde_bindir}/pruneemptydirs
%{_kde_bindir}/qtdoc
%{_kde_bindir}/reviewboard-am
%{_kde_bindir}/svn-clean
%{_kde_bindir}/svnbackport
%{_kde_bindir}/svnchangesince
%{_kde_bindir}/svngettags
%{_kde_bindir}/svnintegrate
%{_kde_bindir}/svnforwardport
%{_kde_bindir}/svnlastchange
%{_kde_bindir}/svnlastlog
%{_kde_bindir}/svnrevertlast
%{_kde_bindir}/svnversions
%{_bindir}/uncrustify-kf5
%{_kde_bindir}/zonetab2pot.py
%{_kde_bindir}/optimizegraphics
%{_kde_bindir}/wcgrep
%{_kde_bindir}/kde-systemsettings-tree.py
%{_datadir}/uncrustify
%{_kde_mandir}/man1/adddebug.1.*
%{_kde_mandir}/man1/cheatmake.1.*
%{_kde_mandir}/man1/create_cvsignore.1.*
%{_kde_mandir}/man1/create_makefile.1.*
%{_kde_mandir}/man1/create_makefiles.1.*
%{_kde_mandir}/man1/cvscheck.1.*
%{_kde_mandir}/man1/cvslastchange.1.*
%{_kde_mandir}/man1/cvslastlog.1.*
%{_kde_mandir}/man1/cvsrevertlast.1.*
%{_kde_mandir}/man1/cxxmetric.1.*
%{_kde_mandir}/man1/extend_dmalloc.1.*
%{_kde_mandir}/man1/extractrc.1.*
%{_kde_mandir}/man1/fixincludes.1.*
%{_kde_mandir}/man1/pruneemptydirs.1.*
%{_kde_mandir}/man1/qtdoc.1.*
%{_kde_mandir}/man1/reportview.1.*
%{_kde_mandir}/man1/transxx.1.*
%{_kde_mandir}/man1/zonetab2pot.py.1.*

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde4

%build
%make -C build

%install
%makeinstall_std -C build


# (nl) Prefer the file from colorsvn as it is more up to date
# and this fix a conflict between kde-dev-scripts and colorsvn
rm -f %{buildroot}%{_kde_bindir}/colorsvn

%find_lang %{name} --all-name --with-man
