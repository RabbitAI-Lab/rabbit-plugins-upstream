## Description:

Captures a macOS screen snapshot by recording a brief screen clip through SkillHub screen-record permissions and extracting a PNG frame.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to capture a current macOS screen or target node snapshot for automation, troubleshooting, or workflow documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Screen capture may expose sensitive on-screen information.

Mitigation: Ask the user to confirm the target before each capture and avoid capturing private or confidential content.

Risk: The skill leaves generated media files on disk.

Mitigation: Delete snap.mp4 and snap.png when they are no longer needed.

Risk: The trigger wording is broad for a privacy-sensitive screen-recording action.

Mitigation: Require explicit confirmation before every capture, especially when the visible screen may contain sensitive data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/mac-node-snapshot)
- [SkillHub skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Shell commands, Files, JSON, Guidance]

**Output Format:** [Markdown instructions with bash commands and JSON result structure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces temporary snap.mp4 and snap.png files under the skill tmp directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence; artifact frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
