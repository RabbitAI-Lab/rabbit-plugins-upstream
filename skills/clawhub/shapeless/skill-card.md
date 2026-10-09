## Description:

Helps users draft, schedule, and publish social posts and manage Shapeless content jobs, standing agents, and Brand Memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[firstclasstree](https://clawhub.ai/user/firstclasstree)

### License/Terms of Use:

MIT-0

## Use Case:

People managing a connected Shapeless account use this skill to prepare and review social content, schedule or publish posts, monitor content jobs, and maintain their brand voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account actions can approve or publish posts, wake standing agents, or persist changes to Brand Memory.

Mitigation: Review affected content and require explicit user confirmation before each live or durable action.

Risk: An unpinned CLI fallback or exposed API key could compromise a connected social account.

Mitigation: Prefer OAuth or a trusted, pinned CLI installation and protect API keys.

## Reference(s):

- [Shapeless skill on ClawHub](https://clawhub.ai/firstclasstree/skills/shapeless)
- [Shapeless documentation](https://shapelessai.com/docs)
- [Shapeless posts documentation](https://shapelessai.com/docs/posts.md)
- [Shapeless jobs documentation](https://shapelessai.com/docs/jobs.md)
- [Shapeless Brand Memory documentation](https://shapelessai.com/docs/brand-memory.md)
- [Shapeless API documentation](https://shapelessai.com/docs/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown with optional commands and account-action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create or update posts, content jobs, standing agents, and durable Brand Memory in a connected account.]

## Skill Version(s):

1.0.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
