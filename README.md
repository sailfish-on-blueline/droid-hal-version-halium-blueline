# Pixel 3 hardware identity

Uses the upstream `mer-hybris/droid-hal-version` Git submodule to build the Google Pixel 3 Halium 12 version metapackage. The spec includes `droid-hal-version/droid-hal-version.inc` directly. The submodule commit is pinned by this repository.

The upstream template generates `/usr/lib/hw-release`, the `/etc/hw-release` symlink, build metadata and a documentation subpackage. The device spec supplies the Google manufacturer, Pixel 3 model, `halium-blueline` adaptation identity, native vibrator configuration and aarch64 identity fields. Epoch 1 preserves upgrade ordering from the previous standalone `0.1-2` package to the upstream `0.0.1` version scheme.

The device spec uses OBS `BuildIgnore` directives for the upstream boot and recovery image build dependencies. This metapackage generates hardware identity and build metadata. Its runtime dependency on `kernel-adaptation-halium-blueline` supplies the installed device's kernel.

Initialize the submodule after cloning.

```sh
git submodule update --init --recursive
```

Build inside the Sailfish Platform SDK.

```sh
rpmbuild --build-in-place --nodeps --target aarch64 -bb rpm/droid-hal-version-halium-blueline.spec
```
