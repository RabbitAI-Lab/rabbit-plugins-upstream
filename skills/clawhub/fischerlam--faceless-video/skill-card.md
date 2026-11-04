## Description:

Scenario-focused Sparki skill for faceless or no-camera-presence outputs while using the latest official Sparki setup, API-key, and upload workflow guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fischerlam](https://clawhub.ai/user/fischerlam)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to turn ideas or existing footage into faceless, no-camera-presence videos such as automation-style explainers, educational clips, narration-led outputs, shorts, reels, or TikTok-ready edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected videos, prompts, and project metadata to Sparki.

Mitigation: Use it only with content approved for Sparki processing and review uploads before execution.

Risk: The workflow may store a Sparki API key in local configuration.

Mitigation: Prefer SPARKI_API_KEY or another protected credential workflow over persistent plaintext configuration where possible.

Risk: Overriding the API base URL can redirect authenticated Sparki traffic.

Mitigation: Avoid --base-url unless the endpoint is fully trusted.

## Reference(s):

- [Faceless Video on ClawHub](https://clawhub.ai/fischerlam/skills/faceless-video)
- [Sparki](https://sparki.io)
- [Sparki Telegram upload](https://t.me/Sparki_AI_bot/upload)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide API-key setup, local file upload, Telegram Mini App upload, project creation, polling, and download workflows for Sparki-generated video outputs.]

## Skill Version(s):

1.0.12 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
