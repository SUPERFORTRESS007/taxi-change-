[app]
title = Taxi Change
source.dir = .
package.name = taxichange
package.domain = org.taxi
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0
icon.filename = %(source.dir)s/icon.png
android.permissions = INTERNET
android.accept_sdk_license = True
android.api = 34
android.build_tools_version = 34.0.0
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
