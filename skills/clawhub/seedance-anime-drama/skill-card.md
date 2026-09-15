## Description:

Requires OFOX_API_KEY; turns a novel or script excerpt into an anime-style storyboard clip by generating character opening frames with Ofox image APIs and animating them with Ofox video APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to turn story excerpts into anime-style single shots or short sequences with a consistent primary character. It guides the agent through brief questions, two approval gates, image generation, and video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recovery guidance includes an overbroad wildcard global installer path.

Mitigation: Install only the specific required core skills from a trusted source, and avoid wildcard global --yes installation.

Risk: The optional identity-reference route can expose user images through public hosting.

Mitigation: Do not use the public-image identity route for personal, private, or proprietary images unless short-lived private hosting and deletion are controlled.

Risk: Story text, prompts, and generated assets are sent to Ofox for paid processing.

Mitigation: Review content sensitivity before use and require the documented dry-run cost table plus explicit user approval before generation.

Risk: The workflow depends on separate ofox-image-core and ofox-video-core skills.

Mitigation: Verify both core skills are installed from the same trusted publisher source and run their availability checks before spending.

Risk: Generated image or video requests can be refused by model moderation or copyright checks.

Mitigation: Treat refusals as prompt or model selection issues, revise the prompt or route, and rely on the tool-reported billing status rather than assuming cost.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/seedance-anime-drama)
- [Skill homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-anime-drama)
- [Ofox API key portal](https://app.ofox.ai)
- [Ofox models catalog](https://api.ofox.ai/v1/models/catalog)
- [ofox-video-core creative brief](../ofox-video-core/references/creative-brief.md)
- [ofox-video-core prompt structure](../ofox-video-core/references/prompt-structure.md)
- [ofox-video-core approval gate](../ofox-video-core/references/approval-gate.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with bash command blocks, approval tables, prompts, and generated file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY, curl, jq, and installed ofox-image-core and ofox-video-core skills; outputs include prompts, dry-run cost tables, IMAGE_PATH, VIDEO_PATH, and cost reports.]

## Skill Version(s):

1.13.1 (source: frontmatter, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
