## Description:

Turns public TikTok comments and operator-written replies into individual spoken reply clips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Social-media operators use this skill to plan a labeled list of replies to public TikTok comments and generate one spoken audio clip per reply line they have written. It can work from pasted comments when live lookup is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reusable device token grants broad Beatra account and media-generation access.

Mitigation: Review the requested access before connecting, keep the token private, and disconnect the device when access is no longer needed.

Risk: Paid comment lookups, voice cloning, and speech synthesis can consume credits.

Mitigation: Check each live price and exact request, then obtain operator approval before every paid stage or additional lookup page.

Risk: Automatic updates can replace skill code without separate approval.

Mitigation: Disable automatic updates when code changes require review before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/tiktok-comment-reply-voice)
- [Beatra skill homepage](https://beatra.ai/skills/tiktok-comment-reply-voice)
- [TikTok comment reply workflow](artifact/references/workflow.md)
- [Comment lookup](artifact/references/comment-lookup.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Audio clips, Markdown guidance]

**Output Format:** [Labeled listen list and individual MP3 spoken-reply clips]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One clip per approved reply line; reports available task results and actual credits charged.]

## Skill Version(s):

0.1.8 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
