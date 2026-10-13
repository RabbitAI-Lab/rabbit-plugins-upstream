#!/usr/bin/env python3
"""Install a verified standalone CLI without replacing existing installations.

Python 3.9+ standard library; curl is preferred when available for OS TLS support.
Only --version is executed. Account data, services, PATH and shell files are untouched.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import platform
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
import zipfile


MANIFEST = Path(__file__).resolve().parent.parent / "references" / "cli-release.json"


def detect_platform(system=None, machine=None):
    system = system or platform.system()
    machine = (machine or platform.machine()).lower()
    if system == "Windows":
        machine = os.environ.get("PROCESSOR_ARCHITEW6432", machine).lower()
    if system == "Darwin" and machine in ("x86_64", "amd64"):
        # A translated Python process may report x86_64 on Apple Silicon.
        result = subprocess.run(["/usr/sbin/sysctl", "-in", "sysctl.proc_translated"],
                                capture_output=True, text=True, check=False)
        if result.returncode == 0 and result.stdout.strip() == "1":
            machine = "arm64"
    arch = {"amd64": "x86_64", "x86_64": "x86_64", "arm64": "arm64",
            "aarch64": "arm64"}.get(machine, machine)
    prefix = {"Darwin": "macos", "Linux": "linux", "Windows": "windows"}.get(system)
    key = f"{prefix}-{arch}"
    if key not in ("macos-arm64", "macos-x86_64", "linux-x86_64", "windows-x86_64"):
        raise RuntimeError(f"No release for {system}/{machine}; no installation changed")
    return key


def default_directory():
    if os.name == "nt":
        local = os.environ.get("LOCALAPPDATA")
        if not local:
            raise RuntimeError("LOCALAPPDATA is missing; specify --install-dir")
        return Path(local) / "Programs" / "WeMolCLI"
    return Path.home() / ".local" / "bin"


def candidates(directory, explicit=None):
    if explicit:
        path = Path(explicit).expanduser().absolute()
        if not path.is_file():
            raise RuntimeError("--existing-cli must identify an existing executable")
        return [path]
    names = ["wemol-cli"]
    if os.name == "nt":
        extensions = os.environ.get("PATHEXT", ".COM;.EXE;.BAT;.CMD").split(";")
        names += ["wemol-cli" + ext.lower() for ext in extensions if ext]
    found = {}
    for folder in [*os.get_exec_path(), str(directory)]:
        for name in names:
            path = Path(folder or os.curdir).expanduser().absolute() / name
            if path.is_file():
                found.setdefault(str(path.resolve()), path)
            elif path.is_symlink():
                raise RuntimeError(f"Broken CLI symlink: {path}; no installation changed")
    return list(found.values())


def version_of(path):
    p = subprocess.run([str(path), "--version"], capture_output=True, text=True,
                       timeout=15, check=False)
    match = re.fullmatch(r"wemol-cli (\d+\.\d+\.\d+(?:[-+][\w.-]+)?)", p.stdout.strip())
    if p.returncode or not match:
        raise RuntimeError(f"Cannot verify CLI identity/version at {path}; left unchanged")
    return match[1]


def existing_result(path, expected):
    version = version_of(path)
    return {"ok": True, "action": "reused" if version == expected else "existing-version",
            "path": str(path), "version": version, "required_version": expected,
            "compatible": version == expected, "configuration_changed": False}


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def verify(path, size, expected):
    if path.stat().st_size != size or digest(path) != expected:
        raise RuntimeError(f"Checksum/size mismatch for {path.name}; nothing installed")


def download(asset, target):
    url = asset["url"]
    if not url.startswith("https://github.com/wecomput/wemol-cli/releases/download/v"):
        raise RuntimeError("Release manifest must use the official HTTPS release origin")
    curl = shutil.which("curl")
    if curl:
        p = subprocess.run([curl, "--fail", "--location", "--silent", "--show-error",
                            "--proto", "=https", "--proto-redir", "=https",
                            "--connect-timeout", "15", "--max-time", "120",
                            "--max-filesize", str(asset["archive_size"]),
                            "--output", str(target), url],
                           capture_output=True, text=True, timeout=130, check=False)
        if p.returncode:
            raise RuntimeError(f"Download failed: {p.stderr.strip()}")
    else:
        class HttpsRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, req, fp, code, msg, headers, newurl):
                if not newurl.startswith("https://"):
                    raise RuntimeError("Refusing non-HTTPS download redirect")
                return super().redirect_request(req, fp, code, msg, headers, newurl)
        opener = urllib.request.build_opener(HttpsRedirect())
        with opener.open(url, timeout=60) as response, target.open("wb") as out:
            total = 0
            while chunk := response.read(1024 * 1024):
                total += len(chunk)
                if total > asset["archive_size"]:
                    raise RuntimeError("Download exceeds the pinned archive size")
                out.write(chunk)


def extract_binary(archive, asset, target):
    # Read exactly one regular member; never extract archive paths to the filesystem.
    if asset["format"] == "zip":
        with zipfile.ZipFile(archive) as z:
            members = [m for m in z.infolist()
                       if PurePosixPath(m.filename).name == asset["executable"] and not m.is_dir()]
            if len(members) != 1 or stat.S_ISLNK(members[0].external_attr >> 16):
                raise RuntimeError("Archive must contain exactly one regular CLI executable")
            if members[0].file_size != asset["binary_size"]:
                raise RuntimeError("Unexpected executable size")
            with z.open(members[0]) as src, target.open("wb") as dst:
                shutil.copyfileobj(src, dst)
    elif asset["format"] == "tar.gz":
        with tarfile.open(archive, "r:gz") as t:
            members = [m for m in t.getmembers() if PurePosixPath(m.name).name == asset["executable"]]
            if len(members) != 1 or not members[0].isreg():
                raise RuntimeError("Archive must contain exactly one regular CLI executable")
            if members[0].size != asset["binary_size"]:
                raise RuntimeError("Unexpected executable size")
            with t.extractfile(members[0]) as src, target.open("wb") as dst:
                shutil.copyfileobj(src, dst)
    else:
        raise RuntimeError("Unsupported archive format")
    verify(target, asset["binary_size"], asset["binary_sha256"])


def install(directory, manifest, platform_key, explicit=None):
    paths = candidates(directory, explicit)
    if len(paths) > 1:
        return {"ok": False, "action": "select-existing",
                "candidates": [str(p) for p in paths], "configuration_changed": False}
    if paths:
        return existing_result(paths[0], manifest["version"])
    platform_key = platform_key or detect_platform()
    asset = manifest["platforms"][platform_key]
    target = directory / asset["executable"]
    if target.exists() or target.is_symlink():
        raise RuntimeError(f"Installation target already exists: {target}")
    # Download/check before creating a persistent directory or touching its contents.
    with tempfile.TemporaryDirectory(prefix="wemol-cli-download-") as temp:
        archive = Path(temp) / "release.archive"
        download(asset, archive)
        verify(archive, asset["archive_size"], asset["archive_sha256"])
        created = not directory.exists()
        directory.mkdir(parents=True, exist_ok=True)
        try:
            with tempfile.TemporaryDirectory(prefix=".wemol-cli-stage-", dir=directory) as stage:
                binary = Path(stage) / asset["executable"]
                extract_binary(archive, asset, binary)
                binary.chmod(0o755)
                if version_of(binary) != manifest["version"]:
                    raise RuntimeError("Downloaded executable reports an unexpected version")
                # Atomic no-clobber install, including a concurrent install race.
                os.link(binary, target)
        finally:
            if created and not target.exists():
                try:
                    directory.rmdir()
                except OSError:
                    pass
    return {"ok": True, "action": "installed", "path": str(target),
            "version": manifest["version"], "platform": platform_key, "compatible": True,
            "configuration_changed": False,
            "on_path": any(Path(p or os.curdir).resolve() == directory.resolve() for p in os.get_exec_path())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--install-dir", type=Path, help="Override the user binary directory")
    parser.add_argument("--existing-cli", help="Explicit existing CLI when multiple installations exist")
    args = parser.parse_args()
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        directory = (args.install_dir or default_directory()).expanduser().absolute()
        result = install(directory, manifest, None, args.existing_cli)
    except Exception as error:
        result = {"ok": False, "action": "stopped", "error": str(error), "configuration_changed": False}
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["ok"] and result.get("compatible") else 1


if __name__ == "__main__":
    sys.exit(main())
