%global git 5a6c336982e5956c6dce5d3d51d057ac034ce7ca
Summary: A desktop recorder
Name: byzanz
Version: 0.3
Release: 0.25
License: GPLv3+
URL: http://git.gnome.org/browse/byzanz/
#Source0: http://download.gnome.org/sources/%{name}/0.2/%{name}-%{version}.tar.bz2
# git archive --format=tar --prefix=byzanz-%{git}/ %{git} | xz > byzanz-%{git}
Source0: byzanz-%{git}.tar.xz
Patch0: byzanz-gcc11.patch

BuildRequires: cairo-devel >= 1.8.10 gtk3-devel libXdamage-devel >= 1.0 glib2-devel >= 2.6.0
BuildRequires: gnome-common gstreamer1-devel gstreamer1-plugins-base-devel gettext-devel
BuildRequires: intltool perl(XML::Parser) libtool autoconf automake

Requires(pre): GConf2
Requires(post): GConf2
Requires(preun): GConf2

%description
Byzanz is a desktop recorder striving for ease of use. It can record to 
GIF images, Ogg Theora video - optionally with sound - and other formats.
A command-line recording tool is included.

%prep
%setup -q -n byzanz-%{git}
%patch0 -p1

%build
./autogen.sh
CFLAGS="%optflags -Wno-deprecated-declarations"
%ifarch armv7l armv7hl armv7hnl
# http://rwmj.wordpress.com/2014/01/06/alignment-errors-on-fedora-arm/
CFLAGS="$CFLAGS -Wno-cast-align"
%endif
%configure
make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make DESTDIR=%{buildroot} install
%find_lang byzanz

%files -f byzanz.lang
%doc AUTHORS ChangeLog COPYING NEWS
%{_bindir}/byzanz-playback
%{_bindir}/byzanz-record
%{_datadir}/icons/hicolor/*/apps/byzanz-record-area.*
%{_datadir}/icons/hicolor/*/apps/byzanz-record-desktop.*
%{_datadir}/icons/hicolor/*/apps/byzanz-record-window.*
%{_mandir}/man1/byzanz.1*
%{_mandir}/man1/byzanz-playback.1*
%{_mandir}/man1/byzanz-record.1*

%changelog
* Tue Jun 13 2023 EastDong <xudong23@iscas.ac.cn> - 0.3-0.25
- Fix '__atomic_load' discards 'volatile' qualifier

* Fri May 07 2021 weidong <weidong@uniontech.com> - 0.3-0.24
- Initial package.

