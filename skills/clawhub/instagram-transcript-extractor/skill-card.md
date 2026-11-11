## Description:

Extract spoken transcripts from one or more public Instagram video or Reel links, and summarize, translate, or analyze the resulting text when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apismith-labs](https://clawhub.ai/user/apismith-labs)

### License/Terms of Use:

MIT-0

## Use Case:

External users can request the spoken transcript of a public Instagram video or Reel, then use the returned text for a summary, translation, or analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Transcript retrieval uses network-capable Apify tooling, and the security scan does not establish how the host enforces tool permissions.

Mitigation: Use the connected Apify tool only after its availability, authorization, and Actor schema are confirmed; never share credentials in chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apismith-labs/skills/instagram-transcript-extractor)
- [Project installation guide](https://github.com/apismith-labs/instagram-ai-agent-skills#install-by-platform)
- [Example requests](https://github.com/apismith-labs/instagram-ai-agent-skills#instagram-transcript-extractor)
- [Apify MCP setup](https://docs.apify.com/mcp)
- [Apify Instagram transcripts Actor](https://apify.com/apple_yang/instagram-transcripts-scraper)
- [Workflow reference](references/workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript text is returned as received; timestamps are included only when returned. Multi-link processing depends on host batch support.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
