## Description:

Guides agents through the HyperFrames CLI workflow for scaffolding, validating, previewing, rendering, publishing, cloud rendering, diagnostics, and related media tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video automation engineers use this skill to operate the HyperFrames CLI for creating, checking, previewing, rendering, publishing, and deploying HyperFrames video projects across local, HeyGen-hosted, AWS Lambda, and Google Cloud Run environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses mutable npm execution for HyperFrames CLI commands.

Mitigation: Install only from a trusted publisher and prefer an exact package version or pinned project wrapper before running commands.

Risk: Cloud rendering and deployment paths may use HeyGen, AWS, or GCP credentials.

Mitigation: Use dedicated narrowly scoped credentials, verify HEYGEN_API_URL before using stored credentials, and separate hosted HeyGen, AWS, and GCP trust boundaries.

Risk: Telemetry and feedback commands can send operational details outside the local environment.

Mitigation: Disable telemetry or feedback unless explicitly wanted, and review or redact public feedback payloads before sending.

Risk: Hosted rendering, publishing, and feedback workflows can upload project files or reproduction artifacts.

Mitigation: Inspect upload contents, use project-specific exclusion rules, and require explicit approval before public publishing or issue filing.

## Reference(s):

- [HyperFrames CLI Skill on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [cloud - HeyGen-hosted rendering](references/cloud.md)
- [preview, play, render, publish](references/preview-render.md)
- [lint, check, snapshot](references/lint-validate-inspect.md)
- [Lambda rendering on AWS](references/lambda.md)
- [Cloud Run rendering on Google Cloud](references/cloudrun.md)
- [Compare and batch rendering](references/compare-and-batch.md)
- [doctor, browser](references/doctor-browser.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce JSON-oriented command guidance for CLI calls that support machine-readable output.]

## Skill Version(s):

1.0.35 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
