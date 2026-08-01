# Changelog

All notable changes to `systems-thinking` will be documented in this file.
Versioning follows [Semantic Versioning](https://semver.org/) in `X.Y.Z` format.

---

## [0.3.0] — 2026-07-30

### Added
- Integrated a second source book: 金观涛《控制论与科学方法论》(*Cybernetics and Scientific Methodology*), contributing the epistemological half of the skill (possibility space, black-box recognition, information–control dependence, ultra-stability, bifurcation)
- 4 new reference files:
  - `references/possibility-space.md` — possibility space, conjugate control, feedback amplification
  - `references/black-box-epistemology.md` — black-box recognition, falsifiability, undecidability
  - `references/information-and-control.md` — information–control dependence; build the channel before the actuator
  - `references/system-evolution.md` — stable-state structure, ultra-stability, self-reproduction, bifurcation, catastrophe
- 5 new cognitive laws (total now 13): possibility space naming, missing-channel suspicion, model-as-hypothesis, falsifiability, ultra-stability/bifurcation recognition
- New `MUST`/`SHOULD` checks in `evals/checks.json` (total now 18): `possibility-space-named`, `missing-channel-suspected`, `model-falsifiable`, `ultra-stability-recognized`, `bifurcation-identified`, `threshold-tested`
- New excerpts from Book 2 in `references/original-text.md` (§1.1, §1.6, §1.7–§1.8, §2.4, §3.3, §3.7, §4.2, §5.1, §5.4, §5.6)
- `--path <dir>` flag to install into a custom directory (for agents not on the built-in list)
- Interactive install menu: scan results are listed with `[√]`/`[ ]` markers; user can pick detected / all / select-from-list / abort
- `--yes` / `-y` flag to skip confirmation prompts (implied when not a TTY)

### Changed
- `scripts/install.js` rewritten to mirror `npx impeccable skills install` UX: scan → list → confirm → link. Non-TTY environments fall back to "install for detected agents only" (CI-friendly)
- `SKILL.md` expanded: frontmatter, scope, runtime prompt block (13 laws), workflow, principle map (14 rows) now reference both books
- `references/stability.md` extended with stable-state structure, feedback overshoot, ultra-stability sections
- `references/closed-loop-workflow.md` extended with feedback amplification and convergence-rate dynamics
- `templates/debugging-checklist.md` extended with possibility space, black-box model, falsifiability, ultra-stability checks
- `init.ps1` now checks 4 additional reference files (24 total)
- Both `README.md` and `README_CN.md` rewritten in a more natural, conversational tone; listed both books, 13 laws, 12 references, and the new install UX

### Removed
- AI-sounding marketing phrases from both READMEs (e.g. "这不是给人类做的知识测试", "one-line pitch" blocks)

---

## [0.3.1] — 2026-07-30

### Removed
- `assets/runtime-prompt.txt` — redundant with the runtime prompt block already inlined in `SKILL.md`; the duplicate copy could drift out of sync (this cleanup targets the LLM pain point of "two sources of truth"). Removed the `assets/` directory, the `Source: assets/runtime-prompt.txt` line in `SKILL.md`, the `assets/` entry in `package.json` `files`, and the corresponding check in `init.ps1` (now 23 checks)

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
