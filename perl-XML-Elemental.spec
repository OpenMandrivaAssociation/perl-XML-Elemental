%define upstream_name    XML-Elemental
%define upstream_version 2.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Simplistic and perlish handling of XML data
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(XML::SAX)

BuildArch:	noarch

%description
XML::Elemental is a SAX-based package for easily parsing XML documents into a
more native and mostly object-oriented perl form.

The development of this package grew out of the desire for something more
object-oriented then XML::Simple and was more simplistic and perlish then the
various standard XML API modules such as XML::DOM. Easier installation of
modules was also a contributing factor.

Original this package began as a style plugin to XML::Parser. That proved to be
too limiting that it was expanded. With the release of version 2.0 the package
was refactored to take advantage of any parser supporting SAX that includes the
pure perl option that ships with XML::SAX.

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
%doc Changes README
%{perl_vendorlib}/XML
%{_mandir}/man3*/*

%changelog
* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 2.110.0-1mdv2010.1
+ Revision: 471056
- update to 2.11

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.1-5mdv2010.0
+ Revision: 430663
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 2.1-4mdv2009.0
+ Revision: 258840
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.1-3mdv2009.0
+ Revision: 246728
- rebuild

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.1-1mdv2008.1
+ Revision: 152903
- update to new version 2.1
- update to new version 2.1

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.0-1mdv2008.1
+ Revision: 136365
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Mar 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.0-1mdv2007.1
+ Revision: 144129
- fix build dependencies
- Imported perl-XML-Elemental-2.0-1mdv2007.1 into SVN repository.

* Thu Mar 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.0-1mdv2007.1
- first mdv release

