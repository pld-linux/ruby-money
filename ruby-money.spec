Summary:	Library aiding in handling of money
Summary(pl.UTF-8):	Biblioteka języka Ruby pomocna w obsłudze pieniędzy
Name:		ruby-money
Version:	1.7.1
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.vm.bytemark.co.uk/gems/money-%{version}.gem
# Source0-md5:	b42bbaf9bed7ef7ffe1ed792a2611921
URL:		http://money.rubyforge.org/
BuildRequires:	ruby-rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb >= 3.4.1
Requires:	ruby-builder
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library aiding in handling of money.

%description -l pl.UTF-8
Biblioteka języka Ruby pomocna w obsłudze pieniędzy.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/money*
%{ruby_rubylibdir}/bank
%{ruby_rubylibdir}/support
%{ruby_ridir}/Money
%{ruby_ridir}/*Bank
