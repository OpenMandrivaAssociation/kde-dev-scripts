%undefine _debugsource_packages

#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	Various scripts for KDE development
Name:		plasma6-kde-dev-scripts
Version:	24.12.1
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%if 0%{?git:1}
Source0:	https://invent.kde.org/sdk/kde-dev-scripts/-/archive/%{gitbranch}/kde-dev-scripts-%{gitbranchd}.tar.bz2#/kde-dev-scripts-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kde-dev-scripts-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires: 	cmake(KF6DocTools)
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
%{_bindir}/clean-forward-declaration.sh
%{_bindir}/clean-includes.sh
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
%{_bindir}/zonetab2pot.py
%{_bindir}/optimizegraphics
%{_bindir}/wcgrep
%{_bindir}/kde-systemsettings-tree.py
%{_datadir}/uncrustify
%{_bindir}/addmocincludes
%{_bindir}/port_new_gitlab_ci_template.sh
%{_bindir}/uncrustify-kf5
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
%{_mandir}/man1/zonetab2pot.py.1.*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n kde-dev-scripts-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
        -DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build


# (nl) Prefer the file from colorsvn as it is more up to date
# and this fix a conflict between kde-dev-scripts and colorsvn
rm -f %{buildroot}%{_bindir}/colorsvn

%find_lang %{name} --all-name --with-man
