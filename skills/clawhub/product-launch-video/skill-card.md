## Description:

Turns a product URL, script, or brief into a branded product launch or promotional video using HyperFrames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to turn a product website or written brief into a storyboarded, narrated, branded launch video, with a preview before the final MP4 render.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Captured website font metadata can become executable preview HTML.

Mitigation: Avoid untrusted or attacker-controlled URLs until font metadata is strictly validated or escaped; inspect previews in an isolated runtime.

Risk: Remote tooling and media-provider credentials are used while the skill writes persistent project state.

Mitigation: Review commands and credential access, and run in an isolated workspace before approving the final render.

## Reference(s):

- [Story design](references/story-design.md)
- [Visual design](references/visual-design.md)
- [Motion language](references/motion-language.md)
- [Cut catalog](references/cut-catalog.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown project files and HTML compositions, with an MP4 video render]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a storyboard, preview, and frame snapshots for review.]

## Skill Version(s):

1.0.55 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
