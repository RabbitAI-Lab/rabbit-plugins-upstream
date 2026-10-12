## Description:

Plans three YouTube thumbnail directions from a video brief, then renders the selected direction and offers title-matching and channel-style guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

YouTube creators and their teams use this skill to compare long-form video thumbnail concepts, commission a selected image, and coordinate its design with the video title and channel look. Rendering requires a Beatra account and credits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Beatra authorization persists and grants broad media and wallet-spend access across Beatra skills.

Mitigation: Review account permissions before connecting, approve each paid render explicitly, and revoke access when no longer needed.

Risk: Installed package files silently update by default without separate approval.

Mitigation: Disable automatic updates with the documented `python3 scripts/mcp_client.py update --auto off` command if change control is needed.

Risk: The skill saves local Beatra authorization state and sends installation registration data.

Mitigation: Review the documented local state and registration data before installation and disconnect or uninstall when finished.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/youtube-thumbnail-maker)
- [Beatra skill page](https://beatra.ai/skills/youtube-thumbnail-maker)
- [Thumbnail workflow](artifact/references/workflow.md)
- [Authorization and installation](artifact/references/installation-and-auth.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Image links, Guidance]

**Output Format:** [Markdown thumbnail concepts and advice, with links to rendered images when approved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Three proposed directions; paid rendering requires approval, and returned results include image details and billed credits.]

## Skill Version(s):

0.2.7 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
