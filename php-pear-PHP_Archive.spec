%define		_status		alpha
%define		_pearname PHP_Archive
Summary:	%{_pearname} - create and use PHP Archive files
Summary(pl.UTF-8):	%{_pearname} - tworzenie i wykorzystanie archiwów PHP
Name:		php-pear-%{_pearname}
Version:	0.12.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	dd0c56bfb0fc84f3c6c8ff0257939d8f
URL:		http://pear.php.net/package/PHP_Archive/
BuildRequires:	php-pear-PEAR >= 1:1.4.3
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 5.1.0
Requires:	php-pear >= 4:1.0-7
Requires:	php-pear-Archive_Tar >= 1.3.1
Requires:	php-pear-PEAR-core >= 1:1.4.3
Obsoletes:	php-pear-PHP_Archive-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP_Archive allows you to create a single .phar file containing an
entire application.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
PHP_Archive pozwala na tworzenie pojedynczych plików .phar
zawierajacych całe aplikacje.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/PHP/*.php
%{php_pear_dir}/PHP/Archive
%{php_pear_dir}/data/%{_pearname}
