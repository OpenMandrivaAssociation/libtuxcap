%define		major 4.0
%define		libname		%mklibname tuxcap %{major}
%define		develname	%mklibname tuxcap -d
Name:		libtuxcap
Version:	1.4.0
Release:	1
License:	BSD
Summary:	Port of the PopCap Games Framework used for 2D game development
Group:		System/Libraries
Url:		http://sourceforge.net/projects/tuxcap/
Source:		%{name}-%{version}.tar.gz
Patch0:		libtuxcap-1.4.0-includes.patch
Patch1:		libtuxcap-1.4.0-libdir.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(gl)
BuildRequires:	imagemagick-devel
BuildRequires:  imagemagick
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	X11-devel
BuildRequires:	pkgconfig(python)

%description
The TuxCap Games Framework is a GNU/Linux and Mac OSX port of the PopCap
Games Framework used for 2D game development. It comes with PyCap Python
bindings, a fast 2D physics engine, a particle engine, widgets and many
documented examples.

%package -n %{libname}
Group:		System/Libraries
Summary:	Port of the PopCap Games Framework used for 2D game development

%description -n %{libname}
The TuxCap Games Framework is a GNU/Linux and Mac OSX port of the PopCap
Games Framework used for 2D game development. It comes with PyCap Python
bindings, a fast 2D physics engine, a particle engine, widgets and many
documented examples.

%package -n %{develname}
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Summary:	Development headers for %{name}

%description -n %{develname}
Development headers for TuxCap Games Framework

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%__sed -i '/pythondemo1/d' tuxcap/CMakeLists.txt

%build
%cmake
%make

%install

%makeinstall_std -C build

rm -fr %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS CHANGELOG COPYRIGHT README TODO doc/*
%{_includedir}/*
%{_libdir}/*.so

