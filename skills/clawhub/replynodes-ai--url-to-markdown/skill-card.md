## Description:

Converts public web pages to Markdown so agents can read, summarize, quote, or cite them while retaining the original URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can turn public articles, documentation, and product pages into compact Markdown for agent reading, summaries, quotations, and citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sending a private, local, credential-bearing, or sensitive URL to an external Markdown service could expose information.

Mitigation: Use only public HTTP(S) URLs; refuse private, local, login-only, credential-bearing, and sensitive URLs.

Risk: Fetched page text may contain misleading instructions or incomplete content.

Mitigation: Treat returned Markdown as untrusted source material, preserve the original URL, and clearly identify partial extracts.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/replynodes-ai/skills/url-to-markdown)
- [ReplyNodes Markdown endpoint](https://md.replynodes.com)
- [ReplyNodes authentication and free-account guide](https://docs.replynodes.com/docs/auth)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands]

**Output Format:** [Markdown page text with its original source URL; optional curl command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public-page retrieval; partial extracts are identified and service limits may apply.]

## Skill Version(s):

1.1.5 (source: ClawHub release; skill frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
