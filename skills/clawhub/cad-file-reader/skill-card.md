## Description:

Locally reads CAD and PDF drawings to extract annotated geometry, drawing semantics, discipline-specific interpretation candidates, and measurements for human review.

This skill is for research and development only.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

Engineers and drawing reviewers use this skill to inspect DWG, DXF, DWT, and PDF drawings and obtain traceable interpretation and measurement candidates. Results require review and are not final quantities, cost estimates, or design-compliance decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local drawings and cached evidence may contain sensitive project information.

Mitigation: Use trusted local workspaces, control access to drawings and caches, and review reports before sharing.

Risk: Missing runtime dependencies may trigger a first-run download.

Mitigation: Preinstall and review dependencies in restricted environments, or set CAD_AUTO_SETUP=0 to prevent automatic setup.

Risk: Cache cleanup and custom rule directories may alter local results.

Mitigation: Review the target directory and rules before using --apply cleanup or custom rule directories.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/lisong2003-lgtm/skills/cad-file-reader)
- [Capability boundaries](artifact/CAPABILITIES.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Drawing evidence and review-oriented candidate reports in Markdown, JSON, CSV, Excel, or Word]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Candidates include evidence locations, confidence, and review reasons; measurements are not final quantities.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
