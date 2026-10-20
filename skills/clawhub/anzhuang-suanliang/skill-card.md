## Description:

Turns installation-engineering CAD drawings or scan indexes into preliminary quantity schedules and material-planning drafts for engineering review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Construction engineers and estimators use the skill to draft installation quantities and materials from DWG drawings or existing scan indexes, then cross-check the estimates against drawings and specialist software. Its drafts do not provide pricing or settlement quantities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can download and install a separate CAD-reading dependency into the local skills directory.

Mitigation: Install only from a trusted publisher; for tighter control, preinstall a trusted cad-file-reader and set CAD_SKILL_DIR, or use SKILL_NO_BASE=1 or CAD_AUTO_SETUP=0 where appropriate.

Risk: Using the CAD-reading dependency can execute its external validation scripts.

Mitigation: Review and trust the dependency and its scripts before enabling the workflow.

Risk: Spreadsheets generated from untrusted CAD drawings may contain formulas derived from drawing text.

Mitigation: Treat generated spreadsheets as untrusted and avoid opening them in a formula-executing environment until cell text is sanitized.

Risk: Drawing ambiguities or duplicate objects can make draft quantities incomplete or overstated.

Mitigation: Review unmatched items, confidence indicators and source drawings before using the estimates for procurement.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/anzhuang-suanliang)
- [Quantity and material mapping rules](references/dual_caliber_rules.json)
- [Standards mapping rules](references/standard_rules.json)
- [Material loss rules](references/loss_rules.json)

## Skill Output:

**Output Type(s):** [Files, Guidance]

**Output Format:** [JSON scan indexes and multi-sheet XLSX quantity and material-planning drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confidence, unmatched items and review checks; estimates require drawing-level verification and are not final billable quantities.]

## Skill Version(s):

0.4.19 (source: frontmatter, manifest, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
