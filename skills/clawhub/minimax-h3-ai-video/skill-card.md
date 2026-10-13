## Description:

Helps creators turn written briefs and image, video, or audio references into MiniMax H3 video prompts and generated videos through Beatra.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and marketing teams use this skill to plan and generate promotional, product, and social videos from a brief or supplied media. It also helps them check costs, track tasks, and review results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad Beatra account token is stored locally.

Mitigation: Protect ~/.beatra credentials and revoke the device in the Beatra Console if the token is exposed or the skill is no longer needed.

Risk: Selected images, video, and audio are uploaded to Beatra.

Mitigation: Upload only media you are comfortable sharing with Beatra.

Risk: Video generation can incur charges.

Mitigation: Review the live cost and admission card before approving a paid generation request.

Risk: The bundled client silently installs verified updates by default.

Mitigation: Disable automatic updates with python3 scripts/mcp_client.py update --auto off if you need to review changes first.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/minimax-h3-ai-video)
- [Video routing](references/video-routing.md)
- [Video workflow](references/workflow.md)
- [Media requirements](references/media-requirements.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and links to generated videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task status, video dimensions and duration, and billed credits.]

## Skill Version(s):

0.2.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
