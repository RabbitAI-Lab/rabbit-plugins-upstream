## Description:

Use this skill for Formaloo requests, including reading, creating, updating, and deleting data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Formaloo connector schemas and run Formaloo form and row actions through their OOMOL-connected account. It supports listing and retrieving forms and submissions, submitting or updating row data, and deleting submitted rows after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unverified internet installer commands that could execute arbitrary code.

Mitigation: Install the oo CLI only from a verified, pinned, or manually inspected source instead of running curl-to-bash or PowerShell iex commands as written.

Risk: Write and destructive Formaloo actions can change or permanently remove form submission data.

Mitigation: Confirm the exact payload, target form or row, and expected effect with the user before running create, update, or delete actions.

Risk: Formaloo access is mediated by OOMOL-connected credentials.

Mitigation: Use the skill only when the user accepts OOMOL-mediated access and has connected the intended Formaloo account.

## Reference(s):

- [ClawHub Formaloo skill page](https://clawhub.ai/oomol/skills/oo-formaloo)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Formaloo homepage](https://www.formaloo.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
