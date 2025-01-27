#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-System-Command
Version  : 1.122
Release  : 33
URL      : https://cpan.metacpan.org/authors/id/B/BO/BOOK/System-Command-1.122.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BO/BOOK/System-Command-1.122.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libsystem-command-perl/libsystem-command-perl_1.119-1.debian.tar.xz
Summary  : 'Object for running system commands'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-System-Command-license = %{version}-%{release}
Requires: perl-System-Command-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(IPC::Run)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
System::Command - Object for running system commands
SYNOPSIS
use System::Command;

%package dev
Summary: dev components for the perl-System-Command package.
Group: Development
Provides: perl-System-Command-devel = %{version}-%{release}
Requires: perl-System-Command = %{version}-%{release}

%description dev
dev components for the perl-System-Command package.


%package license
Summary: license components for the perl-System-Command package.
Group: Default

%description license
license components for the perl-System-Command package.


%package perl
Summary: perl components for the perl-System-Command package.
Group: Default
Requires: perl-System-Command = %{version}-%{release}

%description perl
perl components for the perl-System-Command package.


%prep
%setup -q -n System-Command-1.122
cd %{_builddir}
tar xf %{_sourcedir}/libsystem-command-perl_1.119-1.debian.tar.xz
cd %{_builddir}/System-Command-1.122
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/System-Command-1.122/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-System-Command
cp %{_builddir}/System-Command-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-System-Command/3af8122c1ecbbbc8627e2830fba209099ad6749b || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-System-Command/ddc9fa9e1985900f098122f6284ff2c563498596 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/System::Command.3
/usr/share/man/man3/System::Command::Reaper.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-System-Command/3af8122c1ecbbbc8627e2830fba209099ad6749b
/usr/share/package-licenses/perl-System-Command/ddc9fa9e1985900f098122f6284ff2c563498596

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
