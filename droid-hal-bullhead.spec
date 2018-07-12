# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device bullhead
%define vendor lge

%define vendor_pretty LG
%define device_pretty Nexus 5X

%define installable_zip 1

# Set dorid target to AArch64
%define droid_target_aarch64 1

%define straggler_files \
/bugreports\
/d\
/file_contexts.bin\
/property_contexts\
/sdcard\
/selinux_version\
/service_contexts\
/vendor\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

