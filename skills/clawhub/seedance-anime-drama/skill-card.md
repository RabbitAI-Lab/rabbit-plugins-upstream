## Description:

Creates anime-style storyboard video prompts and generation commands from a novel or script excerpt by first producing character opening frames with Ofox image generation, then using those frames for Ofox video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to turn prose or script excerpts into anime-style video shot plans, image-generation prompts, approval tables, and shell commands for Ofox image and video APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generated images, and video requests are sent to Ofox and its upstream providers using OFOX_API_KEY.

Mitigation: Use the skill only when that data sharing is acceptable for the content being processed.

Risk: The identity-reference path may require making user images publicly reachable.

Mitigation: Avoid personal or sensitive images for this path; use private temporary URLs and delete them afterward, or prefer the local --frame-first-image path.

Risk: A mutable npx recovery command can introduce supply-chain risk.

Mitigation: Pin or verify the package source before running the recovery command.

Risk: Generation uses paid image and video API calls.

Mitigation: Require the documented dry-run cost tables and explicit user approval before each paid generation phase.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/seedance-anime-drama)
- [Source homepage](https://github.com/ofoxai/skills/tree/main/skills/seedance-anime-drama)
- [Ofox API key portal](https://app.ofox.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and approval tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY and local curl and jq; produces prompts and commands for image and video generation rather than media files directly.]

## Skill Version(s):

1.11.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
