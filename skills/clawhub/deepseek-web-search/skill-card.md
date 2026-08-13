## Description:

Use when you need up-to-date information, current events, or answers beyond your knowledge cutoff and want a synthesized answer with source URLs rather than a raw result list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mingzeng21](https://clawhub.ai/user/mingzeng21)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to answer current or time-sensitive questions through DeepSeek's server-side web search and receive a synthesized answer with consulted source URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer writes local skill files and may create a config.json containing a DeepSeek API key.

Mitigation: Review the source or use a pinned trusted copy before installing, and prefer DEEPSEEK_API_KEY or a locally protected config file for credentials.

Risk: Returned answers are model synthesis, and source URLs are pages consulted rather than per-claim citations.

Mitigation: Verify important claims against the returned source URLs before relying on or republishing the answer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mingzeng21/skills/deepseek-web-search)
- [DeepSeek Platform](https://platform.deepseek.com)
- [Node.js](https://nodejs.org/)

## Skill Output:

**Output Type(s):** [Text, JSON, API Calls, Guidance]

**Output Format:** [JSON object containing answer text, source URLs, query, model, usage, and engine metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, network access, and a DeepSeek API key; default maximum answer length is 8000 tokens with a 16384-token cap.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
