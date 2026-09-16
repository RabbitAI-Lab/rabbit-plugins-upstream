## Description:

Enables agents to operate Jimeng AI through the OOMOL jimeng_ai connector for reading task results and submitting image, video, upscale, and video-agent jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Jimeng AI media-generation workflows from an OOMOL-connected account, including async image generation, text-to-image, image-to-video, video generation, smart upscale, and Lilinque video-agent tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts executed directly by the shell.

Mitigation: Use a trusted OOMOL distribution path, prefer signed or checksum-verified CLI installation, and avoid running installer commands from an elevated shell.

Risk: Write actions submit Jimeng AI generation or processing jobs that may consume credits or change remote service state.

Mitigation: Confirm the exact action, payload, and expected effect with the user before running any action tagged as write.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jimeng-ai)
- [Jimeng AI homepage](https://www.volcengine.com/product/jimeng)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON when actions run.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
