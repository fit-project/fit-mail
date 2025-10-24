#!/usr/bin/env bash
set -euo pipefail

APP=fit-mail
VERSION="$(python -c 'from fit_common.core import get_version; print(get_version())')"
BUILD_DIR="$(pwd)"
DIST_DIR="$BUILD_DIR/dist/$APP"
APPDIR="$BUILD_DIR/AppDir"

# 1) PyInstaller
pyinstaller --clean -y fit-onefile.spec

# 2) Create AppDir
rm -rf "$APPDIR"
mkdir -p "$APPDIR/usr/bin"
cp -a "$DIST_DIR/." "$APPDIR/usr/bin/"

# 3) Icon and desktop
cp icon.png "$APPDIR/fit-mail.png"

cat > "$APPDIR/$APP.desktop" <<EOF
[Desktop Entry]
Type=Application
Name=FIT Mail
Exec=$APP
Icon=fit-mail
Terminal=false
Categories=Utility;Network;
EOF

# 4) AppRun
cat > "$APPDIR/AppRun" <<'EOF'
#!/usr/bin/env bash
HERE="$(dirname "$(readlink -f "$0")")"
export PATH="$HERE/usr/bin:$PATH"
export QT_QPA_PLATFORM=wayland,xcb
exec "$HERE/usr/bin/fit-mail" "$@"
EOF
chmod +x "$APPDIR/AppRun"

# 5) Make AppImage
appimagetool "$APPDIR" "$BUILD_DIR/${APP}-${VERSION}-linux-x86_64.AppImage"
echo "Creato ${APP}-${VERSION}-linux-x86_64.AppImage"