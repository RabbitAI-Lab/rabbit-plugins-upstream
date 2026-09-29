<!-- CHANGELOG 模板。骨架+占位符；条目风格按 oss-voice §4（一行一条、面向用户效果、破坏性变更入 Breaking Changes）执行，不在此复制。 -->

# Changelog

All notable changes to {{project_name}} are documented in this file.

## [Unreleased]

### Added

- {{unreleased_added_item}}

## [{{latest_version}}] - {{date}}

### Added

- {{added_item_1}} <!-- 写用户可感知的效果，如 "members can scope docs per project"，不写 "修改 pull.ts" -->

### Changed

- {{changed_item_1}}

### Breaking Changes

- {{breaking_item_1}} <!-- 写清谁受影响 + 迁移口径，如 "every pull fails until the entry and its directory are renamed together; run {{migration_cmd}}" -->

[Unreleased]: https://github.com/{{repo_owner}}/{{project_name}}/compare/{{latest_version}}...HEAD
[{{latest_version}}]: https://github.com/{{repo_owner}}/{{project_name}}/releases/tag/{{latest_version}}
