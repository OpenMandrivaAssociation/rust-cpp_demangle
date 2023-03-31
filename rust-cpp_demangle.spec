# Generated by rust2rpm 10
%bcond_with check
%global debug_package %{nil}

%global __cargo_is_bin() false

%global crate cpp_demangle

Name:           rust-%{crate}
Version:        0.3.3
Release:        2
Summary:        Crate for demangling C++ symbols

# Upstream license specification: Apache-2.0/MIT
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/cpp_demangle
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
A crate for demangling C++ symbols.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+afl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+afl-devel %{_description}

This package contains library source intended for building other packages
which use "afl" feature of "%{crate}" crate.

%files       -n %{name}+afl-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+cppfilt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cppfilt-devel %{_description}

This package contains library source intended for building other packages
which use "cppfilt" feature of "%{crate}" crate.

%files       -n %{name}+cppfilt-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+fuzz-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fuzz-devel %{_description}

This package contains library source intended for building other packages
which use "fuzz" feature of "%{crate}" crate.

%files       -n %{name}+fuzz-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+logging-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+logging-devel %{_description}

This package contains library source intended for building other packages
which use "logging" feature of "%{crate}" crate.

%files       -n %{name}+logging-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+run_libiberty_tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+run_libiberty_tests-devel %{_description}

This package contains library source intended for building other packages
which use "run_libiberty_tests" feature of "%{crate}" crate.

%files       -n %{name}+run_libiberty_tests-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Josh Stone <jistone@redhat.com> - 0.2.14-1
- Update to 0.2.14

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 17:06:18 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.12-4
- Update glob to 0.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.12-2
- Adapt to new packaging

* Tue Sep 11 2018 Josh Stone <jistone@redhat.com> - 0.2.12-1
- Update to 0.2.12

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.11-1
- Update to 0.2.11

* Thu Aug 09 2018 Josh Stone <jistone@redhat.com> - 0.2.10-1
- Update to 0.2.10

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Josh Stone <jistone@redhat.com> - 0.2.9-1
- Update to 0.2.9

* Sat May 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.8-1
- Update to 0.2.8

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.7-2
- Rebuild for rust-packaging v5

* Fri Dec 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.7-1
- Initial package
