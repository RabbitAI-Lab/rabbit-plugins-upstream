# Conventional Commits Reference

## Specification

The Conventional Commits specification is a lightweight convention on top of commit messages.
It provides an easy set of rules for creating an explicit commit history, making it easier
to write automated tools on top of it.

## Core Format

```
<type>[optional scope][!]: <description>

[optional body]

[optional footer(s)]
```

## Types (required)

- `feat:` → a new feature (correlates with MINOR in SemVer)
- `fix:` → a bug fix (correlates with PATCH in SemVer)

## Breaking Changes

A `!` after the type/scope or `BREAKING CHANGE:` in the body/footer indicates a breaking API change (correlates with MAJOR in SemVer).

## Examples

### Commit message with description and breaking change footer
```
feat: allow provided config object to extend other configs

BREAKING CHANGE: `extends` key in config file is now used for extending other config files
```

### Commit message with ! to draw attention to breaking change
```
feat(api)!: send an email to the customer when a product is shipped
```

### Commit message with scope and !
```
feat(api)!: drop support for v1 endpoints

Refs: #123
```

## FAQ

**Why use Conventional Commits?**
- Automatically generate CHANGELOGs
- Automatically determine SemVer version bumps
- Communicate the nature of changes to teammates/public
- Trigger build and publish pipelines
- Make commit history easier to read

## Parsers

Tools that can parse Conventional Commits:
- Node.js: `conventional-changelog-cli`, `commitlint`
- Python: `commitizen`
- Go: `conventional-commits-parser`
