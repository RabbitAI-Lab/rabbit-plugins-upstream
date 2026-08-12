## Description:

Audits local images or image URLs for pornographic, political, violent, or terrorist content by compressing images and submitting them to the NX API, then summarizing pass, violation, and failure results in a table.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaowu89](https://clawhub.ai/user/xiaowu89)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operations teams use this skill to batch-check images or image URLs for policy-sensitive content and receive a concise audit table. It is intended for workflows where users explicitly request image moderation, violation scanning, or safety checks for JPG, PNG, or WebP assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload local images or submitted URLs to ai.nxtici.com for moderation.

Mitigation: Review data handling requirements before use and avoid submitting private images, internal URLs, or regulated content unless approved.

Risk: The skill searches broad .env locations for NX_API_KEY and may read unrelated secrets from parent directories or the user home directory.

Mitigation: Run it from a dedicated workspace and use a purpose-specific NX_API_KEY rather than directories containing unrelated .env secrets.

Risk: The skill sends a stable device identifier with API requests.

Mitigation: Use the documented client identifier option or review privacy expectations before running it on sensitive systems.

Risk: The runtime can modify the system by installing sharp globally if it is missing.

Mitigation: Install dependencies in advance in a controlled environment or run the skill in an isolated development container.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/xiaowu89/skill-function)
- [ClawHub skill page](https://clawhub.ai/xiaowu89/skills/skill-function)
- [NX image security check API endpoint](https://ai.nxtici.com/v1/nx/imgSecCheck)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown response with shell commands and a summarized audit table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs pass, violation, and failure status with source engine and error details when available.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
