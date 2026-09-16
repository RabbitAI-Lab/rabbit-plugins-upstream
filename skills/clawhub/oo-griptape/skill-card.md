## Description:

Griptape lets agents operate Griptape Cloud through an OOMOL-connected account, including assistant, run, event, and organization actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Griptape connector schemas, run Griptape Cloud actions through the oo CLI, and manage assistants, runs, events, and organizations from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Review the install path before use, prefer a verified package or inspected installer, and avoid running remote shell pipelines directly.

Risk: The skill can perform account-changing Griptape Cloud actions, including writes and assistant deletion.

Mitigation: Confirm every write or delete action against the exact Griptape resource and payload before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-griptape)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Griptape Homepage](https://www.griptape.ai)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Skill Icon](https://static.oomol.com/logo/third-party/griptape.svg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI commands that perform read, write, or destructive Griptape Cloud actions after schema inspection and user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
