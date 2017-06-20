%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global service kuryr
%global plugin kuryr-tempest-plugin
%global module kuryr_tempest_plugin

Name:       python-%{service}-tests-tempest
Version:    XXX
Release:    XXX
Summary:    Tempest Integration of Kuryr and Kuryr-Kubernetes
License:    ASL 2.0
URL:        https://git.openstack.org/cgit/openstack/%{plugin}/

Source0:    http://tarballs.openstack.org/%{plugin}/%{plugin}-%{upstream_version}.tar.gz

BuildArch:  noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  git
BuildRequires:  openstack-macros

Requires:   python-pbr
Requires:   python-setuptools
Requires:   python-six  >= 1.9.0
Requires:   python-tempest >= 1:12.2.0
Requires:   python-testrepository
Requires:   python-oslotest >= 1.10.0
Requires:   python-os-testr
Requires:   python-testtools
Requires:   python-kubernetes
# NOTE: 2.0.0 is not yet available in RDO repos. will specify version when
# that's done.
# Requires:   python-kubernetes >= 2.0.0
%description
This package contains Tempest tests to cover the kuryr-kubernetes project.
Additionally it provides a plugin to automatically load these tests into Tempest.

%prep
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup

rm -rf %{module}.egg-info

%build
%py2_build

%install
%py2_install

%files
%license LICENSE
%doc CONTRIBUTING.rst README.rst
%{python2_sitelib}/%{module}
%{python2_sitelib}/%{module}-*-py?.?.egg-info

%changelog
