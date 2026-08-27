## Description:

Operates Happy Scribe through the OOMOL-connected happy_scribe connector for reading, creating, updating, and deleting transcription-related data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Happy Scribe accounts through OOMOL for organization, transcription, order, export, translation, and cleanup workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and destructive connector actions can change or delete Happy Scribe account data.

Mitigation: Confirm the exact payload, target IDs, and intended effect with the user before write actions, and require explicit approval before destructive deletion.

Risk: Order confirmation and job creation can affect billing-related workflows.

Mitigation: Review order details, job parameters, and user intent before confirming orders or creating transcription, translation, or export jobs.

## Reference(s):

- [Happy Scribe ClawHub skill page](https://clawhub.ai/oomol/skills/oo-happy-scribe)
- [Happy Scribe homepage](https://www.happyscribe.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command results are JSON objects with data and meta.executionId when actions run.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
