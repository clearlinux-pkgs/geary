#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : geary
Version  : 3.32.2
Release  : 3
URL      : https://download.gnome.org/sources/geary/3.32/geary-3.32.2.tar.xz
Source0  : https://download.gnome.org/sources/geary/3.32/geary-3.32.2.tar.xz
Summary  : A lightweight email client for the GNOME desktop
Group    : Development/Tools
License  : BSD-2-Clause CC-BY-SA-3.0 LGPL-2.1
Requires: geary-bin = %{version}-%{release}
Requires: geary-data = %{version}-%{release}
Requires: geary-lib = %{version}-%{release}
Requires: geary-license = %{version}-%{release}
Requires: geary-locales = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : folks-dev
BuildRequires : gnome-online-accounts-dev
BuildRequires : json-glib-dev
BuildRequires : libnotify-dev
BuildRequires : pkgconfig(enchant-2)
BuildRequires : pkgconfig(folks)
BuildRequires : pkgconfig(gck-1)
BuildRequires : pkgconfig(gmime-2.6)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(iso-codes)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libcanberra)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libunwind)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(webkit2gtk-4.0)
BuildRequires : sqlite-autoconf-dev
BuildRequires : webkitgtk-dev
BuildRequires : ytnef-dev

%description
Geary: Send and receive email
=============================
Geary is an email application built around conversations, for the
GNOME 3 desktop. It allows you to read, find and send email with a
straightforward, modern interface.

%package bin
Summary: bin components for the geary package.
Group: Binaries
Requires: geary-data = %{version}-%{release}
Requires: geary-license = %{version}-%{release}

%description bin
bin components for the geary package.


%package data
Summary: data components for the geary package.
Group: Data

%description data
data components for the geary package.


%package doc
Summary: doc components for the geary package.
Group: Documentation

%description doc
doc components for the geary package.


%package lib
Summary: lib components for the geary package.
Group: Libraries
Requires: geary-data = %{version}-%{release}
Requires: geary-license = %{version}-%{release}

%description lib
lib components for the geary package.


%package license
Summary: license components for the geary package.
Group: Default

%description license
license components for the geary package.


%package locales
Summary: locales components for the geary package.
Group: Default

%description locales
locales components for the geary package.


%prep
%setup -q -n geary-3.32.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565190835
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/geary
cp COPYING %{buildroot}/usr/share/package-licenses/geary/COPYING
cp COPYING.icons %{buildroot}/usr/share/package-licenses/geary/COPYING.icons
cp COPYING.snowball %{buildroot}/usr/share/package-licenses/geary/COPYING.snowball
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang geary

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/geary

%files data
%defattr(-,root,root,-)
/usr/share/applications/geary-autostart.desktop
/usr/share/applications/org.gnome.Geary.desktop
/usr/share/geary/sql/version-001.sql
/usr/share/geary/sql/version-002.sql
/usr/share/geary/sql/version-003.sql
/usr/share/geary/sql/version-004.sql
/usr/share/geary/sql/version-005.sql
/usr/share/geary/sql/version-006.sql
/usr/share/geary/sql/version-007.sql
/usr/share/geary/sql/version-008.sql
/usr/share/geary/sql/version-009.sql
/usr/share/geary/sql/version-010.sql
/usr/share/geary/sql/version-011.sql
/usr/share/geary/sql/version-012.sql
/usr/share/geary/sql/version-013.sql
/usr/share/geary/sql/version-014.sql
/usr/share/geary/sql/version-015.sql
/usr/share/geary/sql/version-016.sql
/usr/share/geary/sql/version-017.sql
/usr/share/geary/sql/version-018.sql
/usr/share/geary/sql/version-019.sql
/usr/share/geary/sql/version-020.sql
/usr/share/geary/sql/version-021.sql
/usr/share/geary/sql/version-022.sql
/usr/share/geary/sql/version-023.sql
/usr/share/geary/sql/version-024.sql
/usr/share/geary/sql/version-025.sql
/usr/share/glib-2.0/schemas/org.gnome.Geary.gschema.xml
/usr/share/icons/hicolor/scalable/actions/close-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/detach-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/edit-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/format-ordered-list-symbolic-rtl.svg
/usr/share/icons/hicolor/scalable/actions/format-ordered-list-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/format-text-remove-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/format-unordered-list-symbolic-rtl.svg
/usr/share/icons/hicolor/scalable/actions/format-unordered-list-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/mail-archive-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/mail-drafts-symbolic-rtl.svg
/usr/share/icons/hicolor/scalable/actions/mail-drafts-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/mail-forward-symbolic-rtl.svg
/usr/share/icons/hicolor/scalable/actions/mail-forward-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/mail-inbox-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/mail-outbox-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/mail-reply-all-symbolic-rtl.svg
/usr/share/icons/hicolor/scalable/actions/mail-reply-all-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/mail-reply-sender-symbolic-rtl.svg
/usr/share/icons/hicolor/scalable/actions/mail-reply-sender-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/mail-sent-symbolic-rtl.svg
/usr/share/icons/hicolor/scalable/actions/mail-sent-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/marker-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/tag-symbolic-rtl.svg
/usr/share/icons/hicolor/scalable/actions/tag-symbolic.svg
/usr/share/icons/hicolor/scalable/actions/text-x-generic-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.Geary.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Geary-symbolic.svg
/usr/share/metainfo/org.gnome.Geary.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/geary/accounts.page
/usr/share/help/C/geary/archive.page
/usr/share/help/C/geary/bugs.page
/usr/share/help/C/geary/contributing.page
/usr/share/help/C/geary/figures/geary.svg
/usr/share/help/C/geary/index.page
/usr/share/help/C/geary/label.page
/usr/share/help/C/geary/limits.page
/usr/share/help/C/geary/overview.page
/usr/share/help/C/geary/preferences.page
/usr/share/help/C/geary/search.page
/usr/share/help/C/geary/shortcuts.page
/usr/share/help/C/geary/star.page
/usr/share/help/C/geary/write.page
/usr/share/help/cs/geary/accounts.page
/usr/share/help/cs/geary/archive.page
/usr/share/help/cs/geary/bugs.page
/usr/share/help/cs/geary/contributing.page
/usr/share/help/cs/geary/figures/geary.svg
/usr/share/help/cs/geary/index.page
/usr/share/help/cs/geary/label.page
/usr/share/help/cs/geary/limits.page
/usr/share/help/cs/geary/overview.page
/usr/share/help/cs/geary/preferences.page
/usr/share/help/cs/geary/search.page
/usr/share/help/cs/geary/shortcuts.page
/usr/share/help/cs/geary/star.page
/usr/share/help/cs/geary/write.page
/usr/share/help/de/geary/accounts.page
/usr/share/help/de/geary/archive.page
/usr/share/help/de/geary/bugs.page
/usr/share/help/de/geary/contributing.page
/usr/share/help/de/geary/figures/geary.svg
/usr/share/help/de/geary/index.page
/usr/share/help/de/geary/label.page
/usr/share/help/de/geary/limits.page
/usr/share/help/de/geary/overview.page
/usr/share/help/de/geary/preferences.page
/usr/share/help/de/geary/search.page
/usr/share/help/de/geary/shortcuts.page
/usr/share/help/de/geary/star.page
/usr/share/help/de/geary/write.page
/usr/share/help/el/geary/accounts.page
/usr/share/help/el/geary/archive.page
/usr/share/help/el/geary/bugs.page
/usr/share/help/el/geary/contributing.page
/usr/share/help/el/geary/figures/geary.svg
/usr/share/help/el/geary/index.page
/usr/share/help/el/geary/label.page
/usr/share/help/el/geary/limits.page
/usr/share/help/el/geary/overview.page
/usr/share/help/el/geary/preferences.page
/usr/share/help/el/geary/search.page
/usr/share/help/el/geary/shortcuts.page
/usr/share/help/el/geary/star.page
/usr/share/help/el/geary/write.page
/usr/share/help/es/geary/accounts.page
/usr/share/help/es/geary/archive.page
/usr/share/help/es/geary/bugs.page
/usr/share/help/es/geary/contributing.page
/usr/share/help/es/geary/figures/geary.svg
/usr/share/help/es/geary/index.page
/usr/share/help/es/geary/label.page
/usr/share/help/es/geary/limits.page
/usr/share/help/es/geary/overview.page
/usr/share/help/es/geary/preferences.page
/usr/share/help/es/geary/search.page
/usr/share/help/es/geary/shortcuts.page
/usr/share/help/es/geary/star.page
/usr/share/help/es/geary/write.page
/usr/share/help/fr/geary/accounts.page
/usr/share/help/fr/geary/archive.page
/usr/share/help/fr/geary/bugs.page
/usr/share/help/fr/geary/contributing.page
/usr/share/help/fr/geary/figures/geary.svg
/usr/share/help/fr/geary/index.page
/usr/share/help/fr/geary/label.page
/usr/share/help/fr/geary/limits.page
/usr/share/help/fr/geary/overview.page
/usr/share/help/fr/geary/preferences.page
/usr/share/help/fr/geary/search.page
/usr/share/help/fr/geary/shortcuts.page
/usr/share/help/fr/geary/star.page
/usr/share/help/fr/geary/write.page
/usr/share/help/it/geary/accounts.page
/usr/share/help/it/geary/archive.page
/usr/share/help/it/geary/bugs.page
/usr/share/help/it/geary/contributing.page
/usr/share/help/it/geary/figures/geary.svg
/usr/share/help/it/geary/index.page
/usr/share/help/it/geary/label.page
/usr/share/help/it/geary/limits.page
/usr/share/help/it/geary/overview.page
/usr/share/help/it/geary/preferences.page
/usr/share/help/it/geary/search.page
/usr/share/help/it/geary/shortcuts.page
/usr/share/help/it/geary/star.page
/usr/share/help/it/geary/write.page
/usr/share/help/pl/geary/accounts.page
/usr/share/help/pl/geary/archive.page
/usr/share/help/pl/geary/bugs.page
/usr/share/help/pl/geary/contributing.page
/usr/share/help/pl/geary/figures/geary.svg
/usr/share/help/pl/geary/index.page
/usr/share/help/pl/geary/label.page
/usr/share/help/pl/geary/limits.page
/usr/share/help/pl/geary/overview.page
/usr/share/help/pl/geary/preferences.page
/usr/share/help/pl/geary/search.page
/usr/share/help/pl/geary/shortcuts.page
/usr/share/help/pl/geary/star.page
/usr/share/help/pl/geary/write.page
/usr/share/help/pt_BR/geary/accounts.page
/usr/share/help/pt_BR/geary/archive.page
/usr/share/help/pt_BR/geary/bugs.page
/usr/share/help/pt_BR/geary/contributing.page
/usr/share/help/pt_BR/geary/figures/geary.svg
/usr/share/help/pt_BR/geary/index.page
/usr/share/help/pt_BR/geary/label.page
/usr/share/help/pt_BR/geary/limits.page
/usr/share/help/pt_BR/geary/overview.page
/usr/share/help/pt_BR/geary/preferences.page
/usr/share/help/pt_BR/geary/search.page
/usr/share/help/pt_BR/geary/shortcuts.page
/usr/share/help/pt_BR/geary/star.page
/usr/share/help/pt_BR/geary/write.page
/usr/share/help/sv/geary/accounts.page
/usr/share/help/sv/geary/archive.page
/usr/share/help/sv/geary/bugs.page
/usr/share/help/sv/geary/contributing.page
/usr/share/help/sv/geary/figures/geary.svg
/usr/share/help/sv/geary/index.page
/usr/share/help/sv/geary/label.page
/usr/share/help/sv/geary/limits.page
/usr/share/help/sv/geary/overview.page
/usr/share/help/sv/geary/preferences.page
/usr/share/help/sv/geary/search.page
/usr/share/help/sv/geary/shortcuts.page
/usr/share/help/sv/geary/star.page
/usr/share/help/sv/geary/write.page
/usr/share/help/tr/geary/accounts.page
/usr/share/help/tr/geary/archive.page
/usr/share/help/tr/geary/bugs.page
/usr/share/help/tr/geary/contributing.page
/usr/share/help/tr/geary/figures/geary.svg
/usr/share/help/tr/geary/index.page
/usr/share/help/tr/geary/label.page
/usr/share/help/tr/geary/limits.page
/usr/share/help/tr/geary/overview.page
/usr/share/help/tr/geary/preferences.page
/usr/share/help/tr/geary/search.page
/usr/share/help/tr/geary/shortcuts.page
/usr/share/help/tr/geary/star.page
/usr/share/help/tr/geary/write.page

%files lib
%defattr(-,root,root,-)
/usr/lib64/geary/web-extensions/libgeary-web-process.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/geary/COPYING
/usr/share/package-licenses/geary/COPYING.icons
/usr/share/package-licenses/geary/COPYING.snowball

%files locales -f geary.lang
%defattr(-,root,root,-)

