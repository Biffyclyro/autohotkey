pkgname="autohotkey-pkg"
pkgver="1.0.0"
pkgrel="1"
pkgdesc="Autohotkey for linux"
arch=("x86_64")
depends=("python" "python-pipenv")
license=("custom")
install=autohotkey.install
source=("main.py" "Pipfile" "Pipfile.lock" "autohotkey.service.config" "template.txt.exemple" "autohotkey")
sha512sums=("SKIP" "SKIP" "SKIP" "SKIP" "SKIP" "SKIP")
package() {
  mkdir -p "${pkgdir}/usr/bin"
  mkdir -p "${pkgdir}/usr/lib/systemd/system"
  mkdir -p "${pkgdir}/usr/lib/$pkgname"
  cp "${srcdir}/main.py" "${pkgdir}/usr/lib/$pkgname/"
  cp "${srcdir}/Pipfile" "${pkgdir}/usr/lib/$pkgname/"
  cp "${srcdir}/Pipfile.lock" "${pkgdir}/usr/lib/$pkgname/"
  cp "${srcdir}/autohotkey" "${pkgdir}/usr/bin/"
  sh "${srcdir}/autohotkey.service.config" $srcdir $pkgdir
  chmod +x "${pkgdir}/usr/lib/$package"
  chmod +x "${pkgdir}/usr/bin/autohotkey"
}
