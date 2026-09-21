## Description:

Paperless-ngx lets agents operate a connected Paperless-ngx account through OOMOL's oo CLI for document search, retrieval, uploads, metadata management, automation, sharing, and administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to search, read, organize, upload, update, share, and administer documents in a connected Paperless-ngx instance. It supports workflows involving document metadata, tags, notes, OCR/search results, mail processing, saved views, users, groups, workflows, and AI-assisted document features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands could install the oo CLI without review.

Mitigation: Do not allow the agent to run installer commands automatically; install or verify the oo CLI yourself before use.

Risk: The skill can perform high-impact Paperless-ngx changes, including destructive document operations, public sharing, email actions, user changes, MFA changes, and configuration updates.

Mitigation: Require explicit approval for write, destructive, public-sharing, email, user, MFA, and configuration actions.

Risk: Actions run with the connected Paperless-ngx account's permissions.

Mitigation: Use a least-privileged Paperless-ngx account and review the connected account scope before enabling the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-paperless-ngx)
- [Paperless-ngx documentation](https://docs.paperless-ngx.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect the live connector schema before execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.1 (source: evidence.release.version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
