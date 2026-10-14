## Description:

Beatra AI Voice Studio helps agents select voices, turn approved scripts into narration, organize long-form or multilingual speech, and create consent-based reusable voices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use the skill to plan and generate voiceovers from approved text, organize audiobook or multilingual narration, and create authorized reusable voices through Beatra.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client can silently replace local package files through automatic updates.

Mitigation: Review and trust the Beatra update channel before installing; disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if unwanted.

Risk: The skill stores a shared Beatra device token locally.

Mitigation: Protect the installation's credentials and disconnect or revoke access when no longer needed.

Risk: Voice samples may be uploaded and generation or cloning can spend Beatra credits.

Mitigation: Require clear speaker consent before cloning, and review live price estimates and approve each paid operation before submission.

## Reference(s):

- [Beatra AI Voice Studio on ClawHub](https://clawhub.ai/beatra-ai/skills/beatra-ai-voice-studio)
- [Beatra AI Voice Studio](https://beatra.ai/skills/beatra-ai-voice-studio)
- [Voice casting and delivery](references/voice-casting-and-delivery.md)
- [Voice cloning and review](references/voice-cloning-and-review.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Audio asset links, Guidance]

**Output Format:** [Markdown with voice plans, task results, and audio links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports returned task and billing details; audio is delivered through returned asset links.]

## Skill Version(s):

0.3.1 (source: server-resolved release and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
