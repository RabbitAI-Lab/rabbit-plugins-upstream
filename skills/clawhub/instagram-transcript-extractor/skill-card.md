## Description:

Extract spoken transcripts from one or more public Instagram video or Reel links, and summarize, translate, or analyze the resulting text when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apismith-labs](https://clawhub.ai/user/apismith-labs)

### License/Terms of Use:

MIT-0

## Use Case:

External users can submit public Instagram video or Reel links to receive spoken transcripts, then request summaries, translations, timestamps when available, or simple analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Processing uses a third-party Apify Actor through the user's connected account, may incur charges, and the Actor's code is outside the inspected bundle.

Mitigation: Review the Actor's pricing and data handling before use, and configure credentials only through the host's private connection settings.

Risk: Results can be incomplete when the host cannot establish that retrieval finished.

Mitigation: Keep affected results provisional or pending until complete retrieval is established.

## Reference(s):

- [Apify MCP setup](https://docs.apify.com/mcp)
- [Codex desktop setup](https://docs.apify.com/integrations/codex-app)
- [Instagram Transcripts Scraper Actor](https://apify.com/apple_yang/instagram-transcripts-scraper)
- [Workflow reference](references/workflow.md)

## Skill Output:

**Output Type(s):** [Text, Analysis]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-link transcript results; timestamps when validated; summaries, translations, or analysis when requested. Original transcript and generated text are labeled separately.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
