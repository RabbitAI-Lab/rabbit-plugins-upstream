## Description:

Cloud-powered image compression and resize for JPG, PNG, WebP, HEIC, and related formats using the Pixmind API and Tencent Cloud COS imageMogr2.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fuyunzhishang](https://clawhub.ai/user/fuyunzhishang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compress, resize, and convert local or URL-based images, including batch-selected folders, through a cloud image-processing API while preserving originals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images, including batch-selected folders, are uploaded to Pixmind/Tencent-backed cloud processing.

Mitigation: Use only when external processing is acceptable, and avoid sensitive, regulated, or private images unless that transfer is approved.

Risk: The skill requires a Pixmind API key for authenticated API calls.

Mitigation: Keep PIXMIND_API_KEY protected in the environment or secret manager, and do not paste it into prompts, logs, or source files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fuyunzhishang/skills/pixmind-image-compress)
- [Pixmind](https://www.pixmind.io)
- [Pixmind API Platform keys](https://www.pixmind.io/api-platform/dashboard/keys)
- [Tencent Cloud COS imageMogr2 documentation](https://cloud.tencent.com/document/product/460/36540)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown with inline shell commands and CLI output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PIXMIND_API_KEY and may save compressed image files to the configured output directory.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
