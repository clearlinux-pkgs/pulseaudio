#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pulseaudio
Version  : 11.1
Release  : 20
URL      : https://freedesktop.org/software/pulseaudio/releases/pulseaudio-11.1.tar.xz
Source0  : https://freedesktop.org/software/pulseaudio/releases/pulseaudio-11.1.tar.xz
Summary  : PulseAudio GLib 2.0 Main Loop Wrapper
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: pulseaudio-bin
Requires: pulseaudio-config
Requires: pulseaudio-lib
Requires: pulseaudio-data
Requires: pulseaudio-locales
Requires: pulseaudio-doc
BuildRequires : bluez-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gdbm-dev32
BuildRequires : gettext
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : libX11-dev
BuildRequires : libX11-dev32
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libcap-ng-dev32
BuildRequires : libsamplerate-dev
BuildRequires : libtool-dev32
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(32alsa)
BuildRequires : pkgconfig(32check)
BuildRequires : pkgconfig(32dbus-1)
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
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
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
Patch1: 0001-Support-a-stateless-configuration.patch
Patch2: lessfence.patch

%description
PULSEAUDIO SOUND SERVER
WEB SITE:
http://pulseaudio.org/
GIT:
git://anongit.freedesktop.org/pulseaudio/pulseaudio

%package bin
Summary: bin components for the pulseaudio package.
Group: Binaries
Requires: pulseaudio-data
Requires: pulseaudio-config

%description bin
bin components for the pulseaudio package.


%package config
Summary: config components for the pulseaudio package.
Group: Default

%description config
config components for the pulseaudio package.


%package data
Summary: data components for the pulseaudio package.
Group: Data

%description data
data components for the pulseaudio package.


%package dev
Summary: dev components for the pulseaudio package.
Group: Development
Requires: pulseaudio-lib
Requires: pulseaudio-bin
Requires: pulseaudio-data
Provides: pulseaudio-devel

%description dev
dev components for the pulseaudio package.


%package dev32
Summary: dev32 components for the pulseaudio package.
Group: Default
Requires: pulseaudio-lib32
Requires: pulseaudio-bin
Requires: pulseaudio-data
Requires: pulseaudio-dev

%description dev32
dev32 components for the pulseaudio package.


%package doc
Summary: doc components for the pulseaudio package.
Group: Documentation

%description doc
doc components for the pulseaudio package.


%package lib
Summary: lib components for the pulseaudio package.
Group: Libraries
Requires: pulseaudio-data
Requires: pulseaudio-config

%description lib
lib components for the pulseaudio package.


%package lib32
Summary: lib32 components for the pulseaudio package.
Group: Default
Requires: pulseaudio-data
Requires: pulseaudio-config

%description lib32
lib32 components for the pulseaudio package.


%package locales
Summary: locales components for the pulseaudio package.
Group: Default

%description locales
locales components for the pulseaudio package.


%prep
%setup -q -n pulseaudio-11.1
%patch1 -p1
%patch2 -p1
pushd ..
cp -a pulseaudio-11.1 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505756826
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%autogen --disable-static --with-udev-rules-dir=/usr/lib/udev/rules.d --enable-orc --with-speex --enable-bluez5
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%autogen --disable-static --with-udev-rules-dir=/usr/lib/udev/rules.d --enable-orc --with-speex --enable-bluez5 --without-fftw \
--disable-gtk3 \
--without-speex \
--without-caps \
--disable-bluez5 \
--disable-bluez4 --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1505756826
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang pulseaudio
## make_install_append content
rm -rf %{buildroot}%{_datadir}/vala
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib32/cmake/PulseAudio/PulseAudioConfig.cmake
/usr/lib32/cmake/PulseAudio/PulseAudioConfigVersion.cmake
/usr/lib64/cmake/PulseAudio/PulseAudioConfig.cmake
/usr/lib64/cmake/PulseAudio/PulseAudioConfigVersion.cmake

%files bin
%defattr(-,root,root,-)
/usr/bin/esdcompat
/usr/bin/pacat
/usr/bin/pacmd
/usr/bin/pactl
/usr/bin/padsp
/usr/bin/pamon
/usr/bin/paplay
/usr/bin/parec
/usr/bin/parecord
/usr/bin/pasuspender
/usr/bin/pax11publish
/usr/bin/pulseaudio
/usr/bin/qpaeq
/usr/bin/start-pulseaudio-x11

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/user/pulseaudio.service
/usr/lib/systemd/user/pulseaudio.socket
/usr/lib/udev/rules.d/90-pulseaudio.rules

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/pacat
/usr/share/bash-completion/completions/pacmd
/usr/share/bash-completion/completions/pactl
/usr/share/bash-completion/completions/padsp
/usr/share/bash-completion/completions/paplay
/usr/share/bash-completion/completions/parec
/usr/share/bash-completion/completions/parecord
/usr/share/bash-completion/completions/pasuspender
/usr/share/bash-completion/completions/pulseaudio
/usr/share/dbus-1/system.d/pulseaudio-system.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-aux.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-dock-mic.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-fm.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-front-mic.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-headphone-mic.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-headset-mic.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-internal-mic-always.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-internal-mic.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-linein.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-mic-line.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-mic.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-mic.conf.common
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-rear-mic.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-tvtuner.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input-video.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-input.conf.common
/usr/share/pulseaudio/alsa-mixer/paths/analog-output-headphones-2.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-output-headphones.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-output-lineout.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-output-mono.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-output-speaker-always.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-output-speaker.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-output.conf
/usr/share/pulseaudio/alsa-mixer/paths/analog-output.conf.common
/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-0.conf
/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-1.conf
/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-2.conf
/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-3.conf
/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-4.conf
/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-5.conf
/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-6.conf
/usr/share/pulseaudio/alsa-mixer/paths/hdmi-output-7.conf
/usr/share/pulseaudio/alsa-mixer/paths/iec958-stereo-output.conf
/usr/share/pulseaudio/alsa-mixer/profile-sets/default.conf
/usr/share/pulseaudio/alsa-mixer/profile-sets/force-speaker-and-int-mic.conf
/usr/share/pulseaudio/alsa-mixer/profile-sets/force-speaker.conf
/usr/share/pulseaudio/alsa-mixer/profile-sets/kinect-audio.conf
/usr/share/pulseaudio/alsa-mixer/profile-sets/maudio-fasttrack-pro.conf
/usr/share/pulseaudio/alsa-mixer/profile-sets/native-instruments-audio4dj.conf
/usr/share/pulseaudio/alsa-mixer/profile-sets/native-instruments-audio8dj.conf
/usr/share/pulseaudio/alsa-mixer/profile-sets/native-instruments-korecontroller.conf
/usr/share/pulseaudio/alsa-mixer/profile-sets/native-instruments-traktor-audio10.conf
/usr/share/pulseaudio/alsa-mixer/profile-sets/native-instruments-traktor-audio2.conf
/usr/share/pulseaudio/alsa-mixer/profile-sets/native-instruments-traktor-audio6.conf
/usr/share/pulseaudio/alsa-mixer/profile-sets/native-instruments-traktorkontrol-s4.conf
/usr/share/pulseaudio/alsa-mixer/profile-sets/sb-omni-surround-5.1.conf
/usr/share/pulseaudio/client.conf
/usr/share/pulseaudio/daemon.conf
/usr/share/pulseaudio/default.pa
/usr/share/pulseaudio/system.pa
/usr/share/xdg/autostart/pulseaudio.desktop
/usr/share/zsh/site-functions/_pulseaudio

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
/usr/lib64/libpulse-mainloop-glib.so
/usr/lib64/libpulse-simple.so
/usr/lib64/libpulse.so
/usr/lib64/pkgconfig/libpulse-mainloop-glib.pc
/usr/lib64/pkgconfig/libpulse-simple.pc
/usr/lib64/pkgconfig/libpulse.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libpulse-mainloop-glib.so
/usr/lib32/libpulse-simple.so
/usr/lib32/libpulse.so
/usr/lib32/pkgconfig/32libpulse-mainloop-glib.pc
/usr/lib32/pkgconfig/32libpulse-simple.pc
/usr/lib32/pkgconfig/32libpulse.pc
/usr/lib32/pkgconfig/libpulse-mainloop-glib.pc
/usr/lib32/pkgconfig/libpulse-simple.pc
/usr/lib32/pkgconfig/libpulse.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpulse-mainloop-glib.so.0
/usr/lib64/libpulse-mainloop-glib.so.0.0.5
/usr/lib64/libpulse-simple.so.0
/usr/lib64/libpulse-simple.so.0.1.1
/usr/lib64/libpulse.so.0
/usr/lib64/libpulse.so.0.20.2
/usr/lib64/pulse-11.1/modules/libalsa-util.so
/usr/lib64/pulse-11.1/modules/libbluez4-util.so
/usr/lib64/pulse-11.1/modules/libbluez5-util.so
/usr/lib64/pulse-11.1/modules/libcli.so
/usr/lib64/pulse-11.1/modules/liboss-util.so
/usr/lib64/pulse-11.1/modules/libprotocol-cli.so
/usr/lib64/pulse-11.1/modules/libprotocol-esound.so
/usr/lib64/pulse-11.1/modules/libprotocol-http.so
/usr/lib64/pulse-11.1/modules/libprotocol-native.so
/usr/lib64/pulse-11.1/modules/libprotocol-simple.so
/usr/lib64/pulse-11.1/modules/libraop.so
/usr/lib64/pulse-11.1/modules/librtp.so
/usr/lib64/pulse-11.1/modules/module-allow-passthrough.so
/usr/lib64/pulse-11.1/modules/module-alsa-card.so
/usr/lib64/pulse-11.1/modules/module-alsa-sink.so
/usr/lib64/pulse-11.1/modules/module-alsa-source.so
/usr/lib64/pulse-11.1/modules/module-always-sink.so
/usr/lib64/pulse-11.1/modules/module-augment-properties.so
/usr/lib64/pulse-11.1/modules/module-bluetooth-discover.so
/usr/lib64/pulse-11.1/modules/module-bluetooth-policy.so
/usr/lib64/pulse-11.1/modules/module-bluez4-device.so
/usr/lib64/pulse-11.1/modules/module-bluez4-discover.so
/usr/lib64/pulse-11.1/modules/module-bluez5-device.so
/usr/lib64/pulse-11.1/modules/module-bluez5-discover.so
/usr/lib64/pulse-11.1/modules/module-card-restore.so
/usr/lib64/pulse-11.1/modules/module-cli-protocol-tcp.so
/usr/lib64/pulse-11.1/modules/module-cli-protocol-unix.so
/usr/lib64/pulse-11.1/modules/module-cli.so
/usr/lib64/pulse-11.1/modules/module-combine-sink.so
/usr/lib64/pulse-11.1/modules/module-combine.so
/usr/lib64/pulse-11.1/modules/module-console-kit.so
/usr/lib64/pulse-11.1/modules/module-dbus-protocol.so
/usr/lib64/pulse-11.1/modules/module-default-device-restore.so
/usr/lib64/pulse-11.1/modules/module-detect.so
/usr/lib64/pulse-11.1/modules/module-device-manager.so
/usr/lib64/pulse-11.1/modules/module-device-restore.so
/usr/lib64/pulse-11.1/modules/module-echo-cancel.so
/usr/lib64/pulse-11.1/modules/module-equalizer-sink.so
/usr/lib64/pulse-11.1/modules/module-esound-compat-spawnfd.so
/usr/lib64/pulse-11.1/modules/module-esound-compat-spawnpid.so
/usr/lib64/pulse-11.1/modules/module-esound-protocol-tcp.so
/usr/lib64/pulse-11.1/modules/module-esound-protocol-unix.so
/usr/lib64/pulse-11.1/modules/module-esound-sink.so
/usr/lib64/pulse-11.1/modules/module-filter-apply.so
/usr/lib64/pulse-11.1/modules/module-filter-heuristics.so
/usr/lib64/pulse-11.1/modules/module-hal-detect.so
/usr/lib64/pulse-11.1/modules/module-http-protocol-tcp.so
/usr/lib64/pulse-11.1/modules/module-http-protocol-unix.so
/usr/lib64/pulse-11.1/modules/module-intended-roles.so
/usr/lib64/pulse-11.1/modules/module-ladspa-sink.so
/usr/lib64/pulse-11.1/modules/module-loopback.so
/usr/lib64/pulse-11.1/modules/module-match.so
/usr/lib64/pulse-11.1/modules/module-mmkbd-evdev.so
/usr/lib64/pulse-11.1/modules/module-native-protocol-fd.so
/usr/lib64/pulse-11.1/modules/module-native-protocol-tcp.so
/usr/lib64/pulse-11.1/modules/module-native-protocol-unix.so
/usr/lib64/pulse-11.1/modules/module-null-sink.so
/usr/lib64/pulse-11.1/modules/module-null-source.so
/usr/lib64/pulse-11.1/modules/module-oss.so
/usr/lib64/pulse-11.1/modules/module-pipe-sink.so
/usr/lib64/pulse-11.1/modules/module-pipe-source.so
/usr/lib64/pulse-11.1/modules/module-position-event-sounds.so
/usr/lib64/pulse-11.1/modules/module-raop-sink.so
/usr/lib64/pulse-11.1/modules/module-remap-sink.so
/usr/lib64/pulse-11.1/modules/module-remap-source.so
/usr/lib64/pulse-11.1/modules/module-rescue-streams.so
/usr/lib64/pulse-11.1/modules/module-role-cork.so
/usr/lib64/pulse-11.1/modules/module-role-ducking.so
/usr/lib64/pulse-11.1/modules/module-rtp-recv.so
/usr/lib64/pulse-11.1/modules/module-rtp-send.so
/usr/lib64/pulse-11.1/modules/module-rygel-media-server.so
/usr/lib64/pulse-11.1/modules/module-simple-protocol-tcp.so
/usr/lib64/pulse-11.1/modules/module-simple-protocol-unix.so
/usr/lib64/pulse-11.1/modules/module-sine-source.so
/usr/lib64/pulse-11.1/modules/module-sine.so
/usr/lib64/pulse-11.1/modules/module-stream-restore.so
/usr/lib64/pulse-11.1/modules/module-suspend-on-idle.so
/usr/lib64/pulse-11.1/modules/module-switch-on-connect.so
/usr/lib64/pulse-11.1/modules/module-switch-on-port-available.so
/usr/lib64/pulse-11.1/modules/module-systemd-login.so
/usr/lib64/pulse-11.1/modules/module-tunnel-sink-new.so
/usr/lib64/pulse-11.1/modules/module-tunnel-sink.so
/usr/lib64/pulse-11.1/modules/module-tunnel-source-new.so
/usr/lib64/pulse-11.1/modules/module-tunnel-source.so
/usr/lib64/pulse-11.1/modules/module-udev-detect.so
/usr/lib64/pulse-11.1/modules/module-virtual-sink.so
/usr/lib64/pulse-11.1/modules/module-virtual-source.so
/usr/lib64/pulse-11.1/modules/module-virtual-surround-sink.so
/usr/lib64/pulse-11.1/modules/module-volume-restore.so
/usr/lib64/pulse-11.1/modules/module-x11-bell.so
/usr/lib64/pulse-11.1/modules/module-x11-cork-request.so
/usr/lib64/pulse-11.1/modules/module-x11-publish.so
/usr/lib64/pulse-11.1/modules/module-x11-xsmp.so
/usr/lib64/pulseaudio/libpulsecommon-11.1.so
/usr/lib64/pulseaudio/libpulsecore-11.1.so
/usr/lib64/pulseaudio/libpulsedsp.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpulse-mainloop-glib.so.0
/usr/lib32/libpulse-mainloop-glib.so.0.0.5
/usr/lib32/libpulse-simple.so.0
/usr/lib32/libpulse-simple.so.0.1.1
/usr/lib32/libpulse.so.0
/usr/lib32/libpulse.so.0.20.2
/usr/lib32/pulse-11.1/modules/libalsa-util.so
/usr/lib32/pulse-11.1/modules/libcli.so
/usr/lib32/pulse-11.1/modules/liboss-util.so
/usr/lib32/pulse-11.1/modules/libprotocol-cli.so
/usr/lib32/pulse-11.1/modules/libprotocol-esound.so
/usr/lib32/pulse-11.1/modules/libprotocol-http.so
/usr/lib32/pulse-11.1/modules/libprotocol-native.so
/usr/lib32/pulse-11.1/modules/libprotocol-simple.so
/usr/lib32/pulse-11.1/modules/libraop.so
/usr/lib32/pulse-11.1/modules/librtp.so
/usr/lib32/pulse-11.1/modules/module-allow-passthrough.so
/usr/lib32/pulse-11.1/modules/module-alsa-card.so
/usr/lib32/pulse-11.1/modules/module-alsa-sink.so
/usr/lib32/pulse-11.1/modules/module-alsa-source.so
/usr/lib32/pulse-11.1/modules/module-always-sink.so
/usr/lib32/pulse-11.1/modules/module-augment-properties.so
/usr/lib32/pulse-11.1/modules/module-card-restore.so
/usr/lib32/pulse-11.1/modules/module-cli-protocol-tcp.so
/usr/lib32/pulse-11.1/modules/module-cli-protocol-unix.so
/usr/lib32/pulse-11.1/modules/module-cli.so
/usr/lib32/pulse-11.1/modules/module-combine-sink.so
/usr/lib32/pulse-11.1/modules/module-combine.so
/usr/lib32/pulse-11.1/modules/module-console-kit.so
/usr/lib32/pulse-11.1/modules/module-dbus-protocol.so
/usr/lib32/pulse-11.1/modules/module-default-device-restore.so
/usr/lib32/pulse-11.1/modules/module-detect.so
/usr/lib32/pulse-11.1/modules/module-device-manager.so
/usr/lib32/pulse-11.1/modules/module-device-restore.so
/usr/lib32/pulse-11.1/modules/module-echo-cancel.so
/usr/lib32/pulse-11.1/modules/module-esound-compat-spawnfd.so
/usr/lib32/pulse-11.1/modules/module-esound-compat-spawnpid.so
/usr/lib32/pulse-11.1/modules/module-esound-protocol-tcp.so
/usr/lib32/pulse-11.1/modules/module-esound-protocol-unix.so
/usr/lib32/pulse-11.1/modules/module-esound-sink.so
/usr/lib32/pulse-11.1/modules/module-filter-apply.so
/usr/lib32/pulse-11.1/modules/module-filter-heuristics.so
/usr/lib32/pulse-11.1/modules/module-hal-detect.so
/usr/lib32/pulse-11.1/modules/module-http-protocol-tcp.so
/usr/lib32/pulse-11.1/modules/module-http-protocol-unix.so
/usr/lib32/pulse-11.1/modules/module-intended-roles.so
/usr/lib32/pulse-11.1/modules/module-ladspa-sink.so
/usr/lib32/pulse-11.1/modules/module-loopback.so
/usr/lib32/pulse-11.1/modules/module-match.so
/usr/lib32/pulse-11.1/modules/module-mmkbd-evdev.so
/usr/lib32/pulse-11.1/modules/module-native-protocol-fd.so
/usr/lib32/pulse-11.1/modules/module-native-protocol-tcp.so
/usr/lib32/pulse-11.1/modules/module-native-protocol-unix.so
/usr/lib32/pulse-11.1/modules/module-null-sink.so
/usr/lib32/pulse-11.1/modules/module-null-source.so
/usr/lib32/pulse-11.1/modules/module-oss.so
/usr/lib32/pulse-11.1/modules/module-pipe-sink.so
/usr/lib32/pulse-11.1/modules/module-pipe-source.so
/usr/lib32/pulse-11.1/modules/module-position-event-sounds.so
/usr/lib32/pulse-11.1/modules/module-raop-sink.so
/usr/lib32/pulse-11.1/modules/module-remap-sink.so
/usr/lib32/pulse-11.1/modules/module-remap-source.so
/usr/lib32/pulse-11.1/modules/module-rescue-streams.so
/usr/lib32/pulse-11.1/modules/module-role-cork.so
/usr/lib32/pulse-11.1/modules/module-role-ducking.so
/usr/lib32/pulse-11.1/modules/module-rtp-recv.so
/usr/lib32/pulse-11.1/modules/module-rtp-send.so
/usr/lib32/pulse-11.1/modules/module-rygel-media-server.so
/usr/lib32/pulse-11.1/modules/module-simple-protocol-tcp.so
/usr/lib32/pulse-11.1/modules/module-simple-protocol-unix.so
/usr/lib32/pulse-11.1/modules/module-sine-source.so
/usr/lib32/pulse-11.1/modules/module-sine.so
/usr/lib32/pulse-11.1/modules/module-stream-restore.so
/usr/lib32/pulse-11.1/modules/module-suspend-on-idle.so
/usr/lib32/pulse-11.1/modules/module-switch-on-connect.so
/usr/lib32/pulse-11.1/modules/module-switch-on-port-available.so
/usr/lib32/pulse-11.1/modules/module-systemd-login.so
/usr/lib32/pulse-11.1/modules/module-tunnel-sink-new.so
/usr/lib32/pulse-11.1/modules/module-tunnel-sink.so
/usr/lib32/pulse-11.1/modules/module-tunnel-source-new.so
/usr/lib32/pulse-11.1/modules/module-tunnel-source.so
/usr/lib32/pulse-11.1/modules/module-udev-detect.so
/usr/lib32/pulse-11.1/modules/module-virtual-sink.so
/usr/lib32/pulse-11.1/modules/module-virtual-source.so
/usr/lib32/pulse-11.1/modules/module-virtual-surround-sink.so
/usr/lib32/pulse-11.1/modules/module-volume-restore.so
/usr/lib32/pulse-11.1/modules/module-x11-bell.so
/usr/lib32/pulse-11.1/modules/module-x11-cork-request.so
/usr/lib32/pulse-11.1/modules/module-x11-publish.so
/usr/lib32/pulse-11.1/modules/module-x11-xsmp.so
/usr/lib32/pulseaudio/libpulsecommon-11.1.so
/usr/lib32/pulseaudio/libpulsecore-11.1.so
/usr/lib32/pulseaudio/libpulsedsp.so

%files locales -f pulseaudio.lang
%defattr(-,root,root,-)

