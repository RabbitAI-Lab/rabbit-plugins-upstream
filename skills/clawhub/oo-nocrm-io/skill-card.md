## Description:

Use this skill to read, create, update, and delete noCRM.io data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate noCRM.io leads and teams through the OOMOL oo CLI connector. It supports lead creation, duplication, assignment, tagging, description updates, lifecycle changes, deletion, and team listing with confirmation guidance for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands may execute code from external URLs during first-time setup.

Mitigation: Review installer steps before running remote scripts, and only use setup commands when the oo CLI is missing.

Risk: Write and destructive actions can create, modify, cancel, or delete noCRM.io leads.

Mitigation: Confirm the exact payload, target record, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [noCRM.io homepage](https://www.nocrm.io)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
