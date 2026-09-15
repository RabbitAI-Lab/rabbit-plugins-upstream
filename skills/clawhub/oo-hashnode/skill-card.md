## Description:

Hashnode (hashnode.com). Use this skill for Hashnode requests, including reading, creating, updating, publishing, and deleting content through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and publishing teams use this skill to manage Hashnode profiles, publications, posts, and drafts from an agent via an OOMOL-connected Hashnode account. It supports read operations and content-changing workflows such as creating drafts, publishing posts, updating content, and deleting drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute unverified code.

Mitigation: Prefer a verified installer or official installation guide with checksum or signature validation before running setup commands.

Risk: The OOMOL CLI and Hashnode connector operate with access to the connected Hashnode account.

Mitigation: Install only when that account access is acceptable, and keep credentials scoped and revocable through the connected-account provider.

Risk: Write and destructive actions can publish, update, delete, or overwrite Hashnode content.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before running write or destructive connector actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hashnode)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Hashnode homepage](https://hashnode.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Markdown, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Hashnode connector schema inspection before payload construction; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
