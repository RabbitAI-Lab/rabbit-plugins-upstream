## Description:

Operates Bazhuayu through an OOMOL-connected account so an agent can inspect schemas, run connector actions, retrieve task data, manage cloud tasks, and query task analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent work with Bazhuayu tasks through the OOMOL oo CLI, including reading task data, checking statuses, starting or stopping cloud runs, updating task settings, and querying recent task analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can start, stop, copy, or update Bazhuayu tasks and subtasks through the connected account.

Mitigation: Confirm the exact target, payload, and expected account impact before approving write or destructive actions.

Risk: The first-time setup fallback includes a remote install script for the oo CLI.

Mitigation: Use a verified oo CLI installation method when possible and avoid blindly running remote install commands.

Risk: Unexported-data acknowledgement is task-scoped and can conflict across multiple consumers.

Mitigation: Use a single sequential consumer for get_unexported_data and only call mark_data_exported after the preceding result is persisted.

## Reference(s):

- [Bazhuayu ClawHub Skill](https://clawhub.ai/oomol/skills/oo-bazhuayu)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Bazhuayu Homepage](https://www.bazhuayu.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include JSON data and execution metadata returned by the oo CLI.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
