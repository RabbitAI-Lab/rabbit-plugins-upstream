## Description:

Turns product photos into AI video shots that keep the product identical using a lock sheet, reference images, controlled camera motion, drift checks, and real packshots where text must be exact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product marketers use the skill to prepare reference images and prompts for short AI product videos, then check clips for changes to product shape, color, size, or labels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer uses an unpinned npx skills package, which may change between installations.

Mitigation: Review the installer and pin a trusted package version before installing.

Risk: Product images, clip links, and descriptions may be sent to Varg and other named providers.

Mitigation: Avoid sending confidential assets unless approved, and review the providers’ privacy terms.

Risk: The security scan is partial because a local reference could not be resolved.

Mitigation: Review the unresolved reference and inspect the relevant skill content before use.

## Reference(s):

- [Varg how-to guides](https://varg.ai/how-to)
- [Varg MCP server](https://mcp.varg.ai/mcp)
- [Seedance product consistency guide](https://www.seedance.tv/blog/how-to-keep-product-shape-consistent-in-ai-video-ads)
- [ClawHub release page](https://clawhub.ai/vargai/skills/varg-product-lock)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown lock sheets, prompts, and clip review guidance with inline command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reusable prompt templates and workflow guidance; reference image count and shot duration vary by task.]

## Skill Version(s):

1.0.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
