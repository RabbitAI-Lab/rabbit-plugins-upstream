## Description:

This skill handles Indeed (indeed.com) requests involving reading, updating, or clearing data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Indeed through an OOMOL-connected account, including reading employer job data and updating or clearing sourced job posting information with confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Review and verify the installer distribution path before running downloaded installer scripts.

Risk: Write and destructive Indeed actions can change or clear job posting data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [Indeed homepage](https://www.indeed.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-indeed)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schema inspection before action execution; connector responses are JSON when run with --json.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
