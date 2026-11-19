## Description:

Use the WordPress command-line tool to read and manage a user's self-hosted site, draft or publish posts, and work with supported WordPress APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site owners use this skill to inspect WordPress content and manage posts, including drafting, updating, scheduling, publishing, unpublishing, and moving posts to trash. It also supports selected WordPress API operations such as working with media, comments, and menus.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delete actions can remove site content, and scan coverage is incomplete.

Mitigation: Review each delete target before execution and use the trash unless permanent deletion was explicitly requested.

## Reference(s):

- [WordPress API reference](references/api.md)
- [ClawHub release page](https://clawhub.ai/wirecat/skills/wirecat-wordpress)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Markdown, Guidance]

**Output Format:** [JSON responses and Markdown content, with shell commands and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Site changes depend on the selected profile's permissions; publishing can make content public immediately.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
