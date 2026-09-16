## Description:

Qase (qase.io). Use this skill for Qase requests that read, create, or update data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and agents use this skill to operate Qase projects, test cases, and test runs through the oo CLI. It supports reading Qase data and performing confirmed state-changing actions such as creating cases, creating runs, and completing runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup recommends running downloaded installer scripts directly in a shell.

Mitigation: Prefer installing the oo CLI through a pinned, verified release or official package method, and check downloaded artifacts before execution.

Risk: Create and update actions can change Qase data.

Mitigation: Confirm the exact action, project, and payload with the user before running write actions.

## Reference(s):

- [ClawHub Qase skill page](https://clawhub.ai/oomol/skills/oo-qase)
- [Qase homepage](https://qase.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should fetch the live connector schema before sending action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
