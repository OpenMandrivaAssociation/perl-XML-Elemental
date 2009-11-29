%define upstream_name    XML-Elemental
%define upstream_version 2.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Simplistic and perlish handling of XML data
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
Buildrequires:  perl(Class::Accessor)
Buildrequires:  perl(XML::SAX)

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/XML
%{_mandir}/man3*/*
