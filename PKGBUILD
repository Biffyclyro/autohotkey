pkgname="autohotkey-pkg"
pkgver="1.0.0"
pkgrel="1"
pkgdesc="Autohotkey for linux"
arch=("x86_64")
depends=("python>=3.10.1" "python-pipenv>=2021.11.23")
makedepends=("git")
license=("custom")
install=autohotkey.install
source=("main.py" "Pipfile" "Pipfile.lock" "create.config" "template.txt.example" "autohotkey" "install-env")
sha512sums=("SKIP" "SKIP" "SKIP" "SKIP" "SKIP" "SKIP" "SKIP")

package() {
  mkdir -p "${pkgdir}/usr/bin"
  mkdir -p "${pkgdir}/usr/lib/systemd/system"
  mkdir -p "${pkgdir}/usr/lib/$pkgname"
  mkdir -p "${pkgdir}/usr/share/libalpm/hooks/"
  cp "${srcdir}/main.py" "${pkgdir}/usr/lib/$pkgname/"
  cp "${srcdir}/Pipfile" "${pkgdir}/usr/lib/$pkgname/"
  cp "${srcdir}/Pipfile.lock" "${pkgdir}/usr/lib/$pkgname/"
  cp "${srcdir}/template.txt.example" "${pkgdir}/usr/lib/$pkgname/"
  cp "${srcdir}/autohotkey" "${pkgdir}/usr/bin/"
  cp "${srcdir}/install-env" "${pkgdir}/usr/lib/$pkgname/"
  sh "${srcdir}/create.config" $srcdir $pkgdir
  chmod +x "${pkgdir}/usr/lib/$package"
  chmod +x "${pkgdir}/usr/bin/autohotkey"
  chmod +x "${pkgdir}/usr/lib/$pkgname/install-env"
}
