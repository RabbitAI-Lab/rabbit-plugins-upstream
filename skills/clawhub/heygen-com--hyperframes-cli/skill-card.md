## Description:

Guides agents through HyperFrames CLI workflows for building, checking, previewing, rendering, and publishing video compositions locally or in the cloud.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to scaffold video projects, diagnose build and render problems, review previews, and render or publish compositions with the HyperFrames CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands run through an unpinned npm CLI with broad authority over local projects.

Mitigation: Review the skill before installation, trust the HyperFrames package before use, and prefer a pinned or locally installed CLI.

Risk: Cloud uploads, publishing, deletion, infrastructure destruction, skill installation, and public repro reports may expose data or make lasting changes.

Mitigation: Require explicit approval before each of these actions and review what will be uploaded or published.

Risk: Remote browser debugging may expose an active browsing session.

Mitigation: Use isolated browser profiles for remote debugging.

## Reference(s):

- [HyperFrames CLI release on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [Preview, render, and publishing guide](artifact/references/preview-render.md)
- [Cloud rendering guide](artifact/references/cloud.md)
- [Lint and validation guide](artifact/references/lint-validate-inspect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with command examples and project instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of project files and rendered video outputs.]

## Skill Version(s):

1.0.50 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
