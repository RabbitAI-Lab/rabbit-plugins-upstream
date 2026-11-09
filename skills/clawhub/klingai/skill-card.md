## Description:

Calls Kling AI for video and image generation, subject and voice management, and account quota inquiries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[klingai-dev](https://clawhub.ai/user/klingai-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to generate images and videos with Kling AI, manage reusable subjects and voices, and check account quotas. It also provides credential setup options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation can create billable tasks and sends prompts and supplied media to Kling AI.

Mitigation: Confirm the requested generation and expected cost, and review media before submission.

Risk: Credential setup can save an API key in local credential storage.

Mitigation: Protect the local credentials and avoid sharing or exposing the API key.

## Reference(s):

- [Kling AI API documentation](https://klingai.com/document-api/)
- [Kling AI API authentication](https://klingai.com/document-api/api/get-started/authentication.md)
- [Kling AI skill release on ClawHub](https://clawhub.ai/klingai-dev/skills/klingai)

## Skill Output:

**Output Type(s):** [Images, Videos, Text, Configuration]

**Output Format:** [Generated media files with text results and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation requests may incur charges; account quota inquiries are read-only.]

## Skill Version(s):

2.0.3 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
