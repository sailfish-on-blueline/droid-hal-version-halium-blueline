%define device halium-blueline
%define vendor google
%define vendor_pretty Google
%define device_pretty Pixel 3
%define have_vibrator_native 1
%define have_kernel_modules 1

# The version metapackage only generates hardware identity and build metadata.
#!BuildIgnore: droid-hal-img-boot
#!BuildIgnore: droid-hal-img-recovery

# The upstream version starts at 0.0.1; retain upgrade ordering from 0.1-2.
Epoch: 1
BuildArch: noarch
AutoReqProv: no
Provides: droid-hal-version
Provides: hw-release
Requires: droid-config-halium-blueline
Requires: kernel-adaptation-halium-blueline

%include droid-hal-version/droid-hal-version.inc

# Preserve the Halium identity fields used by this adaptation.
cat >> %{buildroot}%{_prefix}/lib/hw-release <<'HWRELEASE'
SAILFISH_VENDOR=google
SAILFISH_DEVICE=halium-blueline
SAILFISH_PRODUCT=halium-blueline
SAILFISH_ARCH=aarch64
SAILFISH_TYPE=community
HWRELEASE
cp %{buildroot}%{_prefix}/lib/hw-release %{buildroot}%{_datadir}/doc/SailfishOS/hw-release
