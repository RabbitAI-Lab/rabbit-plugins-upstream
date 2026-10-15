## Description:

Guides Ghost publishing, newsletters, content migrations, and site audits through administrative workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[highnoonoffice](https://clawhub.ai/user/highnoonoffice)

### License/Terms of Use:

MIT-0

## Use Case:

Ghost publishers and content teams use this skill to draft and update posts, send newsletters, migrate content, and review site health and email performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting browser-based, site-wide code-injection guidance could change the live site unexpectedly.

Mitigation: Do not let an agent execute browser code-injection steps; review site-wide changes manually.

Risk: Owner or staff credentials enable elevated administrative actions beyond routine publishing.

Mitigation: Use a dedicated Ghost integration key where possible; avoid owner or staff tokens unless expressly needed.

Risk: Newsletter sends, bulk updates, and deletions can affect many subscribers or posts and may be difficult to reverse.

Mitigation: Require explicit confirmation of recipients, scope, and changes before execution.

Risk: Cron automation or webhook flows may expose subscriber data.

Mitigation: Review automation and data access before enabling these flows, and require explicit approval.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/highnoonoffice/skills/ghost-publishing-pro)
- [Project homepage (listed in metadata; provenance unverified)](https://github.com/highnoonoffice/hno-skills)
- [Ghost Admin API reference](artifact/references/api.md)
- [Publishing workflows](artifact/references/workflows.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with API request and script examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include publishing instructions, migration scripts, and audit summaries.]

## Skill Version(s):

2.6.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
