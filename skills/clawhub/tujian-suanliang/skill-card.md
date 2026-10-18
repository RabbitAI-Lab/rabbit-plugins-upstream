## Description:

Estimates concrete quantities and reinforcement ranges from structural DWG/DXF drawings by floor and pour zone for material planning.

This skill is for research and development only.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Construction planners and engineers use this skill to prepare floor- and pour-zone material estimates, including concrete grade breakdowns and reinforcement ranges. Results are planning estimates, not measurements for detailing, ordering cut lengths, or settlement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may fetch, install and execute an external CAD reader dependency.

Mitigation: Review and preinstall the dependency before use, or disable automatic setup with SKILL_NO_BASE=1 and CAD_AUTO_SETUP=0 where appropriate.

Risk: Generated reports may contain project paths and drawing-derived details.

Mitigation: Review reports and remove sensitive project information before sharing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lisong2003-lgtm/skills/tujian-suanliang)
- [Skill README](README.md)
- [Quantity pipeline guidance](packs/quantity-pipeline/SKILL.md)
- [Quantity rules](rules/口径.json)

## Skill Output:

**Output Type(s):** [Markdown, CSV, JSON, Spreadsheets, Guidance]

**Output Format:** [Markdown, CSV, JSON and XLSX reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes planning quantities, estimated reinforcement ranges and missing-input or review notes.]

## Skill Version(s):

0.9.18 (source: SKILL.md frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
