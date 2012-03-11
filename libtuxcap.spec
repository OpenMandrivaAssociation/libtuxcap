%define		major 4

%define		libname		%mklibname tuxcap %{major}
%define		develname	%mklibname tuxcap -d

Name:		libtuxcap
Version:	1.4.0
Release:	%mkrel 1
License:	BSD
Summary:	Port of the PopCap Games Framework used for 2D game development
Group:		System/Libraries
Url:		http://sourceforge.net/projects/tuxcap/
Source:		%{name}-%{version}.tar.gz
Patch0:		libtuxcap-1.4.0-includes.patch
BuildRequires:	cmake
BuildRequires:	mesagl-devel
BuildRequires:	imagemagick-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	X11-devel
BuildRequires:	python-devel

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
Requires:	%{libname} = %{EVRD}
Summary:	Development headers for %{name}

%description -n %{develname}
Development headers for TuxCap Games Framework

%prep
%setup -q
%patch0 -p1

%__sed -i '/pythondemo1/d' tuxcap/CMakeLists.txt

%build
%cmake
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%__rm -f %{buildroot}%{_libdir}/*.a

%clean
%__rm -rf %{buildroot}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS CHANGELOG COPYRIGHT README TODO doc/*
%{_includedir}/*
%{_libdir}/*.so

