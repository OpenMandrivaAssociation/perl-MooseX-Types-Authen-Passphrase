%define upstream_name    MooseX-Types-Authen-Passphrase
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Authen::Passphrase type constraint and coercions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Authen::Passphrase)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(MooseX::Types::Moose)
BuildRequires:	perl(Test::use::ok)
BuildArch:	noarch

%description
This the MooseX::Types manpage library provides string coercions for the
the Authen::Passphrase manpage family of classes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.20.0-3mdv2011.0
+ Revision: 655603
- rebuild for updated spec-helper

* Mon Aug 30 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 574421
- update summary

* Fri Aug 27 2010 Shlomi Fish <shlomif@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 573484
- import perl-MooseX-Types-Authen-Passphrase

