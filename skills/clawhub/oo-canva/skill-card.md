## Description:

Enables an agent to operate Canva through the OOMOL oo CLI connector for reading, creating, exporting, uploading, organizing, and moving Canva resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent work with Canva designs, assets, folders, exports, and upload jobs through a connected OOMOL account. It supports both read-only discovery and user-confirmed write actions such as creating designs, folders, exports, uploads, and item moves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can execute a remotely downloaded oo CLI installer without verification.

Mitigation: Review the installer source and prefer a verified official release or package manager before installation.

Risk: Write actions can change Canva state by creating designs, creating folders, starting exports or uploads, or moving items.

Mitigation: Require explicit user approval for the exact action, payload, and expected effect before running any write action.

Risk: The skill depends on an authenticated OOMOL-connected Canva account and may fail when authorization, scopes, billing, or credentials are unavailable.

Mitigation: Only perform setup or reconnection steps after a matching command failure and resolve account, scope, or billing errors before retrying.

## Reference(s):

- [Canva homepage](https://www.canva.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-canva)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Canva connector calls that return JSON data and asynchronous job handles.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
