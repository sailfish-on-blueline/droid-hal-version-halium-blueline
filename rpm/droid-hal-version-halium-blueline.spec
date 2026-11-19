Name: droid-hal-version-halium-blueline
Version: 0.1
Release: 2
Summary: Google Pixel 3 Halium adaptation identity
License: GPLv2
BuildArch: noarch
AutoReqProv: no
Provides: droid-hal-version
Provides: hw-release
Requires: droid-config-halium-blueline
Requires: kernel-adaptation-halium-blueline

%description
Hardware identity for the AOSP Android 12 Google Pixel 3 Sailfish adaptation.

%install
mkdir -p %{buildroot}/etc
cat > %{buildroot}/etc/hw-release <<'HWRELEASE'
NAME="Google Pixel 3"
ID=halium-blueline
VERSION_ID=0.1
PRETTY_NAME="Google Pixel 3 (Halium 12)"
MER_HA_DEVICE=halium-blueline
SAILFISH_VENDOR=google
SAILFISH_DEVICE=halium-blueline
SAILFISH_PRODUCT=halium-blueline
SAILFISH_ARCH=aarch64
SAILFISH_TYPE=community
HWRELEASE

%files
/etc/hw-release
