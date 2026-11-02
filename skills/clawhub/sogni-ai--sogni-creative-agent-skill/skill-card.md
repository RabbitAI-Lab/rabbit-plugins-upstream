## Description:

A CLI and agent skill for generating and editing images, videos, and music with Sogni AI, including creative workflows and asset management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sogni-ai](https://clawhub.ai/user/sogni-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use the skill to generate, edit, and upscale image, video, and music assets, and to manage multi-step creative workflows through Sogni AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags the direct-mode privacy wording as misleading; direct generation still sends media for remote processing.

Mitigation: Use only media you authorize Sogni and its processing infrastructure to receive; do not use direct generation for media that must remain local.

Risk: Generation may incur charges, and exposed credentials or uninstall backups containing credentials could compromise account access.

Mitigation: Confirm spending limits before use, and keep the API key and any uninstall backup containing it private.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sogni-ai/skills/sogni-creative-agent-skill)
- [Sogni AI](https://sogni.ai)

## Skill Output:

**Output Type(s):** [Images, Video, Audio, 3D assets, Guidance]

**Output Format:** [Generated media files with concise textual status and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include multiple generated assets and workflow artifacts, depending on the request.]

## Skill Version(s):

3.60.1 (source: frontmatter, changelog, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
