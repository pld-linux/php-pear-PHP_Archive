%include	/usr/lib/rpm/macros.php
%define		_class		PHP
%define		_subclass	Archive
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - create and use PHP Archive files
Summary(pl.UTF-8):	%{_pearname} - tworzenie i wykorzystanie archiwów PHP
Name:		php-pear-%{_pearname}
Version:	0.11.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	be6dfa685d559ed445b93e4706d4ca2a
URL:		http://pear.php.net/package/PHP_Archive/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 4:5.1.0
Requires:	php-pear >= 4:1.0-7
Requires:	php-pear-Archive_Tar >= 1.3.1
Requires:	php-pear-PEAR-core >= 1:1.3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# catches patters from strings
%define		_noautoreq	'pear(phar://.*)'

%description
PHP_Archive allows you to create a single .phar file containing an
entire application.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PHP_Archive pozwala na tworzenie pojedynczych plików .phar
zawierajacych całe aplikacje.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/data/%{_pearname}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
