# Pixel 3 hardware identity

Provides `/etc/hw-release` for the Google Pixel 3 Halium 12 Sailfish adaptation. Declares the Google manufacturer, Pixel 3 model, `halium-blueline` adaptation identity and aarch64 architecture.

Build inside the Sailfish Platform SDK.

```sh
rpmbuild --build-in-place --nodeps --target aarch64 -bb rpm/droid-hal-version-halium-blueline.spec
```
