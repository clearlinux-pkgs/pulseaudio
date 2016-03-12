#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pulseaudio
Version  : 8.0
Release  : 4
URL      : https://freedesktop.org/software/pulseaudio/releases/pulseaudio-8.0.tar.xz
Source0  : https://freedesktop.org/software/pulseaudio/releases/pulseaudio-8.0.tar.xz
Summary  : PulseAudio Simplified Synchronous Client Interface
Group    : Development/Tools
License  : LGPL-2.1
Requires: pulseaudio-bin
Requires: pulseaudio-config
Requires: pulseaudio-lib
Requires: pulseaudio-data
Requires: pulseaudio-locales
Requires: pulseaudio-doc
BuildRequires : gdbm-dev
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : libcap-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(fftw3f)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(orc-0.4)
BuildRequires : pkgconfig(sndfile)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb)
Patch1: 0001-Support-a-stateless-configuration.patch

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


%package locales
Summary: locales components for the pulseaudio package.
Group: Default

%description locales
locales components for the pulseaudio package.


%prep
%setup -q -n pulseaudio-8.0
%patch1 -p1

%build
%autogen --disable-static --with-udev-rules-dir=/usr/lib/udev/rules.d --enable-orc
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang pulseaudio
## make_install_append content
rm -rf %{buildroot}%{_datadir}/vala
## make_install_append end

%files
%defattr(-,root,root,-)
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
/usr/bin/pulseaudio
/usr/bin/qpaeq

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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/pulse-8.0/modules/libalsa-util.so
/usr/lib64/pulse-8.0/modules/libcli.so
/usr/lib64/pulse-8.0/modules/liboss-util.so
/usr/lib64/pulse-8.0/modules/libprotocol-cli.so
/usr/lib64/pulse-8.0/modules/libprotocol-esound.so
/usr/lib64/pulse-8.0/modules/libprotocol-http.so
/usr/lib64/pulse-8.0/modules/libprotocol-native.so
/usr/lib64/pulse-8.0/modules/libprotocol-simple.so
/usr/lib64/pulse-8.0/modules/libraop.so
/usr/lib64/pulse-8.0/modules/librtp.so
/usr/lib64/pulse-8.0/modules/module-alsa-card.so
/usr/lib64/pulse-8.0/modules/module-alsa-sink.so
/usr/lib64/pulse-8.0/modules/module-alsa-source.so
/usr/lib64/pulse-8.0/modules/module-always-sink.so
/usr/lib64/pulse-8.0/modules/module-augment-properties.so
/usr/lib64/pulse-8.0/modules/module-card-restore.so
/usr/lib64/pulse-8.0/modules/module-cli-protocol-tcp.so
/usr/lib64/pulse-8.0/modules/module-cli-protocol-unix.so
/usr/lib64/pulse-8.0/modules/module-cli.so
/usr/lib64/pulse-8.0/modules/module-combine-sink.so
/usr/lib64/pulse-8.0/modules/module-combine.so
/usr/lib64/pulse-8.0/modules/module-console-kit.so
/usr/lib64/pulse-8.0/modules/module-dbus-protocol.so
/usr/lib64/pulse-8.0/modules/module-default-device-restore.so
/usr/lib64/pulse-8.0/modules/module-detect.so
/usr/lib64/pulse-8.0/modules/module-device-manager.so
/usr/lib64/pulse-8.0/modules/module-device-restore.so
/usr/lib64/pulse-8.0/modules/module-echo-cancel.so
/usr/lib64/pulse-8.0/modules/module-equalizer-sink.so
/usr/lib64/pulse-8.0/modules/module-esound-compat-spawnfd.so
/usr/lib64/pulse-8.0/modules/module-esound-compat-spawnpid.so
/usr/lib64/pulse-8.0/modules/module-esound-protocol-tcp.so
/usr/lib64/pulse-8.0/modules/module-esound-protocol-unix.so
/usr/lib64/pulse-8.0/modules/module-esound-sink.so
/usr/lib64/pulse-8.0/modules/module-filter-apply.so
/usr/lib64/pulse-8.0/modules/module-filter-heuristics.so
/usr/lib64/pulse-8.0/modules/module-hal-detect.so
/usr/lib64/pulse-8.0/modules/module-http-protocol-tcp.so
/usr/lib64/pulse-8.0/modules/module-http-protocol-unix.so
/usr/lib64/pulse-8.0/modules/module-intended-roles.so
/usr/lib64/pulse-8.0/modules/module-ladspa-sink.so
/usr/lib64/pulse-8.0/modules/module-loopback.so
/usr/lib64/pulse-8.0/modules/module-match.so
/usr/lib64/pulse-8.0/modules/module-mmkbd-evdev.so
/usr/lib64/pulse-8.0/modules/module-native-protocol-fd.so
/usr/lib64/pulse-8.0/modules/module-native-protocol-tcp.so
/usr/lib64/pulse-8.0/modules/module-native-protocol-unix.so
/usr/lib64/pulse-8.0/modules/module-null-sink.so
/usr/lib64/pulse-8.0/modules/module-null-source.so
/usr/lib64/pulse-8.0/modules/module-oss.so
/usr/lib64/pulse-8.0/modules/module-pipe-sink.so
/usr/lib64/pulse-8.0/modules/module-pipe-source.so
/usr/lib64/pulse-8.0/modules/module-position-event-sounds.so
/usr/lib64/pulse-8.0/modules/module-raop-sink.so
/usr/lib64/pulse-8.0/modules/module-remap-sink.so
/usr/lib64/pulse-8.0/modules/module-remap-source.so
/usr/lib64/pulse-8.0/modules/module-rescue-streams.so
/usr/lib64/pulse-8.0/modules/module-role-cork.so
/usr/lib64/pulse-8.0/modules/module-role-ducking.so
/usr/lib64/pulse-8.0/modules/module-rtp-recv.so
/usr/lib64/pulse-8.0/modules/module-rtp-send.so
/usr/lib64/pulse-8.0/modules/module-rygel-media-server.so
/usr/lib64/pulse-8.0/modules/module-simple-protocol-tcp.so
/usr/lib64/pulse-8.0/modules/module-simple-protocol-unix.so
/usr/lib64/pulse-8.0/modules/module-sine-source.so
/usr/lib64/pulse-8.0/modules/module-sine.so
/usr/lib64/pulse-8.0/modules/module-stream-restore.so
/usr/lib64/pulse-8.0/modules/module-suspend-on-idle.so
/usr/lib64/pulse-8.0/modules/module-switch-on-connect.so
/usr/lib64/pulse-8.0/modules/module-switch-on-port-available.so
/usr/lib64/pulse-8.0/modules/module-systemd-login.so
/usr/lib64/pulse-8.0/modules/module-tunnel-sink-new.so
/usr/lib64/pulse-8.0/modules/module-tunnel-sink.so
/usr/lib64/pulse-8.0/modules/module-tunnel-source-new.so
/usr/lib64/pulse-8.0/modules/module-tunnel-source.so
/usr/lib64/pulse-8.0/modules/module-udev-detect.so
/usr/lib64/pulse-8.0/modules/module-virtual-sink.so
/usr/lib64/pulse-8.0/modules/module-virtual-source.so
/usr/lib64/pulse-8.0/modules/module-virtual-surround-sink.so
/usr/lib64/pulse-8.0/modules/module-volume-restore.so
/usr/lib64/pulseaudio/libpulsecommon-8.0.so
/usr/lib64/pulseaudio/libpulsecore-8.0.so
/usr/lib64/pulseaudio/libpulsedsp.so

%files locales -f pulseaudio.lang 
%defattr(-,root,root,-)

