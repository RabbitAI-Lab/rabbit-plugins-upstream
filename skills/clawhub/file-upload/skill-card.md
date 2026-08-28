## Description:

Uploads local image, video, or audio files to Flyelep cloud storage through the Flyelep HTTP API and returns a permanent public URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a user provides a local media file that must be converted into a public Flyelep URL before calling downstream Flyelep image, video, or audio workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media becomes accessible through permanent public links.

Mitigation: Upload only media that the user intends to make public, and avoid confidential, private, or rights-unclear content.

Risk: The Flyelep secretKey is required for API calls.

Mitigation: Request the key at runtime and do not store real keys in skill files, examples, repositories, logs, or persistent configuration.

Risk: Video and audio uploads are stored without the image content review step described by the skill.

Mitigation: Use video and audio only when the source and rights are clear, and confirm the user intended to upload that media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/file-upload)
- [Flyelep file upload API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)
- [Flyelep control board](https://www.flyelep.cn/controlboard)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline HTTP and shell command examples; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the data.fullPath URL for downstream use; each upload processes one file.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
