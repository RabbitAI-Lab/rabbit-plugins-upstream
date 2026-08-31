## Description:

Ghost Publishing Pro helps agents publish, audit, migrate, analyze, and automate Ghost CMS sites through Admin API workflows for posts, newsletters, batch imports, site health, excerpts, and indexing repair.

This skill is ready for commercial/non-commercial use.

## Publisher:

[highnoonoffice](https://clawhub.ai/user/highnoonoffice)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and publishers use this skill to manage Ghost CMS publishing workflows from an agent, including drafting, updating, scheduling, newsletter sending, migration, SEO repair, and site audits. It is intended for users who can provide Ghost Admin API credentials and review live-site changes before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide live publishing, newsletter sends, and bulk content changes that may be difficult to reverse.

Mitigation: Require explicit confirmation of the content, subscriber segment, post count, and intended changes before publishing, emailing, or running bulk operations.

Risk: Ghost Admin credentials or owner-level tokens can expose privileged site operations.

Mitigation: Use a dedicated, revocable Ghost integration key where possible, protect the credentials file, avoid owner tokens unless a task specifically requires them, and never place Admin keys in client-side code.

Risk: The security summary notes behavior beyond the stated Admin API-only scope, including browser code injection, external webhook/data sharing, persistent automation, and broader credentials.

Mitigation: Do not allow autonomous browser code injection or settings changes; enable webhooks, cron publishing, or external sharing only after scoping events, payloads, authentication, review, and rollback procedures.

Risk: Ghost API constraints such as token expiry, optimistic locking, rate limits, and one-shot email sends can cause failed or unintended partial operations.

Mitigation: Regenerate short-lived tokens as needed, fetch fresh updated_at values before updates, add delays to batch operations, and verify results after each high-impact workflow.

## Reference(s):

- [Ghost Admin API Reference](references/api.md)
- [Ghost Publishing Workflows](references/workflows.md)
- [ClawHub skill page](https://clawhub.ai/highnoonoffice/skills/ghost-publishing-pro)
- [Project homepage](https://github.com/highnoonoffice/hno-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with inline shell commands, JSON payloads, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Ghost Admin API requests that create, update, publish, schedule, email, audit, or migrate site content.]

## Skill Version(s):

2.5.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
