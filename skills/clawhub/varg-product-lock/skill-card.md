## Description:

Turns product photos into AI video shots that keep the product consistent by defining a product lock, preparing multi-angle references, guiding camera motion, checking for drift, and restoring exact packshot details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Product creators, marketers, and developers use this skill to plan product-focused AI video shots, reduce shape and label drift, check generated clips against product details, and restore exact packshot text where needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images may contain confidential designs or other sensitive material sent to external AI providers.

Mitigation: Use assets authorized for VARG and the selected AI providers, and check their handling policies before submitting confidential designs.

Risk: Repeated video generation and drift checks may incur service credits.

Mitigation: Set a generation and retry budget before producing clips.

Risk: External installers, related skills, and remote service internals are outside this artifact review.

Mitigation: Review the installation version and install only the intended skill; assess related skills and external installers separately.

## Reference(s):

- [VARG how-to guide](https://varg.ai/how-to)
- [VARG Product Lock on ClawHub](https://clawhub.ai/vargai/skills/varg-product-lock)
- [Guide to keeping product shape consistent in AI video](https://www.seedance.tv/blog/how-to-keep-product-shape-consistent-in-ai-video-ads)
- [AI product video reference examples](https://github.com/AuraJZ/ai-product-video)
- [VARG MCP server](https://mcp.varg.ai/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, AI video clips, Video-analysis results]

**Output Format:** [Markdown guidance with product lock sheets, prompts, and inline Bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses product photos and a selected video model; external generation and analysis services may incur credits.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
