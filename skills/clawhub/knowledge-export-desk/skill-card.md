## Description:

Plan knowledge-base placement and write workspace export files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge-base maintainers use this skill to choose a workspace path for notes, reports, or knowledge-base articles and to record an export file at the selected path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The write stage may create or modify a local workspace export file at the selected path.

Mitigation: Confirm the intended workspace path before invoking the write stage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/knowledge-export-desk)

## Skill Output:

**Output Type(s):** [Text, Files, Configuration]

**Output Format:** [Plain text path strings and structured recorded-path objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify a local workspace export file when the write stage is requested.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
