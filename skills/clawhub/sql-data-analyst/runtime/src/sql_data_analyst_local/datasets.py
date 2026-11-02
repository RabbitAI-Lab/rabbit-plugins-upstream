from __future__ import annotations

import os
import secrets
import stat
from pathlib import Path, PurePosixPath
from typing import Literal
from uuid import UUID

from pydantic import Field, JsonValue, ValidationError, model_validator

from sql_data_analyst_local.contracts import StrictContract
from sql_data_analyst_local.state import LocalState, StateError


_DIRECTORY_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
_REGULAR_READ_FLAGS = os.O_RDONLY | os.O_NOFOLLOW
_REGULAR_WRITE_FLAGS = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW
_SOURCE_FORMATS = Literal["csv", "json", "jsonl", "xlsx", "parquet"]


class DatasetError(RuntimeError):
    """A stable dataset error that never includes content or local paths."""

    def __init__(self, code: str = "dataset_invalid") -> None:
        allowed = {
            "dataset_invalid",
            "dataset_too_large",
            "dataset_exists",
            "dataset_not_found",
        }
        self.code = code if code in allowed else "dataset_invalid"
        super().__init__(self.code)


class LocalColumn(StrictContract):
    name: str = Field(min_length=1, max_length=128)
    display_name: str = Field(max_length=128)
    type: str = Field(min_length=1, max_length=64)
    nullable: bool
    null_count: int = Field(ge=0)
    distinct_count: int | None = Field(default=None, ge=0)


class LocalTable(StrictContract):
    logical_name: str = Field(pattern=r"^[a-z][a-z0-9_]{0,63}$")
    display_name: str = Field(min_length=1, max_length=191)
    parquet_path: str = Field(min_length=1, max_length=256)
    row_count: int = Field(ge=0)
    columns: list[LocalColumn] = Field(max_length=200)
    profile: dict[str, JsonValue]

    @model_validator(mode="after")
    def normalized_table(self) -> "LocalTable":
        expected = f"normalized/{self.logical_name}.parquet"
        if self.parquet_path != expected:
            raise ValueError("invalid parquet path")
        names = [column.name.casefold() for column in self.columns]
        if len(names) != len(set(names)):
            raise ValueError("duplicate columns")
        if set(self.profile) != {"row_count", "column_count"}:
            raise ValueError("invalid profile fields")
        profile_rows = self.profile.get("row_count")
        profile_columns = self.profile.get("column_count")
        if type(profile_rows) is not int or profile_rows != self.row_count:
            raise ValueError("profile row count mismatch")
        if type(profile_columns) is not int or profile_columns != len(self.columns):
            raise ValueError("profile column count mismatch")
        return self


class DatasetManifest(StrictContract):
    schema_version: Literal[1]
    dataset_id: UUID
    source_format: _SOURCE_FORMATS
    source_fingerprint: str = Field(pattern=r"^[a-f0-9]{64}$")
    tables: list[LocalTable] = Field(min_length=1, max_length=20)

    @model_validator(mode="after")
    def unique_tables(self) -> "DatasetManifest":
        names = [table.logical_name for table in self.tables]
        if len(names) != len(set(names)):
            raise ValueError("duplicate tables")
        return self

    @property
    def table_map(self) -> dict[str, LocalTable]:
        return {table.logical_name: table for table in self.tables}


class _DirectoryHandle:
    def __init__(self, descriptor: int) -> None:
        self._descriptor = descriptor
        self._closed = False

    def create_file(self, name: str) -> int:
        self._check_open()
        self._component(name)
        descriptor = -1
        try:
            descriptor = os.open(
                name,
                _REGULAR_WRITE_FLAGS,
                0o600,
                dir_fd=self._descriptor,
            )
            os.fchmod(descriptor, 0o600)
            return descriptor
        except OSError:
            if descriptor >= 0:
                os.close(descriptor)
            raise DatasetError() from None

    def open_file(self, name: str) -> int:
        self._check_open()
        self._component(name)
        descriptor = -1
        try:
            descriptor = os.open(name, _REGULAR_READ_FLAGS, dir_fd=self._descriptor)
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                raise DatasetError()
            return descriptor
        except DatasetError:
            if descriptor >= 0:
                os.close(descriptor)
            raise
        except OSError:
            if descriptor >= 0:
                os.close(descriptor)
            raise DatasetError() from None

    def create_directory(self, name: str) -> "_DirectoryHandle":
        self._check_open()
        self._component(name)
        descriptor = -1
        try:
            os.mkdir(name, 0o700, dir_fd=self._descriptor)
            descriptor = os.open(name, _DIRECTORY_FLAGS, dir_fd=self._descriptor)
            os.fchmod(descriptor, 0o700)
            return _DirectoryHandle(descriptor)
        except OSError:
            if descriptor >= 0:
                os.close(descriptor)
            raise DatasetError() from None

    def unlink_file(self, name: str) -> None:
        descriptor = self.open_file(name)
        os.close(descriptor)
        try:
            os.unlink(name, dir_fd=self._descriptor)
        except OSError:
            raise DatasetError() from None

    def sync(self) -> None:
        self._check_open()
        try:
            os.fsync(self._descriptor)
        except OSError:
            raise DatasetError() from None

    def close(self) -> None:
        if not self._closed:
            descriptor = self._descriptor
            self._descriptor = -1
            self._closed = True
            os.close(descriptor)

    def __enter__(self) -> "_DirectoryHandle":
        self._check_open()
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    @property
    def descriptor(self) -> int:
        self._check_open()
        return self._descriptor

    def _check_open(self) -> None:
        if self._closed:
            raise DatasetError()

    @staticmethod
    def _component(name: str) -> None:
        if (
            not isinstance(name, str)
            or not name
            or name in {".", ".."}
            or "/" in name
            or "\x00" in name
        ):
            raise DatasetError()


class _DatasetStage(_DirectoryHandle):
    def __init__(
        self,
        repository: "DatasetRepository",
        dataset_id: UUID,
        datasets_descriptor: int,
        temporary_name: str,
        stage_descriptor: int,
    ) -> None:
        super().__init__(stage_descriptor)
        self._repository = repository
        self._dataset_id = dataset_id
        self._datasets_descriptor = datasets_descriptor
        self.temporary_name = temporary_name
        self._commit_state = "staging"

    def commit(self) -> None:
        self._check_open()
        if self._commit_state != "staging":
            raise DatasetError()
        self._repository._assert_same_datasets(self._datasets_descriptor)
        target = str(self._dataset_id)
        try:
            try:
                os.stat(
                    target,
                    dir_fd=self._datasets_descriptor,
                    follow_symlinks=False,
                )
            except FileNotFoundError:
                pass
            else:
                raise DatasetError("dataset_exists")
            os.rename(
                self.temporary_name,
                target,
                src_dir_fd=self._datasets_descriptor,
                dst_dir_fd=self._datasets_descriptor,
            )
            self._commit_state = "renamed"
            try:
                self._repository._assert_same_datasets(
                    self._datasets_descriptor,
                    matched_close_best_effort=True,
                )
            except DatasetError:
                self._rollback_renamed()
                raise
            self._commit_state = "published"
        except DatasetError:
            raise
        except OSError:
            raise DatasetError() from None

        # Rename is the publication/commit point. A later directory fsync error
        # cannot be reported as an ingest failure while the UUID is visible.
        try:
            os.fsync(self._datasets_descriptor)
        except OSError:
            pass

    def abort(self) -> None:
        self._check_open()
        if self._commit_state == "published":
            return
        if self._commit_state != "staging":
            raise DatasetError()
        try:
            self._repository._validate_tree(self.descriptor)
            self._repository._remove_open_tree(self.descriptor)
            os.rmdir(self.temporary_name, dir_fd=self._datasets_descriptor)
        except DatasetError:
            raise
        except OSError:
            raise DatasetError() from None

    def _rollback_renamed(self) -> None:
        if self._commit_state != "renamed":
            raise DatasetError()
        target = str(self._dataset_id)
        try:
            # The stage descriptor remains open across rename. Clean through it
            # so a workspace path swap cannot redirect or prevent rollback.
            self._repository._validate_tree(self.descriptor)
            self._repository._remove_open_tree(self.descriptor)
            os.rmdir(target, dir_fd=self._datasets_descriptor)
            self._commit_state = "rolled_back"
            os.fsync(self._datasets_descriptor)
        except DatasetError:
            raise
        except OSError:
            raise DatasetError() from None

    def close(self) -> None:
        published = self._commit_state == "published"
        close_failed = False
        try:
            super().close()
        except OSError:
            close_failed = True
        if self._datasets_descriptor >= 0:
            descriptor = self._datasets_descriptor
            self._datasets_descriptor = -1
            try:
                os.close(descriptor)
            except OSError:
                close_failed = True
        self._commit_state = "closed"
        if close_failed and not published:
            raise DatasetError() from None

    def __exit__(self, *args: object) -> None:
        try:
            if self._commit_state == "staging":
                self.abort()
            elif self._commit_state == "renamed":
                self._rollback_renamed()
        finally:
            self.close()


class DatasetRepository:
    def __init__(self, workspace_root: Path) -> None:
        try:
            self._state = LocalState(workspace_root)
            descriptor = self._state._open_parent(  # noqa: SLF001
                ("datasets", ".directory"), create=True
            )
        except StateError:
            raise DatasetError() from None
        else:
            os.close(descriptor)
        self.workspace_root = self._state.root
        self.datasets_root = self.workspace_root / "datasets"

    def dataset_path(self, dataset_id: UUID) -> Path:
        return self.datasets_root / self._dataset_name(dataset_id)

    def inspect(self, dataset_id: UUID) -> DatasetManifest:
        name = self._dataset_name(dataset_id)
        try:
            value = self._state.read_json(f"datasets/{name}/manifest.json")
            if value is None:
                raise DatasetError("dataset_not_found")
            manifest = DatasetManifest.model_validate(value)
            if manifest.dataset_id != dataset_id:
                raise DatasetError()
            self._validate_manifest_files(manifest)
            return manifest
        except DatasetError:
            raise
        except (StateError, ValidationError, TypeError, ValueError):
            raise DatasetError() from None

    def table_path(self, dataset_id: UUID, table: LocalTable) -> Path:
        name = self._dataset_name(dataset_id)
        if not isinstance(table, LocalTable):
            raise DatasetError()
        expected = PurePosixPath("normalized") / f"{table.logical_name}.parquet"
        if PurePosixPath(table.parquet_path) != expected:
            raise DatasetError()
        return self.datasets_root / name / Path(*expected.parts)

    def _open_table_file(self, dataset_id: UUID, table: LocalTable) -> int:
        """Open a normalized table without resolving any workspace path."""
        if not isinstance(table, LocalTable):
            raise DatasetError()
        expected = PurePosixPath("normalized") / f"{table.logical_name}.parquet"
        if PurePosixPath(table.parquet_path) != expected:
            raise DatasetError()
        dataset = self._open_dataset(dataset_id)
        normalized = -1
        descriptor = -1
        try:
            normalized = os.open("normalized", _DIRECTORY_FLAGS, dir_fd=dataset)
            descriptor = os.open(
                f"{table.logical_name}.parquet",
                _REGULAR_READ_FLAGS,
                dir_fd=normalized,
            )
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                raise DatasetError()
            result = descriptor
            descriptor = -1
            return result
        except DatasetError:
            raise
        except OSError as error:
            self._raise_os_error(error)
        finally:
            if descriptor >= 0:
                os.close(descriptor)
            if normalized >= 0:
                os.close(normalized)
            os.close(dataset)
        raise DatasetError()

    def delete(self, dataset_id: UUID) -> None:
        name = self._dataset_name(dataset_id)
        datasets = self._open_datasets(create=False)
        child = -1
        try:
            try:
                metadata = os.stat(name, dir_fd=datasets, follow_symlinks=False)
            except FileNotFoundError:
                return
            except OSError as error:
                self._raise_os_error(error)
            if not stat.S_ISDIR(metadata.st_mode):
                raise DatasetError()
            try:
                child = os.open(name, _DIRECTORY_FLAGS, dir_fd=datasets)
            except OSError as error:
                self._raise_os_error(error)
            self._validate_tree(child)
            os.close(child)
            child = -1
            self._remove_tree(datasets, name)
            os.fsync(datasets)
        except DatasetError:
            raise
        except OSError:
            raise DatasetError() from None
        finally:
            if child >= 0:
                os.close(child)
            os.close(datasets)

    def _begin_staging(self, dataset_id: UUID) -> _DatasetStage:
        target = self._dataset_name(dataset_id)
        datasets = self._open_datasets(create=True)
        temporary: str | None = None
        stage = -1
        try:
            try:
                os.stat(target, dir_fd=datasets, follow_symlinks=False)
            except FileNotFoundError:
                pass
            except OSError as error:
                self._raise_os_error(error)
            else:
                raise DatasetError("dataset_exists")
            for _ in range(16):
                temporary = f".{target}.{secrets.token_hex(8)}.tmp"
                try:
                    os.mkdir(temporary, 0o700, dir_fd=datasets)
                except FileExistsError:
                    continue
                except OSError as error:
                    self._raise_os_error(error)
                try:
                    stage = os.open(temporary, _DIRECTORY_FLAGS, dir_fd=datasets)
                    os.fchmod(stage, 0o700)
                    os.fsync(datasets)
                    return _DatasetStage(
                        self,
                        dataset_id,
                        datasets,
                        temporary,
                        stage,
                    )
                except BaseException as error:
                    if stage >= 0:
                        os.close(stage)
                        stage = -1
                    try:
                        os.rmdir(temporary, dir_fd=datasets)
                    except OSError:
                        raise DatasetError() from None
                    if isinstance(error, DatasetError):
                        raise
                    if isinstance(error, OSError):
                        raise DatasetError() from None
                    raise
            raise DatasetError()
        except BaseException:
            if stage >= 0:
                os.close(stage)
            os.close(datasets)
            raise

    def _assert_same_datasets(
        self,
        expected_descriptor: int,
        *,
        matched_close_best_effort: bool = False,
    ) -> None:
        current = self._open_datasets(create=False)
        matched = False
        try:
            try:
                expected = os.fstat(expected_descriptor)
                actual = os.fstat(current)
            except OSError:
                raise DatasetError() from None
            if (expected.st_dev, expected.st_ino) != (actual.st_dev, actual.st_ino):
                raise DatasetError()
            matched = True
        finally:
            try:
                os.close(current)
            except OSError:
                if not (matched and matched_close_best_effort):
                    raise DatasetError() from None

    def _validate_manifest_files(self, manifest: DatasetManifest) -> None:
        dataset = self._open_dataset(manifest.dataset_id)
        normalized = -1
        descriptor = -1
        try:
            normalized = os.open("normalized", _DIRECTORY_FLAGS, dir_fd=dataset)
            for table in manifest.tables:
                expected = f"{table.logical_name}.parquet"
                descriptor = os.open(expected, _REGULAR_READ_FLAGS, dir_fd=normalized)
                if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                    raise DatasetError()
                os.close(descriptor)
                descriptor = -1
        except DatasetError:
            raise
        except OSError as error:
            self._raise_os_error(error)
        finally:
            if descriptor >= 0:
                os.close(descriptor)
            if normalized >= 0:
                os.close(normalized)
            os.close(dataset)

    def _open_dataset(self, dataset_id: UUID) -> int:
        datasets = self._open_datasets(create=False)
        try:
            return os.open(
                self._dataset_name(dataset_id), _DIRECTORY_FLAGS, dir_fd=datasets
            )
        except OSError as error:
            self._raise_os_error(error)
        finally:
            os.close(datasets)
        raise DatasetError()

    def _open_datasets(self, *, create: bool) -> int:
        try:
            return self._state._open_parent(  # noqa: SLF001
                ("datasets", ".directory"), create=create
            )
        except (StateError, FileNotFoundError):
            raise DatasetError() from None

    @classmethod
    def _validate_tree(cls, descriptor: int) -> None:
        for entry in os.listdir(descriptor):
            metadata = os.stat(entry, dir_fd=descriptor, follow_symlinks=False)
            if stat.S_ISREG(metadata.st_mode):
                continue
            if not stat.S_ISDIR(metadata.st_mode):
                raise DatasetError()
            child = os.open(entry, _DIRECTORY_FLAGS, dir_fd=descriptor)
            try:
                cls._validate_tree(child)
            finally:
                cls._close_best_effort(child)

    @classmethod
    def _remove_tree(cls, parent: int, name: str) -> None:
        child = os.open(name, _DIRECTORY_FLAGS, dir_fd=parent)
        try:
            for entry in os.listdir(child):
                metadata = os.stat(entry, dir_fd=child, follow_symlinks=False)
                if stat.S_ISDIR(metadata.st_mode):
                    cls._remove_tree(child, entry)
                elif stat.S_ISREG(metadata.st_mode):
                    os.unlink(entry, dir_fd=child)
                else:
                    raise DatasetError()
        finally:
            os.close(child)
        os.rmdir(name, dir_fd=parent)

    @classmethod
    def _remove_open_tree(cls, descriptor: int) -> None:
        for entry in os.listdir(descriptor):
            metadata = os.stat(entry, dir_fd=descriptor, follow_symlinks=False)
            if stat.S_ISDIR(metadata.st_mode):
                child = os.open(entry, _DIRECTORY_FLAGS, dir_fd=descriptor)
                try:
                    cls._remove_open_tree(child)
                finally:
                    cls._close_best_effort(child)
                os.rmdir(entry, dir_fd=descriptor)
            elif stat.S_ISREG(metadata.st_mode):
                os.unlink(entry, dir_fd=descriptor)
            else:
                raise DatasetError()

    @staticmethod
    def _dataset_name(dataset_id: UUID) -> str:
        if not isinstance(dataset_id, UUID):
            raise DatasetError()
        return str(dataset_id)

    @staticmethod
    def _raise_os_error(error: OSError) -> None:
        del error
        raise DatasetError() from None

    @staticmethod
    def _close_best_effort(descriptor: int) -> None:
        try:
            os.close(descriptor)
        except OSError:
            pass
