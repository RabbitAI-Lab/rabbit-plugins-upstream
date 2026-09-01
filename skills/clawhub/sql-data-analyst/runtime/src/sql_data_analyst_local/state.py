from __future__ import annotations

import errno
import json
import os
import secrets
import stat
from pathlib import Path, PurePath
from typing import Any


_DIRECTORY_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
_READ_FLAGS = os.O_RDONLY | os.O_NOFOLLOW
_WRITE_FLAGS = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW


class StateError(RuntimeError):
    """A stable local-state error that does not expose filesystem paths."""

    def __init__(self, code: str) -> None:
        self.code = code
        super().__init__(code)


class LocalState:
    def __init__(self, root: Path) -> None:
        absolute = os.path.abspath(os.path.expanduser(os.fspath(root)))
        self.root = Path(absolute)
        if self.root == Path(self.root.anchor):
            raise StateError("state_path_invalid")
        descriptor = self._open_root(create=True)
        try:
            os.fchmod(descriptor, 0o700)
        except OSError:
            raise StateError("state_write_failed") from None
        finally:
            os.close(descriptor)

    def read_json(self, relative_path: str | Path, default: Any = None) -> Any:
        parts = self._relative_parts(relative_path)
        try:
            parent = self._open_parent(parts, create=False)
        except FileNotFoundError:
            return default
        descriptor = -1
        try:
            try:
                descriptor = os.open(parts[-1], _READ_FLAGS, dir_fd=parent)
            except FileNotFoundError:
                return default
            except OSError as error:
                self._raise_path_or_io(error, "state_read_failed")
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                raise StateError("state_path_invalid")
            with os.fdopen(descriptor, "r", encoding="utf-8") as stream:
                descriptor = -1
                return json.load(stream)
        except StateError:
            raise
        except (OSError, UnicodeError, json.JSONDecodeError):
            raise StateError("state_read_failed") from None
        finally:
            if descriptor >= 0:
                os.close(descriptor)
            os.close(parent)

    def write_json(self, relative_path: str | Path, value: Any) -> None:
        parts = self._relative_parts(relative_path)
        try:
            encoded = json.dumps(
                value,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            ).encode("utf-8") + b"\n"
        except (TypeError, ValueError, UnicodeError):
            raise StateError("state_write_failed") from None

        parent = self._open_parent(parts, create=True)
        descriptor = -1
        temporary_name: str | None = None
        try:
            self._reject_unsafe_target(parent, parts[-1])
            descriptor, temporary_name = self._create_temporary(parent, parts[-1])
            os.fchmod(descriptor, 0o600)
            with os.fdopen(descriptor, "wb") as stream:
                descriptor = -1
                stream.write(encoded)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(
                temporary_name,
                parts[-1],
                src_dir_fd=parent,
                dst_dir_fd=parent,
            )
            temporary_name = None
            os.fsync(parent)
        except StateError:
            raise
        except OSError:
            raise StateError("state_write_failed") from None
        finally:
            if descriptor >= 0:
                os.close(descriptor)
            if temporary_name is not None:
                try:
                    os.unlink(temporary_name, dir_fd=parent)
                except OSError:
                    pass
            os.close(parent)

    def _open_root(self, *, create: bool) -> int:
        parts = self.root.parts
        try:
            descriptor = os.open(self.root.anchor, _DIRECTORY_FLAGS)
        except OSError as error:
            self._raise_path_or_io(error, "state_write_failed")
        try:
            for index, component in enumerate(parts[1:], start=1):
                next_descriptor, created = self._open_directory_at(
                    descriptor, component, create=create
                )
                os.close(descriptor)
                descriptor = next_descriptor
                if created or index == len(parts) - 1:
                    try:
                        os.fchmod(descriptor, 0o700)
                    except OSError as error:
                        self._raise_path_or_io(error, "state_write_failed")
            return descriptor
        except BaseException:
            os.close(descriptor)
            raise

    def _open_parent(self, parts: tuple[str, ...], *, create: bool) -> int:
        descriptor = self._open_root(create=create)
        try:
            for component in parts[:-1]:
                next_descriptor, _ = self._open_directory_at(
                    descriptor, component, create=create
                )
                try:
                    os.fchmod(next_descriptor, 0o700)
                except OSError as error:
                    os.close(next_descriptor)
                    self._raise_path_or_io(error, "state_write_failed")
                os.close(descriptor)
                descriptor = next_descriptor
            return descriptor
        except BaseException:
            os.close(descriptor)
            raise

    @staticmethod
    def _open_directory_at(
        parent: int, component: str, *, create: bool
    ) -> tuple[int, bool]:
        created = False
        try:
            return os.open(component, _DIRECTORY_FLAGS, dir_fd=parent), created
        except FileNotFoundError:
            if not create:
                raise
            try:
                os.mkdir(component, 0o700, dir_fd=parent)
                created = True
            except FileExistsError:
                pass
            except OSError as error:
                LocalState._raise_path_or_io(error, "state_write_failed")
            try:
                return os.open(component, _DIRECTORY_FLAGS, dir_fd=parent), created
            except OSError as error:
                LocalState._raise_path_or_io(error, "state_write_failed")
        except OSError as error:
            LocalState._raise_path_or_io(error, "state_write_failed")
        raise StateError("state_write_failed")

    @staticmethod
    def _relative_parts(relative_path: str | Path) -> tuple[str, ...]:
        path = PurePath(relative_path)
        if path.is_absolute() or not path.parts or any(
            part in {"", ".", ".."} for part in path.parts
        ):
            raise StateError("state_path_invalid")
        return path.parts

    @staticmethod
    def _reject_unsafe_target(parent: int, name: str) -> None:
        try:
            metadata = os.stat(name, dir_fd=parent, follow_symlinks=False)
        except FileNotFoundError:
            return
        except OSError as error:
            LocalState._raise_path_or_io(error, "state_write_failed")
        if not stat.S_ISREG(metadata.st_mode):
            raise StateError("state_path_invalid")

    @staticmethod
    def _create_temporary(parent: int, target_name: str) -> tuple[int, str]:
        for _ in range(16):
            temporary_name = f".{target_name}.{secrets.token_hex(8)}.tmp"
            try:
                descriptor = os.open(
                    temporary_name,
                    _WRITE_FLAGS,
                    0o600,
                    dir_fd=parent,
                )
                return descriptor, temporary_name
            except FileExistsError:
                continue
            except OSError as error:
                LocalState._raise_path_or_io(error, "state_write_failed")
        raise StateError("state_write_failed")

    @staticmethod
    def _raise_path_or_io(error: OSError, fallback: str) -> None:
        if error.errno in {errno.ELOOP, errno.ENOTDIR}:
            raise StateError("state_path_invalid") from None
        raise StateError(fallback) from None
