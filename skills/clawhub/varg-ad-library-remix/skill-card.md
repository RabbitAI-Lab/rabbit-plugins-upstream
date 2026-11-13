## Description:

Turns patterns from successful competitor ads into original advertising concepts for a seller's product without reusing the source ad's footage, copy, music, voice, logo, or storyline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and marketing teams use this skill to analyze competitor advertising patterns and develop original ad concepts for their own products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rated this release suspicious with medium confidence due to an unpinned installation command and missing disclosure about sending local videos to VARG; scan coverage was incomplete.

Mitigation: Review the installer and its changing dependencies before use. Before video analysis, confirm you are comfortable sending the video to VARG and have permission to share it.

## Reference(s):

- [VARG setup and usage guide](https://varg.ai/how-to)
- [VARG MCP connection](https://mcp.varg.ai/mcp)
- [Meta Ads Archive API documentation](https://developers.facebook.com/docs/marketing-api/reference/ads_archive/)
- [Example remix workflow](references/example.md)
- [ClawHub release page](https://clawhub.ai/vargai/skills/varg-ad-library-remix)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown with structured ad analyses and concept briefs; JSON may be used for winner records.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Concept counts and details depend on the source ads and product evidence provided.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
