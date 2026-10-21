## Description:

Guides agents through HyperFrames video project setup, editing, checks, previews, and approved local or cloud rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators use this skill to scaffold and inspect HyperFrames projects, troubleshoot build or render failures, preview changes, and render approved videos locally or through HeyGen, AWS Lambda, or Google Cloud Run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned CLI commands can execute external code.

Mitigation: Trust the publisher before installing; prefer a project wrapper or pinned CLI version and review commands before execution.

Risk: Cloud rendering and publishing may use credentials and upload project files.

Mitigation: Review cloud, publish, Lambda, and Cloud Run operations and their destination before granting credentials or uploading a project.

Risk: Feedback and telemetry can transmit project details; skill-management commands can alter local agent tooling.

Mitigation: Review feedback and skill-management commands before use, and opt out of telemetry or feedback when project details should remain private.

## Reference(s):

- [HyperFrames CLI skill release](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HyperFrames catalog search documentation](https://hyperframes.heygen.com/developers/catalog-search)
- [HyperFrames cloud rendering guide](artifact/references/cloud.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Rendering requires final user approval.]

## Skill Version(s):

1.0.71 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
