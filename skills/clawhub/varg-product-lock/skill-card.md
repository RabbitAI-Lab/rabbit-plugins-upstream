## Description:

Turns product photos into AI video shots that keep the product identical: a lock sheet (fixed geometry, fixed surface, allowed motion), a reference pack of 2-4 angles passed as @image roles to Seedance 2.5 or Kling 4, a camera-risk ladder (locked frame → push-in → slide → small orbit), banned motion words, one action per 4-6 s shot, a drift check with varg video_analyze, and the real packshot composited back where text must be exact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and product marketers use this skill to prepare consistent product references and video prompts, check generated clips for product drift, and preserve exact packshot details in AI product videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, clip URLs, and product details may be sent to Varg or other model providers, including confidential or unreleased product material.

Mitigation: Share only material approved for those services; avoid confidential or unreleased products unless their use is authorized.

Risk: The reported installer is unpinned, and scan coverage was partial; a benign scan verdict is not a guarantee of safety.

Mitigation: Review and pin the installer before use, and inspect the skill and its dependencies because a local reference could not be matched.

## Reference(s):

- [Varg how-to](https://varg.ai/how-to)
- [Varg MCP server](https://mcp.varg.ai/mcp)
- [Seedance product-shape consistency guide](https://www.seedance.tv/blog/how-to-keep-product-shape-consistent-in-ai-video-ads)
- [Varg video analysis API](https://api.varg.ai/v2/tools/video_analyze/call)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands]

**Output Format:** [Markdown guidance with product lock sheets, video prompts, and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands for clip analysis and packshot compositing.]

## Skill Version(s):

1.0.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
