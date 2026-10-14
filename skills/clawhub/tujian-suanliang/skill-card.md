## Description:

Estimates concrete quantities and reinforcing-steel ranges from structural DWG/DXF drawings for floor-by-floor and pouring-zone material plans, with drawing-based checks and separate post-pour strip accounting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Construction planners and engineers use this skill to estimate floor-level concrete orders and reinforcing-steel ranges from structural drawings, including concrete grade breakdowns and post-pour strip quantities. Estimates support material planning, not rebar detailing, final measurement, or settlement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may fetch the cad-file-reader dependency from GitHub.

Mitigation: Review the dependency before installation, or disable automatic setup with SKILL_NO_BASE=1 or CAD_AUTO_SETUP=0.

Risk: Local .cadidx caches and report files can retain drawing-derived project data.

Mitigation: Choose a controlled location with --cache-dir and remove caches and reports when retention is no longer needed.

Risk: Planning-level quantity estimates may be mistaken for precise takeoffs or settlement figures.

Mitigation: Check assumptions and quantities against the drawings; do not use estimates for rebar detailing, final measurement, or settlement.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/lisong2003-lgtm/skills/tujian-suanliang)
- [Skill usage and estimation limits](README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown reports, CSV and JSON tables, and optional XLSX workbooks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Planning estimates include net and loss-adjusted concrete quantities, grade breakdowns, and reinforcing-steel ranges; they are not final takeoffs.]

## Skill Version(s):

0.9.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
