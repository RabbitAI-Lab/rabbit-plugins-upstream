## Description:

Pipedrive helps agents read, create, update, and delete Pipedrive CRM records through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to operate Pipedrive CRM data from an agent workflow, including deals, persons, organizations, activities, pipelines, and stages. It supports read, search, create, update, and delete tasks through the OOMOL Pipedrive connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes shell commands that execute remote installer scripts directly.

Mitigation: Prefer a verified package or manual install path, inspect downloaded installer scripts before running them, and install only when the publisher and connector access are trusted.

Risk: The skill can create, update, and delete Pipedrive CRM records.

Mitigation: Confirm the exact target, payload, and expected effect before running write or destructive actions.

Risk: Using the connector grants agent workflows access to Pipedrive business data through the user's connected account.

Mitigation: Use only with an intended OOMOL-connected Pipedrive account and review connector scopes, expired credentials, and billing status before sensitive operations.

## Reference(s):

- [Pipedrive homepage](https://www.pipedrive.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pipedrive)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Pipedrive icon](https://static.oomol.com/logo/third-party/Pipedrive.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce instructions for read, write, and destructive Pipedrive connector actions; write and delete operations require user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
