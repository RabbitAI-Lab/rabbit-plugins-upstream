## Description:

Beatra Universal creates and edits AI images, videos, music, and speech, and retrieves public social data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users use Beatra Universal to create and edit AI media, manage returned assets and task progress, and look up public social data. Voice cloning is intended only for voices the user owns or is authorized to use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded media are processed by Beatra's cloud service.

Mitigation: Share only text and media intended for that service.

Risk: The shared Beatra authorization permits credit spending for generation.

Mitigation: Review the intended action and credit use before submitting billable work.

Risk: Installation analytics run automatically, with no documented opt-out.

Mitigation: Account for automatic analytics when deciding whether to install the skill.

Risk: Removing one Beatra skill may leave other Beatra skills connected.

Mitigation: Check other Beatra skills' connections after uninstalling, and use the existing installation tool for updates.

Risk: Voice cloning may use a voice without its owner's authorization.

Mitigation: Clone only a voice the user owns or has explicit authorization to use.

## Reference(s):

- [Beatra Universal on ClawHub](https://clawhub.ai/beatra-ai/skills/beatra)
- [Updates and security](references/updates-and-security.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Speech and voices](references/speech-and-voices.md)
- [Public social data](references/social.md)

## Skill Output:

**Output Type(s):** [Images, Video, Audio, Text, Files]

**Output Format:** [Generated media files and concise text or Markdown summaries and findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media format, dimensions, duration, and task details vary with the request and supported options.]

## Skill Version(s):

2.9.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
