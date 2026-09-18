## Description:

Use Postman through an OOMOL-connected account to read, create, update, and delete collections, requests, workspaces, environments, APIs, schemas, mock servers, monitors, webhooks, forks, and pull requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and API teams use this skill to operate Postman resources from an agent session through the OOMOL Postman connector. It supports routine read workflows as well as confirmed write and destructive changes to Postman workspaces, collections, APIs, environments, mocks, monitors, comments, forks, and pull requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Postman account, team, environment, access key, request authentication, and billing information.

Mitigation: Require explicit user confirmation before retrieving or displaying sensitive Postman resources, including for read-only actions.

Risk: The setup guidance includes a pipe-to-shell installer pattern.

Mitigation: Use a verified manual installation path for the oo CLI instead of allowing the agent to run the installer automatically.

Risk: Write and destructive actions can change or remove Postman resources.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write actions, and require explicit approval for destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-postman)
- [Postman Homepage](https://www.postman.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command output is returned as JSON when the skill uses the documented --json flag.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
