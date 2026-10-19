## Description:

Coordinates Beatra voice selection, text-to-speech narration, multilingual audio production, and consent-based voice cloning from approved scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to plan and generate narration from approved text, organize long-form or multilingual deliveries, and create an authorized reusable voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared full-scope Beatra device token provides broad account access.

Mitigation: Review the account connection before installing and keep the local credential private; revoke access when no longer needed.

Risk: Default silent updates can replace local package files without a separate confirmation.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if you require manual review of changes.

Risk: Voice cloning uploads a speaker sample and could imitate someone without permission.

Mitigation: Confirm explicit speaker authorization before uploading a sample or submitting a clone request.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/voiceover-narration-studio)
- [Beatra voiceover studio](https://beatra.ai/skills/voiceover-narration-studio)
- [Voice cloning and review](artifact/references/voice-cloning-and-review.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Audio artifact links]

**Output Format:** [Markdown with production plans, task results, and links to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio generation and voice cloning require explicit approval before billable requests.]

## Skill Version(s):

0.2.3 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
