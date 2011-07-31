%define		status		stable
%define		pearname	Net_DNS2
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - PHP5 Resolver library used to communicate with a DNS server
Name:		php-pear-Net_DNS2
Version:	1.1.4
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	6a73f4bdb9c7ceb0d5bbaa2d5e720648
URL:		http://pear.php.net/package/Net_DNS2/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.593
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides (roughly) the same functionality as Net_DNS, but using PHP5
objects, exceptions for error handling, better sockets support.

This release is (in most cases) 2x - 10x faster than Net_DNS, as well
as includes more RR's (including DNSSEC RR's), and improved sockets
and streams support.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/DNS2.php
%{php_pear_dir}/Net/DNS2
