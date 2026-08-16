## Description:

Use this skill for ProcessPlan requests at processplan.com, including reading, creating, and updating data through the OOMOL ProcessPlan connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate ProcessPlan through an OOMOL-connected account. It supports reading pending tasks, process instances, and templates, and starting a new ProcessPlan process after reviewing the payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can start a ProcessPlan process, which changes ProcessPlan state.

Mitigation: Confirm the exact payload and expected effect with the user before running the write action.

Risk: The skill depends on OOMOL's oo CLI and the permissions of the connected ProcessPlan account.

Mitigation: Before installation, confirm the user trusts OOMOL's oo CLI and that the connected account has appropriate permissions.

## Reference(s):

- [ProcessPlan homepage](https://processplan.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON from connector actions when commands are run with --json.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
