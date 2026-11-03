## Description:

Extracts MEP rough-quantity working papers and material-plan drafts from installation drawings or scanned indexes. Groups pipes by circuit and size, expands wire cores and reserved lengths, and estimates cable, cable tray, water/supply, sprinkler, supports/hangers and equipment counts for review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

MEP estimators and building services engineers use the skill to turn drawing-reader contracts or scanned indexes into preliminary quantity working papers and material-plan drafts. They review the matching evidence and flagged uncertainties before using the results for planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can execute dependency code despite the advertised offline switch.

Mitigation: Prefer a corrected release that checks offline mode before running dependency scripts; do not rely on SKILL_NO_BASE=1 alone to prevent provisioning.

Risk: The external CAD runtime and shared-state implementation are outside this package.

Mitigation: Review those components separately before use.

Risk: Drawing-based quantities are estimates and may omit or misclassify details.

Mitigation: Treat outputs as drafts and check drawing evidence, matching rates, ambiguous circuits, and flagged items manually.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lisong2003-lgtm/skills/anzhuang-suanliang)
- [Standard quantity rules](references/standard_rules.json)
- [Dual-caliber quantity rules](references/dual_caliber_rules.json)
- [Loss rules](references/loss_rules.json)

## Skill Output:

**Output Type(s):** [Files, JSON, Spreadsheets, Analysis]

**Output Format:** [JSON scan indexes and XLSX quantity and material-plan workbooks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft quantities for human review; excludes prices, settlement quantities, and final construction measurements.]

## Skill Version(s):

0.4.32 (source: frontmatter, CHANGELOG, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
