## Description:

Drive a self-hosted gitrakz instance to sync a GitHub user's activity into local SQLite, inspect timelines and work sessions, manage deterministic templates, and export results through REST or MCP surfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install or operate a trusted self-hosted gitrakz instance, trigger GitHub activity syncs, query timelines or work sessions, and run or export templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reachable gitrakz API can expose synced GitHub activity if it is left unauthenticated or pointed at an untrusted instance.

Mitigation: Use only a trusted self-hosted instance and keep GITRAKZ_AUTH_TOKEN enabled whenever the API is reachable beyond the local machine.

Risk: GitHub syncs consume network access and rate limit budget, and require a GitHub token.

Mitigation: Use a read-scoped GitHub token and trigger sync only for the task the user requested.

Risk: Optional LLM template features can send commit titles or diffs to the configured model provider.

Mitigation: Leave LLM settings empty unless the user accepts that provider and data flow.

## Reference(s):

- [gitrakz setup](references/setup.md)
- [gitrakz project homepage](https://github.com/psyb0t/gitrakz)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/gitrakz)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON snippets, shell commands, API calls, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce CSV, PDF, or JSON export guidance for gitrakz template runs; does not emit author-supplied HTML.]

## Skill Version(s):

0.7.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
