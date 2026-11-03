## Description:

Call Kling AI for video generation, image generation, subject management, voice management, and account quota inquiry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[klingai-dev](https://clawhub.ai/user/klingai-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use the skill to create videos and images through Kling, manage reusable subjects and voices, review account quota, and configure credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential cleanup and symlink-aware file boundaries have concrete flaws; older credentials may remain in identity.json.

Mitigation: Check identity.json for old credentials, restrict its permissions, and rotate credentials if exposure is possible. Use a dedicated media folder without symlinks and keep allowed roots narrow.

Risk: Submitting private media sends it to Kling; generation is billable, and device binding shares machine-identifying details.

Mitigation: Confirm Kling is the intended provider before submitting private media, review quota and costs, and consider the information shared during device binding.

## Reference(s):

- [Kling AI API documentation](https://klingai.com/document-api/)
- [Kling AI authentication documentation](https://klingai.com/document-api/api/get-started/authentication.md)
- [ClawHub skill release](https://clawhub.ai/klingai-dev/skills/klingai)

## Skill Output:

**Output Type(s):** [Media files, Text, Configuration guidance]

**Output Format:** [Generated video and image files, with task IDs, local paths, quota details, and setup guidance as text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation requests are billable; media is submitted to Kling and results may be saved locally.]

## Skill Version(s):

2.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
