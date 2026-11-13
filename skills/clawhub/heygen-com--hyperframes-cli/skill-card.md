## Description:

HyperFrames CLI - scaffold, check frames, edit timelines, preview, render, share and project history; read JSON and recover from failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to operate the HyperFrames CLI while creating and editing video projects, checking frames and timelines, previewing and rendering output, and managing cloud or local workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan reports undeclared cloud and account-related actions, automatic reporting, and repeated use of an unpinned CLI; scan coverage was partial.

Mitigation: Pin the package version and review its reporting, telemetry, credential access, and cloud resource actions before use; make those actions clear and optional.

## Reference(s):

- [Beats](references/beats.md)
- [Cloud rendering](references/cloud.md)
- [Cloud Run rendering](references/cloudrun.md)
- [Compare and batch rendering](references/compare-and-batch.md)
- [CLI conventions](references/conventions.md)
- [Doctor and browser](references/doctor-browser.md)
- [Feedback](references/feedback.md)
- [Initialize and scaffold](references/init-and-scaffold.md)
- [AWS Lambda rendering](references/lambda.md)
- [Lint, validate, inspect](references/lint-validate-inspect.md)
- [Preview and render](references/preview-render.md)
- [Upgrade and project information](references/upgrade-info-misc.md)
- [HyperFrames CLI on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies by CLI task; no fixed output shape.]

## Skill Version(s):

1.0.91 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
