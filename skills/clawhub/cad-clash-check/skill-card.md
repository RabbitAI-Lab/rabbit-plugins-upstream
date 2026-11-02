## Description:

Reviews DWG/DXF drawings or parsed contracts for cross-discipline 2D overlap and attribute-conflict candidates. Uses axis-grid location when available and degrades honestly when axis data is missing; outputs are human-review candidates, not BIM clash checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Developers and engineers coordinating architectural, structural, municipal, and MEP drawings can use the skill before drawing reviews to identify 2D overlap and attribute-conflict candidates. Findings require human review; the skill does not perform 3D BIM checks or provide engineering sign-off.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A helper may execute code from the working folder.

Mitigation: Use a trusted cad-file-reader installation and provide an absolute trusted --cfr path when running the building helper directly.

Risk: Incomplete axis coverage or repeated member names can hide clashes; a zero-candidate report does not establish that drawings are clear.

Mitigation: Manually verify axis coverage and repeated member names, and review the drawings even when no clashes are reported.

## Reference(s):

- [Cross-Discipline Clash Review on ClawHub](https://clawhub.ai/lisong2003-lgtm/skills/cad-clash-check)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [JSON and Markdown review reports, with a construction-plan template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Human review is required; reports are 2D candidates and do not provide quantity takeoffs or engineering sign-off.]

## Skill Version(s):

0.3.1 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
