## Description:

Use this skill to operate Qingflow through OOMOL's oo CLI, including reading workspace data and performing confirmed record lifecycle actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and operations teams use this skill to inspect Qingflow workspace structures, forms, records, comments, change logs, and workflow logs, and to perform approved record updates or workflow actions through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote install scripts for the oo CLI, which can execute high-impact local code if run without verification.

Mitigation: Review the oo CLI installation path before use, prefer a verified package-manager or signed installer when available, and do not allow an agent to run the remote install script automatically.

Risk: Qingflow write and destructive actions can change records, workflow state, comments, or reminders in the connected workspace.

Mitigation: Before approving those actions, confirm the exact workspace, application, record, payload, and expected effect with the user.

Risk: Using stale assumptions about Qingflow action inputs can produce incorrect payloads or failed operations.

Mitigation: Fetch the live action schema with oo connector schema before constructing payloads for Qingflow actions.

## Reference(s):

- [Qingflow skill on ClawHub](https://clawhub.ai/oomol/skills/oo-qingflow)
- [Qingflow homepage](https://qingflow.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON payload examples, and configuration links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses from the Qingflow connector, including data and execution metadata.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
