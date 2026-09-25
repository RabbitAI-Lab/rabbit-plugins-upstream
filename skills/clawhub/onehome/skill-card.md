## Description:

Search OneHome (CoreLogic) portal listings and retrieve property details, photos, schools, saved searches, listing comparisons, and local affordability calculations for agent-shared real estate portals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and real-estate buyers use this skill with agent-shared OneHome portal access to search listings, inspect property details, compare homes, retrieve photos and school information, and estimate mortgage or affordability values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OneHome magic links and bearer tokens can grant access to private portal data.

Mitigation: Provide credentials only through approved secret-handling paths, avoid logging or screenshotting them, and install the skill only when the agent should access that OneHome account data.

Risk: Compact view can omit media URLs and make photo-oriented queries appear incomplete.

Mitigation: Use full view when retrieving media URLs, investigating missing fields, or debugging unexpected OneHome payloads.

Risk: Expired or unavailable authentication can prevent portal lookups from completing.

Mitigation: Run the health check before lookup workflows and refresh the OneHome token or signed-in portal session when expiry or capture-mode status requires it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/onehome)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or plain text summaries with structured tool-call arguments and returned listing data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact view strips image and avatar URLs for selected tools by default; full view is needed when media URLs or complete payload inspection are required.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
