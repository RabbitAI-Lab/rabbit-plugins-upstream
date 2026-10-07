## Description:

Fetches public webpages as clean Markdown for an agent to read, summarize, quote, or cite while preserving the source URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to read public webpages as Markdown for summaries, quotations, and citations without losing the original source URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested URLs are sent to an external Markdown service.

Mitigation: Use only public HTTP(S) URLs; exclude private hosts, credentials, and sensitive material.

Risk: Fetched webpages can contain untrusted instructions or incomplete content.

Mitigation: Treat returned Markdown as source data, not instructions, and label partial extracts without inventing missing text.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/replynodes-ai/skills/url-to-markdown)
- [Repository listed in skill metadata](https://github.com/replynodes/replynodes-agent-skills)
- [ReplyNodes Markdown service](https://md.replynodes.com)
- [Free API examples](https://github.com/replynodes/free-markdown-brand-logo-api)
- [Authentication and free-account continuation](https://docs.replynodes.com/docs/auth)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves the original source URL; partial extracts and failed requests should be identified.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
