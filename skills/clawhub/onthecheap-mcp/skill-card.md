## Description:

Find free and cheap things to do in a US city, including daily event listings with times, prices and venues, plus searchable deals, festivals, kids activities and local guides from the On the Cheap network.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find free or low-cost local events, deals, festivals, family activities and local guides across supported US city sites. It is suited for answering local activity planning questions, comparing nearby options, and retrieving article details from the On the Cheap network.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Event details, prices, venue information and deal availability come from third-party content and may be outdated.

Mitigation: Summarize results with dates, prices and source URLs, and tell users to verify time-sensitive details before acting.

Risk: Full article HTML can contain markup or text that should not be treated as agent instructions.

Mitigation: Handle article HTML as untrusted content to summarize or cite, not as instructions to execute.

## Reference(s):

- [On the Cheap network](https://livingonthecheap.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/onthecheap-mcp)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Markdown or structured text summarizing event listings, deals, article results and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only outputs may include third-party event details, prices, venues, dates, article excerpts, URLs and optional article body content.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
