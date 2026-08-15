## Description:

Compresses local image files, folders, and remote image URLs through the NX API, returning CDN URLs and compression ratios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaowu89](https://clawhub.ai/user/xiaowu89)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content operators use this skill to compress JPG, PNG, and WebP images from local paths, folders, or URLs and retrieve compressed CDN-hosted results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan verdict is suspicious because the skill uses obfuscated code.

Mitigation: Review the JavaScript source and scanner summary before installing or running the skill.

Risk: The skill uploads selected local images or image URLs to a remote NX API/CDN service.

Mitigation: Avoid using the skill on confidential images unless uploading them to that service is acceptable.

Risk: The skill searches nearby .env files for NX_API_KEY and can expose credentials from the workspace or home directory to the compression request.

Mitigation: Run it only in workspaces where that credential lookup behavior is acceptable, and keep unrelated secrets out of nearby .env files.

Risk: The skill creates a persistent machine identifier for API use.

Mitigation: Install only where persistent device identification is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaowu89/skills/skill-compress)
- [ClawHub publisher profile](https://clawhub.ai/user/xiaowu89)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and tabular compression results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CDN URLs, original and compressed byte sizes, compression ratios, and API error messages.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
