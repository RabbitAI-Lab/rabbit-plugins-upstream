# Changelog

## 1.1.5

- Restore the public display name to Excalidraw Diagrams for Obsidian. Drawing behavior is unchanged.

## 1.1.4

- Condense workflow and remove redundant format questions while retaining the complete spec, reciprocal bindings, overwrite scope and compressed-validation limits.

## 1.1.3

- Condense instructions and reconcile generated versus manual layouts and existing overwrite authorization.
- Reject malformed geometry/bindings and invalid UTF-8 without crashing. Check frontmatter placement and reciprocal arrow references.
- Clarify compressed-file validation limits and supported cycles versus self-loops.

## 1.1.2

- Licensed under MIT-0 (MIT No Attribution), declared in the SKILL.md frontmatter and a LICENSE file. No code changes.

## 1.1.1

- Sharper description and README, plus links to the author's other skills and site. No code changes.

## 1.1.0 (unreleased)

- New `scripts/build_diagram.py`. It builds a drawing from a JSON spec of nodes, edges and groups. It does the layered layout (with cycle support and detours around nodes), label sizing, two-way text and arrow bindings and deterministic IDs, and writes either the Obsidian or the standard format. It refuses to overwrite without `--force`.
- New `scripts/validate.py`, which checks structure, bindings, fonts, font sizes and overlapping shapes.
- `SKILL.md` and `references/excalidraw-format.md` now agree with each other. Fixed the "Default" mode contradiction and the `frameId`/`versionNonce`/`updated` rules, documented `fontFamily` 5 (Excalifont) and the other current fonts, and populated `## Text Elements` in Obsidian files. The 1200x800 canvas limit is gone.
- Narrowed the description to explicit Excalidraw requests, per the ClawHub security audit (Vague Triggers).
- Examples, unit tests and GitHub Actions CI.

## 1.0.x

- Initial release, then a removed hard-coded personal path and a confirmation step before saving or overwriting files.
