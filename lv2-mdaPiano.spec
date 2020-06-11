Name:           lv2-mdaPiano
Version:        0.0.2
Release:        1%{?dist}
Summary:        A port of the MDA Piano VST plugin to LV2

License:        GPLv3+
URL:            https://elephly.net/lv2/mdapiano
Source0:        https://git.elephly.net/software/lv2-mdametapiano.git/archive/%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  lv2-devel
BuildRequires:  lv2-c++-tools-static
BuildRequires:  /usr/bin/ttl2c
BuildRequires:  lvtk-devel < 2

%description
A port of the popular MDA Piano VST plugin to LV2.

%prep
%autosetup -n lv2-mdametapiano-%{version}-1a272c3

%build
%make_build TYPE=mdaPiano

%install
rm -rf $RPM_BUILD_ROOT
%make_install TYPE=mdaPiano INSTALL_DIR=%{buildroot}%{_libdir}/lv2

%files
%license LICENSE
%doc README.md
%{_libdir}/lv2/lv2-mdaPiano.lv2

%changelog
* Thu Jun 11 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.0.2-1
- Initial build
