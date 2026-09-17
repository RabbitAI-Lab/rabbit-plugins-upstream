## Description:

Basin lets agents read, create, update, and delete Basin projects, forms, webhooks, and submissions through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Basin projects, forms, webhooks, and submissions from an agent session while relying on OOMOL-managed credentials. It supports routine reads and user-confirmed create, update, and delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes running an internet-hosted installer directly in a shell.

Mitigation: Install only after reviewing the official install guide, downloading installers separately when appropriate, and verifying publisher and version details before execution.

Risk: Create, update, and delete actions can change or remove Basin data.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub Basin skill listing](https://clawhub.ai/oomol/skills/oo-basin)
- [Basin homepage](https://usebasin.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions return JSON responses from the oo connector when executed with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
