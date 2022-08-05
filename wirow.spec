%global debug_package %{nil}
%global _prj_name wirow-server

Name:           wirow
Version:        1.0.2
Release:        1%{?dist}
Summary:        A full featured self-hosted video web-conferencing platform

License:        AGPLv3
URL:            https://github.com/wirow-io/wirow-server
Source0:        https://github.com/wirow-io/wirow-server/archive/v%{version}.tar.gz

Requires:       ffmpeg
%if 0%{?el8}
# EL8 ships with gcc-8.5.0
BuildRequires:  gcc-toolset-11
%else
BuildRequires:  gcc > 9
%endif
BuildRequires:  cmake >= 3.18
BuildRequires:  nodejs >= 16
BuildRequires:  autoconf automake git libtool make ninja-build python3-pip yasm

%description
A full featured self-hosted video web-conferencing platform shipped as a single executable.

- Works on Linux and FreeBSD.
- Single executable, no setup is required.
- Let's Encrypt integration - instant SSL certs generation for your web-conferencing host.
- Unlimited meeting rooms and webinars.
- Integrated whiteboard.
- Video calls recording.
- Low memory/CPU consumption due to fast core engine written in C.

%prep
%autosetup -n %{_prj_name}-%{version}

npm install --global yarn

%build
%if 0%{?el8}
    # better than 'scl enable' because it's not spawning a new shell
    source /opt/rh/gcc-toolset-11/enable
%endif

cmake ..    -G Ninja \
            -D CMAKE_BUILD_TYPE=RelWithDebInfo \
            -D IW_EXEC=ON \
            -D BUILD_TESTS=ON
ninja

%install
# bin
mkdir -p %{buildroot}%{_bindir}
install -Dpm 755 -t %{buildroot}%{_bindir} build/src/%{name}

# configs
install -Dpm 644 docs/%{name}-configuration.ini %{buildroot}%{_sysconfdir}/%{name}/config.ini

%files
%license LICENSE
%doc Changelog README.md docs/%{name}.adoc docs/%{name}.pdf
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*

%changelog
* Fri Aug 05 2022 cyqsimon - 1.0.2-1
- Release 1.0.2