## Description:

Track water and sleep with JSON file storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aperdigaokbk](https://clawhub.ai/user/aperdigaokbk)

### License/Terms of Use:

MIT-0

## Use Case:

Users and their agents use this skill to record water intake, sleep and wake events, view simple daily statistics, and edit or delete the most recent water entry in a local JSON file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Command templates can turn user-supplied cup counts into executable JavaScript.

Mitigation: Validate cup counts as numbers and pass them as command arguments instead of inserting them into JavaScript source.

Risk: The skill stores health records locally and includes update and delete flows that can change or remove recent history.

Mitigation: Review requested changes before execution and keep a backup or export of health-data.json when the records matter.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aperdigaokbk/skills/healthcheck)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Files, Guidance]

**Output Format:** [Markdown instructions with inline bash and Node.js command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local JSON storage at {baseDir}/health-data.json and does not call external services.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and _meta.json state 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
