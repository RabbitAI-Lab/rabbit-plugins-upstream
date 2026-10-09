## Description:

Helps agents plan, generate, edit, extend, and review short AI videos from written directions or supplied media using Beatra.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill through an agent to design short product videos, ads, social clips, and cinematic concepts, then review delivered clips before requesting revisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent Beatra device token is stored locally and reused across Beatra skills.

Mitigation: Review the shared credential arrangement before connecting and disconnect when access is no longer needed.

Risk: Approved prompts and media are sent to Beatra for processing.

Mitigation: Send only media and text the user approves for external processing.

Risk: Video and other generation stages can spend credits.

Mitigation: Check current pricing and obtain explicit confirmation before each paid stage; report the final charge.

Risk: Installed package code may update silently by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if code changes require explicit approval.

## Reference(s):

- [Beatra AI Video Studio release](https://clawhub.ai/beatra-ai/skills/beatra-ai-video-studio)
- [Intent and routing](artifact/references/intent-and-routing.md)
- [Shot design](artifact/references/shot-design.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with video plans, review guidance, and optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to generated video or image results after approved Beatra tasks complete.]

## Skill Version(s):

1.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
