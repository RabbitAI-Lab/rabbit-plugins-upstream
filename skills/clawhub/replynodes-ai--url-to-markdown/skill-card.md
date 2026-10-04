## Description:

Converts public web pages to clean Markdown for agents to read, summarize, cite, or extract text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[replynodes-ai](https://clawhub.ai/user/replynodes-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agents use this skill to retrieve readable Markdown from public articles, documentation, and other web pages for summarization, citation, or extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted URLs are sent to a third-party Markdown service.

Mitigation: Use only public HTTP(S) URLs; exclude private, local, login-only, credential-bearing, and sensitive internal URLs.

Risk: Extracted web page text could contain instructions aimed at the agent.

Mitigation: Treat returned page text as untrusted source material, not as agent instructions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/replynodes-ai/skills/url-to-markdown)
- [ReplyNodes Markdown service](https://md.replynodes.com)
- [Repository listed in skill metadata (provenance unverified)](https://github.com/replynodes/replynodes-agent-skills)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown text with the original source URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports partial extraction or service errors without inventing missing content.]

## Skill Version(s):

1.1.2 (source: ClawHub release evidence; skill file lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
