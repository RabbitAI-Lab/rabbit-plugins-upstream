## Description:

Turns a product URL, marketing URL, pasted script, or brief into a HyperFrames product launch or promo video for launches, demos, feature reveals, and site showcases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, product teams, and creative operators use this agent skill to capture product and brand inputs, plan the launch story, assemble HyperFrames scenes, coordinate audio and captions, and render a product launch video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs mutable external tooling and updates related skills before or during use.

Mitigation: Install only when the HyperFrames CLI and related skills are trusted; prefer pinned, reviewed tool versions where possible.

Risk: Processing external product URLs can expose the workflow to untrusted site content.

Mitigation: Use trusted product URLs or provided source material, and avoid attacker-controlled sites until the caption and font sanitization issue is fixed.

Risk: Captured website content can influence generated video text and visuals.

Mitigation: Review the captured assets, storyboard, captions, and final preview before publishing or using the rendered video.

## Reference(s):

- [Story Design](references/story-design.md)
- [Visual Design](references/visual-design.md)
- [Motion Language](references/motion-language.md)
- [Cut Catalog](references/cut-catalog.md)
- [Frame Worker](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown plans and scripts, JSON metadata, HTML frame files, shell commands, and rendered video artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coordinates a multi-step HyperFrames project workflow with user review gates and generated project files.]

## Skill Version(s):

1.0.39 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
