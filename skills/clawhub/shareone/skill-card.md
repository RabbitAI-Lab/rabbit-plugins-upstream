## Description:

Publishes HTML and Markdown pages or PDF, Word, and PowerPoint documents as ShareOne short links, with options to manage access, updates, downloads, and comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beep879](https://clawhub.ai/user/beep879)

### License/Terms of Use:

MIT

## Use Case:

Developers and other ShareOne users can publish agent-generated pages and documents for external sharing or team review, then manage links, access settings, downloads, and comments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated collaborator or settings operations can be steered to an untrusted URL origin.

Mitigation: Use only trusted ShareOne domains; do not pass attacker-supplied full URLs to these commands, and fix origin handling before using saved API keys with untrusted links.

Risk: Publishing private conversation content or deleting a share may disclose information or invalidate a link without a runtime confirmation gate.

Mitigation: Require explicit user confirmation before publishing private conversations or deleting any share.

## Reference(s):

- [ShareOne skill release on ClawHub](https://clawhub.ai/beep879/skills/shareone)
- [ShareOne website](https://shareone.vip)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or text with ShareOne links and operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create publicly accessible links to uploaded content.]

## Skill Version(s):

1.5.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
