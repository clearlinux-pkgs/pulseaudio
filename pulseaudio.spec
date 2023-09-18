#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
#
Name     : pulseaudio
Version  : 14.2
Release  : 58
URL      : https://freedesktop.org/software/pulseaudio/releases/pulseaudio-14.2.tar.xz
Source0  : https://freedesktop.org/software/pulseaudio/releases/pulseaudio-14.2.tar.xz
Summary  : PulseAudio Simplified Synchronous Client Interface
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: pulseaudio-bin = %{version}-%{release}
Requires: pulseaudio-data = %{version}-%{release}
Requires: pulseaudio-lib = %{version}-%{release}
Requires: pulseaudio-license = %{version}-%{release}
Requires: pulseaudio-locales = %{version}-%{release}
Requires: pulseaudio-man = %{version}-%{release}
Requires: rtkit
BuildRequires : bluez-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gdbm-dev32
BuildRequires : gettext
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : intltool-dev
BuildRequires : libX11-dev
BuildRequires : libX11-dev32
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libcap-ng-dev32
BuildRequires : libsamplerate-dev
BuildRequires : libtool-dev32
BuildRequires : perl(XML::Parser)
BuildRequires : pkg-config
BuildRequires : pkgconfig(32alsa)
BuildRequires : pkgconfig(32check)
BuildRequires : pkgconfig(32dbus-1)
BuildRequires : pkgconfig(32gio-2.0)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32gobject-2.0)
BuildRequires : pkgconfig(32ice)
BuildRequires : pkgconfig(32libsystemd)
BuildRequires : pkgconfig(32libudev)
BuildRequires : pkgconfig(32openssl)
BuildRequires : pkgconfig(32orc-0.4)
BuildRequires : pkgconfig(32sbc)
BuildRequires : pkgconfig(32sm)
BuildRequires : pkgconfig(32sndfile)
BuildRequires : pkgconfig(32x11-xcb)
BuildRequires : pkgconfig(32xcb)
BuildRequires : pkgconfig(32xtst)
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(bluez)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(fftw3f)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-app-1.0)
BuildRequires : pkgconfig(gstreamer-rtp-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(orc-0.4)
BuildRequires : pkgconfig(sbc)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xtst)
BuildRequires : sbc-dev
BuildRequires : speex-dev
BuildRequires : speexdsp-dev
BuildRequires : valgrind-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Support-a-stateless-configuration.patch
Patch2: lessfence.patch
Patch3: memfd.patch

%description
PULSEAUDIO SOUND SERVER
WEB SITE:
http://pulseaudio.org/
GIT:
https://gitlab.freedesktop.org/pulseaudio/pulseaudio.git

%package bin
Summary: bin components for the pulseaudio package.
Group: Binaries
Requires: pulseaudio-data = %{version}-%{release}
Requires: pulseaudio-license = %{version}-%{release}

%description bin
bin components for the pulseaudio package.


%package data
Summary: data components for the pulseaudio package.
Group: Data

%description data
data components for the pulseaudio package.


%package dev
Summary: dev components for the pulseaudio package.
Group: Development
Requires: pulseaudio-lib = %{version}-%{release}
Requires: pulseaudio-bin = %{version}-%{release}
Requires: pulseaudio-data = %{version}-%{release}
Provides: pulseaudio-devel = %{version}-%{release}
Requires: pulseaudio = %{version}-%{release}

%description dev
dev components for the pulseaudio package.


%package dev32
Summary: dev32 components for the pulseaudio package.
Group: Default
Requires: pulseaudio-lib32 = %{version}-%{release}
Requires: pulseaudio-bin = %{version}-%{release}
Requires: pulseaudio-data = %{version}-%{release}
Requires: pulseaudio-dev = %{version}-%{release}

%description dev32
dev32 components for the pulseaudio package.


%package lib
Summary: lib components for the pulseaudio package.
Group: Libraries
Requires: pulseaudio-data = %{version}-%{release}
Requires: pulseaudio-license = %{version}-%{release}

%description lib
lib components for the pulseaudio package.


%package lib32
Summary: lib32 components for the pulseaudio package.
Group: Default
Requires: pulseaudio-data = %{version}-%{release}
Requires: pulseaudio-license = %{version}-%{release}

%description lib32
lib32 components for the pulseaudio package.


%package license
Summary: license components for the pulseaudio package.
Group: Default

%description license
license components for the pulseaudio package.


%package locales
Summary: locales components for the pulseaudio package.
Group: Default

%description locales
locales components for the pulseaudio package.


%package man
Summary: man components for the pulseaudio package.
Group: Default

%description man
man components for the pulseaudio package.


%prep
%setup -q -n pulseaudio-14.2
cd %{_builddir}/pulseaudio-14.2
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
pushd ..
cp -a pulseaudio-14.2 build32
popd
pushd ..
cp -a pulseaudio-14.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695079103
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%autogen --disable-static --with-udev-rules-dir=/usr/lib/udev/rules.d \
--enable-orc \
--with-speex \
--enable-bluez5 \
--disable-bluez4 \
--disable-bluez5-ofono-headset
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%autogen --disable-static --with-udev-rules-dir=/usr/lib/udev/rules.d \
--enable-orc \
--with-speex \
--enable-bluez5 \
--disable-bluez4 \
--disable-bluez5-ofono-headset --without-fftw \
--disable-gtk3 \
--without-speex \
--without-caps \
--disable-bluez5 \
--disable-bluez4 --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%autogen --disable-static --with-udev-rules-dir=/usr/lib/udev/rules.d \
--enable-orc \
--with-speex \
--enable-bluez5 \
--disable-bluez4 \
--disable-bluez5-ofono-headset
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1695079103
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pulseaudio
cp %{_builddir}/pulseaudio-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pulseaudio/146b824cf04e121da67545caff4ede65bbbb3936 || :
cp %{_builddir}/pulseaudio-%{version}/src/pulsecore/filter/LICENSE.WEBKIT %{buildroot}/usr/share/package-licenses/pulseaudio/24b8a642abc0e34765a795aef5ce10475e17574b || :
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang pulseaudio
## Remove excluded files
rm -f %{buildroot}*/usr/bin/esdcompat
rm -f %{buildroot}*/usr/bin/pa-info
rm -f %{buildroot}*/usr/bin/pacmd
rm -f %{buildroot}*/usr/bin/pasuspender
rm -f %{buildroot}*/usr/bin/pax11publish
rm -f %{buildroot}*/usr/bin/pulseaudio
rm -f %{buildroot}*/usr/bin/qpaeq
rm -f %{buildroot}*/usr/bin/start-pulseaudio-x11
rm -f %{buildroot}*/usr/lib/systemd/user/pulseaudio.service
rm -f %{buildroot}*/usr/lib/systemd/user/pulseaudio.socket
rm -f %{buildroot}*/usr/lib/udev/rules.d/90-pulseaudio.rules
rm -f %{buildroot}*/usr/libexec/pulse/gsettings-helper
rm -f %{buildroot}*/usr/share/GConf/gsettings/pulseaudio.convert
rm -f %{buildroot}*/usr/share/bash-completion/completions/pacmd
rm -f %{buildroot}*/usr/share/bash-completion/completions/pasuspender
rm -f %{buildroot}*/usr/share/bash-completion/completions/pulseaudio
rm -f %{buildroot}*/usr/share/dbus-1/system.d/pulseaudio-system.conf
rm -f %{buildroot}*/usr/share/glib-2.0/schemas/org.freedesktop.pulseaudio.gschema.xml
rm -f %{buildroot}*/usr/share/man/man1/esdcompat.1
rm -f %{buildroot}*/usr/share/man/man1/pacmd.1
rm -f %{buildroot}*/usr/share/man/man1/pasuspender.1
rm -f %{buildroot}*/usr/share/man/man1/pax11publish.1
rm -f %{buildroot}*/usr/share/man/man1/pulseaudio.1
rm -f %{buildroot}*/usr/share/man/man1/start-pulseaudio-x11.1
rm -f %{buildroot}*/usr/share/man/man5/default.pa.5
rm -f %{buildroot}*/usr/share/man/man5/pulse-cli-syntax.5
rm -f %{buildroot}*/usr/share/man/man5/pulse-daemon.conf.5
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-aux.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-dock-mic.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-fm.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-front-mic.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-headphone-mic.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-headset-mic.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-internal-mic-always.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-internal-mic.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-linein.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-mic-line.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-mic.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-mic.conf.common
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-rear-mic.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-tvtuner.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input-video.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-input.conf.common
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-output-headphones-2.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-output-headphones.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-output-lineout.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-output-mono.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-output-speaker-always.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-output-speaker.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-output.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/analog-output.conf.common
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-0.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-1.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-2.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-3.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-4.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-5.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-6.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-7.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/iec958-stereo-input.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/iec958-stereo-output.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/steelseries-arctis-output-chat-common.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/steelseries-arctis-output-game-common.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/usb-gaming-headset-input.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/usb-gaming-headset-output-mono.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/paths/usb-gaming-headset-output-stereo.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/audigy.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/cmedia-high-speed-true-hdaudio.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/default.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/dell-dock-tb16-usb-audio.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/force-speaker-and-int-mic.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/force-speaker.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/kinect-audio.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/maudio-fasttrack-pro.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/native-instruments-audio4dj.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/native-instruments-audio8dj.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/native-instruments-korecontroller.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/native-instruments-traktor-audio10.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/native-instruments-traktor-audio2.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/native-instruments-traktor-audio6.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/native-instruments-traktorkontrol-s4.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/sb-omni-surround-5.1.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/steelseries-arctis-common-usb-audio.conf
rm -f %{buildroot}*/usr/share/pulseaudio/alsa-mixer/profile-sets/usb-gaming-headset.conf
rm -f %{buildroot}*/usr/share/pulseaudio/daemon.conf
rm -f %{buildroot}*/usr/share/pulseaudio/default.pa
rm -f %{buildroot}*/usr/share/pulseaudio/system.pa
rm -f %{buildroot}*/usr/share/xdg/autostart/pulseaudio.desktop
rm -f %{buildroot}*/usr/share/xdg/autostart/pulseaudio.desktop
rm -f %{buildroot}*/usr/share/zsh/site-functions/_pulseaudio
## install_append content
rm -rf %{buildroot}*/%{_datadir}/vala
rm -fr %{buildroot}*//usr/lib32/pulse-*
rm -fr %{buildroot}*//usr/lib64/pulse-*
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/pacat
/V3/usr/bin/pactl
/usr/bin/pacat
/usr/bin/pactl
/usr/bin/padsp
/usr/bin/pamon
/usr/bin/paplay
/usr/bin/parec
/usr/bin/parecord

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/pacat
/usr/share/bash-completion/completions/pactl
/usr/share/bash-completion/completions/padsp
/usr/share/bash-completion/completions/paplay
/usr/share/bash-completion/completions/parec
/usr/share/bash-completion/completions/parecord
/usr/share/pulseaudio/client.conf

%files dev
%defattr(-,root,root,-)
/usr/include/pulse/cdecl.h
/usr/include/pulse/channelmap.h
/usr/include/pulse/context.h
/usr/include/pulse/def.h
/usr/include/pulse/direction.h
/usr/include/pulse/error.h
/usr/include/pulse/ext-device-manager.h
/usr/include/pulse/ext-device-restore.h
/usr/include/pulse/ext-stream-restore.h
/usr/include/pulse/format.h
/usr/include/pulse/gccmacro.h
/usr/include/pulse/glib-mainloop.h
/usr/include/pulse/introspect.h
/usr/include/pulse/mainloop-api.h
/usr/include/pulse/mainloop-signal.h
/usr/include/pulse/mainloop.h
/usr/include/pulse/operation.h
/usr/include/pulse/proplist.h
/usr/include/pulse/pulseaudio.h
/usr/include/pulse/rtclock.h
/usr/include/pulse/sample.h
/usr/include/pulse/scache.h
/usr/include/pulse/simple.h
/usr/include/pulse/stream.h
/usr/include/pulse/subscribe.h
/usr/include/pulse/thread-mainloop.h
/usr/include/pulse/timeval.h
/usr/include/pulse/utf8.h
/usr/include/pulse/util.h
/usr/include/pulse/version.h
/usr/include/pulse/volume.h
/usr/include/pulse/xmalloc.h
/usr/lib64/cmake/PulseAudio/PulseAudioConfig.cmake
/usr/lib64/cmake/PulseAudio/PulseAudioConfigVersion.cmake
/usr/lib64/libpulse-mainloop-glib.so
/usr/lib64/libpulse-simple.so
/usr/lib64/libpulse.so
/usr/lib64/pkgconfig/libpulse-mainloop-glib.pc
/usr/lib64/pkgconfig/libpulse-simple.pc
/usr/lib64/pkgconfig/libpulse.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/cmake/PulseAudio/PulseAudioConfig.cmake
/usr/lib32/cmake/PulseAudio/PulseAudioConfigVersion.cmake
/usr/lib32/libpulse-mainloop-glib.so
/usr/lib32/libpulse-simple.so
/usr/lib32/libpulse.so
/usr/lib32/pkgconfig/32libpulse-mainloop-glib.pc
/usr/lib32/pkgconfig/32libpulse-simple.pc
/usr/lib32/pkgconfig/32libpulse.pc
/usr/lib32/pkgconfig/libpulse-mainloop-glib.pc
/usr/lib32/pkgconfig/libpulse-simple.pc
/usr/lib32/pkgconfig/libpulse.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libpulse-mainloop-glib.so.0.0.6
/V3/usr/lib64/libpulse-simple.so.0.1.1
/V3/usr/lib64/libpulse.so.0.23.0
/V3/usr/lib64/pulseaudio/libpulsecommon-14.2.so
/V3/usr/lib64/pulseaudio/libpulsecore-14.2.so
/V3/usr/lib64/pulseaudio/libpulsedsp.so
/usr/lib64/libpulse-mainloop-glib.so.0
/usr/lib64/libpulse-mainloop-glib.so.0.0.6
/usr/lib64/libpulse-simple.so.0
/usr/lib64/libpulse-simple.so.0.1.1
/usr/lib64/libpulse.so.0
/usr/lib64/libpulse.so.0.23.0
/usr/lib64/pulseaudio/libpulsecommon-14.2.so
/usr/lib64/pulseaudio/libpulsecore-14.2.so
/usr/lib64/pulseaudio/libpulsedsp.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpulse-mainloop-glib.so.0
/usr/lib32/libpulse-mainloop-glib.so.0.0.6
/usr/lib32/libpulse-simple.so.0
/usr/lib32/libpulse-simple.so.0.1.1
/usr/lib32/libpulse.so.0
/usr/lib32/libpulse.so.0.23.0
/usr/lib32/pulseaudio/libpulsecommon-14.2.so
/usr/lib32/pulseaudio/libpulsecore-14.2.so
/usr/lib32/pulseaudio/libpulsedsp.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pulseaudio/146b824cf04e121da67545caff4ede65bbbb3936
/usr/share/package-licenses/pulseaudio/24b8a642abc0e34765a795aef5ce10475e17574b

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pacat.1
/usr/share/man/man1/pactl.1
/usr/share/man/man1/padsp.1
/usr/share/man/man1/pamon.1
/usr/share/man/man1/paplay.1
/usr/share/man/man1/parec.1
/usr/share/man/man1/parecord.1
/usr/share/man/man5/pulse-client.conf.5

%files locales -f pulseaudio.lang
%defattr(-,root,root,-)

