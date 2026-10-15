## Description:

Guides agents through creating, checking, previewing, and rendering HyperFrames video projects with the CLI, locally or through hosted and self-managed cloud options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to scaffold, inspect, troubleshoot, preview, and render HyperFrames projects, including local, HeyGen-hosted, AWS Lambda, and Google Cloud Run workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic feedback can disclose project details through a public channel.

Mitigation: Disable telemetry or require explicit approval for feedback; review and redact the exact payload, and publish issues only with consent.

Risk: Floating npx invocations may execute an unreviewed CLI version.

Mitigation: Pin or locally lock the HyperFrames CLI version before running commands.

Risk: Cloud rendering or publishing can upload project contents and use existing credentials.

Mitigation: Review project contents, destination, and credentials before upload, and avoid public publishing unless intended.

## Reference(s):

- [HyperFrames CLI skill release](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Preview, rendering, and feedback guidance](artifact/references/preview-render.md)
- [HeyGen-hosted cloud rendering guidance](artifact/references/cloud.md)
- [HyperFrames catalog search documentation](https://hyperframes.heygen.com/developers/catalog-search)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide project edits and generation of rendered video assets.]

## Skill Version(s):

1.0.69 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
