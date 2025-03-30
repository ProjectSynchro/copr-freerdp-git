Name:		SDL3_ttf
Version:	3.2.0
Release:	1%{?dist}
Summary:	TrueType font rendering library for SDL3
License:	Zlib
URL:		https://github.com/libsdl-org/SDL_ttf
Source0:	https://github.com/libsdl-org/SDL_ttf/releases/download/release-%{version}/SDL3_ttf-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:	SDL3-devel
BuildRequires:  libGL-devel
BuildRequires:	freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:	zlib-devel

%description
This library allows you to use TrueType fonts to render text in SDL3
applications.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	SDL3-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup
rm -rf external
# Fix end-of-line encoding
sed -i 's/\r//' README.txt CHANGES.txt LICENSE.txt

%build
%cmake -DSDLTTF_HARFBUZZ=true
%cmake_build

%install
%cmake_install
find %{buildroot} -type f -name '*.la' -delete -print

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc README.txt CHANGES.txt
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/SDL2/*
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/SDL3_ttf/

%changelog
* Sun Mar 30 2025 Jack Greiner <jack@emoss.org> - 3.2.0-1
- initial package
