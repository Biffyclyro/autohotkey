pkgname="autohotkey-pkg"
pkgver="1.0.0"
pkgrel="1"
pkgdesc="Autohotkey for linux"
arch=("x86_64")
depends=("python" "python-pipenv")
makedepends=("git")
license=("custom")
install=autohotkey.install
#source=("main.py" "Pipfile" "Pipfile.lock" "create.config" "template.txt.exemple" "autohotkey")
#sha512sums=("SKIP" "SKIP" "SKIP" "SKIP" "SKIP" "SKIP")
source=("${pkgname%-git}::git+https://github.com/Biffyclyro/autohotkey.git")
sha512sums=("SKIP")
package() {
  mkdir -p "${pkgdir}/usr/bin"
  mkdir -p "${pkgdir}/usr/lib/systemd/system"
  mkdir -p "${pkgdir}/usr/lib/$pkgname"
  cp "${srcdir}/main.py" "${pkgdir}/usr/lib/$pkgname/"
  cp "${srcdir}/Pipfile" "${pkgdir}/usr/lib/$pkgname/"
  cp "${srcdir}/Pipfile.lock" "${pkgdir}/usr/lib/$pkgname/"
  cp "${srcdir}/template.txt.exemple" "${pkgdir}/usr/lib/$pkgname/"
  cp "${srcdir}/autohotkey" "${pkgdir}/usr/bin/"
  sh "${srcdir}/create.config" $srcdir $pkgdir
  chmod +x "${pkgdir}/usr/lib/$package"
  chmod +x "${pkgdir}/usr/bin/autohotkey"
}