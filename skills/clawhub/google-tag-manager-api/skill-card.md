## Description:

Helps agents access Google Tag Manager through Maton to manage accounts, containers, workspaces, tags, triggers, variables, permissions, and publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketing operations teams use this skill to inspect and manage Google Tag Manager containers, configure tags and workspaces, publish changes, and administer access through an authorized Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes, publishing, or permission changes could affect the wrong container or grant unintended access.

Mitigation: Default to read-only actions; confirm the exact account, container, change, and permissions before each write.

Risk: A hosted function or trigger destination can run actions or forward event data persistently.

Mitigation: Review the function, destination host, payload, and ongoing delivery behavior; obtain explicit approval before enabling them.

Risk: Long-lived credentials or secrets could be exposed through files, logs, or destination headers.

Mitigation: Prefer OAuth and credential-store authentication; never disclose keys or place provider credentials in forwarding headers.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/byungkyu/skills/google-tag-manager-api)
- [Maton](https://maton.ai)
- [Google Tag Manager API v2 documentation](https://developers.google.com/tag-platform/tag-manager/api/v2)
- [Google Tag Manager API REST reference](https://developers.google.com/tag-platform/tag-manager/api/reference/rest)
- [Scheduled trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command examples and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Maton connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata; skill frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
