%define git 1
%define gitdate %(date +%Y%m%d)

%define major 0
%define libname %mklibname  %{major}
%define oname wacomtablet

Name:           kcm-wacomtablet
Group:          Graphical desktop/KDE
Summary:        Kontrol module for Wacom Graphictablets
Version:        1.3.3
Release:        %mkrel -c git%{gitdate} 1
License:        GPL
URL:            https://projects.kde.org/projects/extragear/base/wacomtablet
# wget -c http://anongit.kde.org/wacomtablet/wacomtablet-latest.tar.gz
Source0:        %{oname}%{?!git:-%{version}}.tar.xz
BuildRequires:  kdelibs4-devel
BuildRequires:  x11-driver-input-wacom-devel >= 0.10.11

%description
This module implements a GUI for the Wacom Linux Drivers and extends it
with profile support to handle different button/pen layouts per profile.

%files
%doc README
%{_datadir}/dbus-1/interfaces/org.kde.Wacom*.xml
%{_kde_docdir}/HTML/en/kcontrol/wacomtablet/
%{_kde_libdir}/kde4/kcm_wacomtablet.so
%{_kde_libdir}/kde4/kded_wacomtablet.so
%{_kde_libdir}/kde4/plasma_applet_wacomtabletsettings.so
%{_kde_appsdir}/wacomtablet/
%{_kde_services}/kcm_wacomtablet.desktop
%{_kde_services}/kded/wacomtablet.desktop
%{_kde_services}/plasma-applet-wacomtabletsettings.desktop

#--------------------------------------------------------------------
%prep
%setup -q%{?git:n %{oname}}

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build


