## Description:

Extract spoken transcripts from one or more public Instagram video or Reel links, and summarize, translate, or analyze the resulting text when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apismith-labs](https://clawhub.ai/user/apismith-labs)

### License/Terms of Use:

MIT-0

## Use Case:

External users can retrieve spoken transcripts from public Instagram videos and Reels, then request summaries, translations, or analysis grounded in the returned text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review notes network capability without a declared tool scope.

Mitigation: Use the host's approved Apify connection and review the permissions it grants before execution.

Risk: The security review flags output handling, and transcript availability and timestamps depend on returned data.

Mitigation: Check returned content against host output limits, and do not invent missing transcript text or timestamps.

## Reference(s):

- [Workflow reference](references/workflow.md)
- [Installation guide](https://github.com/apismith-labs/instagram-ai-agent-skills#install-by-platform)
- [Apify MCP setup](https://docs.apify.com/mcp)
- [Instagram transcripts Actor](https://apify.com/apple_yang/instagram-transcripts-scraper)

## Skill Output:

**Output Type(s):** [Text, Analysis, Markdown]

**Output Format:** [Transcript text or Markdown containing a transcript and optional summary, translation, or analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Timestamps appear only when valid timestamps are returned; summaries, translations, and analysis are based on returned transcript text.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
