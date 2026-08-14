## Description:

Use when an understood video project needs selective transcript-timed titles, lower-thirds, statistics, metric spotlights, comparisons, lists, quotes, chapter cards, or calls to action authored as HyperFrames HTML graphics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitetowerai](https://clawhub.ai/user/whitetowerai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video-editing agents use this skill after video understanding to create transcript-timed content card overlays, review candidate copy and placement, and render approved HyperFrames graphics for a video project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The preview workflow opens local HTML pages, and some bundled examples request GSAP and fonts from third-party CDNs.

Mitigation: Review the example HTML before use in restricted or offline environments; prefer the generated project review pages when local and self-contained assets are required.

Risk: The skill reads and writes project working files and runs ffmpeg, Python, HyperFrames, Node.js, and browser preview tooling.

Mitigation: Run it only in the intended project workspace after reviewing proposed commands, generated paths, and dependency availability.

Risk: Incorrect card copy or placement could misstate transcript evidence or obscure protected faces, head silhouettes, or captions.

Mitigation: Use the candidate review, evidence references, composited still checks, and face/caption clearance gates before rendering the final overlay.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/whitetowerai/skills/video-add-content-cards)
- [Chart Data Reference](artifact/reference/chart-data.md)
- [Content Cards Review Template Design](artifact/reference/ux-design.md)
- [Content Cards Review Template Implementation Plan](artifact/reference/ux-implementation-plan.md)
- [Animated Theme Gallery](artifact/examples/gallery-animated.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with JSON plans, HTML/CSS/JavaScript compositions, Python and Node shell commands, local review pages, and rendered media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project working files, review artifacts, transparent overlay renders, and summary documentation; depends on /video-understand plus local ffmpeg, Python, Node.js, HyperFrames, and browser preview tooling.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
