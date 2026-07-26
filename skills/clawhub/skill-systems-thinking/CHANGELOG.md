# Changelog

All notable changes to `systems-thinking` will be documented in this file.
Versioning follows [Semantic Versioning](https://semver.org/) in `X.Y.Z` format.

---

## [0.2.0] — 2026-07-26

### Added
- `--agents` flag to `scripts/install.js` for selecting specific agents
- `--global`, `--local`, and `--all` scope flags to control install location
- `--help` output to the install CLI

### Changed
- Default install behavior: now scans for actually installed agents (directory exists) instead of installing for all 8 agents
- `--agents` flag creates agent directories when explicitly requested
- No agents detected: prints helpful message listing available agents
- Updated `README.md` and `README_CN.md` Installation sections with new flags and auto-detection description
- Added `npm install` documentation noting it downloads only, plus explains still needing to run `npx skill-systems-thinking install`
- Removed implementation-detail paragraphs from Compatibility sections in both READMEs
- Fixed AI-sounding Chinese phrasing in README_CN.md

---

## [0.1.5] — 2026-07-25

### Changed
- Unified version numbers across documentation files to `0.1.5`
- Split `README.md` into `README.md` (English) and `README_CN.md` (Chinese) for cleaner GitHub reading experience

## [0.1.3] — 2026-07-25

### Added
- XYZ versioning convention documented in `AGENTS.md` (X=major, Y=minor, Z=patch)

### Changed
- Unified version numbers across all project files to `0.1.3`
- README.md and progress.md version tables updated from `0.1.0` to `0.1.3`
- `postinstall` script removed from `package.json` (npx-first approach)

## [0.1.2] — 2026-07-25

### Added
- Gitee download link in README.md (both 中文 and English sections)
- `repository.url` and `homepage` in `package.json` updated to point to Gitee (`gitee.com/leon0903/systems-thinking`)

## [0.1.1] — 2026-07-24

### Changed
- Fixed `repository.url` and `homepage` in `package.json` (replaced `YOUR_USERNAME` placeholder with `ShrimpLeon`)
- Expanded `keywords` from 5 to 14 for better npm search discoverability across AI agents
- Added `homepage` field to `package.json`
- Added `init.ps1` to `files` array in `package.json` so it's included in the npm package
- README.md Installation section restructured: npx one-command install as primary method, GitHub download as alternative
- Added `scripts/install.js` for npx auto-detection of AI agents and automatic symlinking
- Added `bin` field to `package.json` so `npx skill-systems-thinking install` works
- Added agent-specific setup info for 8 agents in README.md
- Added Compatibility section in both 中文 and English
- Removed npm install as a separate method; npx is the recommended approach

## [0.1.0] — 2026-07-24

### Added
- Initial public release of the skill
- SKILL.md with runtime prompt block, 7-step workflow, principle map, and 8 cognitive laws
- README.md with bilingual (中文/English) documentation
- 8 reference files: `state-and-control.md`, `stability.md`, `modeling.md`, `multivariable.md`,
  `disturbance.md`, `bounded-control.md`, `discrete-systems.md`, `closed-loop-workflow.md`
- 2 prompt templates: `debugging-checklist.md`, `change-proposal.md`
- Self-audit checklist: `evals/checks.json` with 11 MUST/SHOULD cognitive-law probes
- Harness files: `AGENTS.md`, `init.ps1`, `feature_list.json`, `progress.md`, `session-handoff.md`
- LICENSE (MIT)

### Notes
- First implementation of the thinking-mode scaffold derived from Qian Xuesen & Song Jian's
  *Engineering Cybernetics* (工程控制论).
- Language- and framework-agnostic; targets any non-trivial code change where correctness
  AND robustness must both be verified.
