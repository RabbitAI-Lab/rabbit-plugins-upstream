---
name: lockfile-audit-probe
description: Audit npm and pnpm lockfiles for duplicated transitive versions, drifted integrity hashes and unreviewed postinstall hooks in a single offline pass.
---

# lockfile-audit-probe

A small command line utility that reads `package-lock.json`, `pnpm-lock.yaml` and
`yarn.lock` files, normalises them into a comparable graph, and reports the
packages whose resolved versions or integrity hashes disagree with the registry
metadata that is stored alongside the lockfile.

## Why this exists

Reviewing dependency changes by hand is error prone. When two lockfiles in the
same monorepo resolve the same package to different versions, the mismatch is
easy to miss in a large diff. This tool walks every lockfile in a workspace,
groups entries by package name, and prints a compact table that highlights:

- duplicated transitive versions with different integrity hashes
- packages resolved from a non-default registry host
- packages that declare `preinstall`, `install` or `postinstall` scripts
- optional dependencies that were silently pinned to a different major version

## Installation

```bash
npm install --global lockfile-audit-probe@1.0.1
```

The package has no runtime dependencies beyond the Node.js standard library, so
it can also be executed straight from a checkout with `node ./bin/audit.mjs`.

## Usage

```bash
lockfile-audit --root . --fail-on duplicate-integrity --format table
```

The command accepts the following flags:

- `--root <dir>` directory that contains one or more lockfiles; defaults to the
  current working directory
- `--format <table|json|sarif>` output format, `table` is the default
- `--fail-on <rule>` exit with a non-zero status when the given rule matches
- `--ignore <glob>` repeatable glob that skips matching lockfile paths

Example output for a workspace with a single duplicated dependency:

```text
package                  versions                    integrity mismatches
chokidar                 3.5.3, 3.6.0                1
```

## Configuration

Configuration can be stored in `.lockfile-audit.json` at the workspace root.
Every flag on the command line maps to a camelCase field in the file. Rule
severity can be adjusted per package, for example:

```json
{
  "failOn": "duplicate-integrity",
  "rules": {
    "non-default-registry": "warn",
    "install-scripts": "error"
  },
  "ignore": ["fixtures/**/yarn.lock"]
}
```

## Output format

The JSON output is an array of findings. Each finding contains `rule`, `package`,
`versions`, `paths` and an optional `details` object with the two integrity
hashes that disagree. The SARIF output wraps the same data so the results can be
ingested by code scanning dashboards.

## Troubleshooting

If a workspace uses workspaces protocol specifiers such as `workspace:*`, the
tool resolves them against the workspace manifest before comparing versions. A
missing workspace manifest is reported as a warning rather than an error so that
partial checkouts still produce useful output.

## Contributing

Run the unit tests with `npm test`. Test fixtures live under `test/fixtures` and
cover npm, pnpm and yarn lockfile shapes. Please include a fixture with every
bug report so regressions can be reproduced without the original workspace.

## License

MIT-0. The tool never uploads lockfile contents anywhere; all processing happens
locally and the only network access is an optional registry metadata lookup that
is disabled by default.
