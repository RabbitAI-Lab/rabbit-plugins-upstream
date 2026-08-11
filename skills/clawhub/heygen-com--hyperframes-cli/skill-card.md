## Description:

Use the HyperFrames CLI to scaffold, validate, preview, render, publish, and troubleshoot local, HeyGen-hosted, AWS Lambda, and Google Cloud Run video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video automation agents use this skill to operate HyperFrames CLI workflows for building, checking, previewing, rendering, publishing, and diagnosing video compositions across local and cloud rendering targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud, publish, feedback, or skill-install commands may move project files, variables, credentials, or outputs outside the local machine or alter the local agent setup.

Mitigation: Confirm the intended scope before using those commands and use dry-run, telemetry disable, logout, destroy, or manual cloud cleanup options where appropriate.

Risk: Secrets placed in render variables or project assets may be exposed through rendering, upload, publishing, or feedback workflows.

Mitigation: Keep secrets out of render variables and project assets, and review project contents before cloud or publishing operations.

Risk: The skill can guide broad local CLI workflows, including browser, FFmpeg, render, and cloud-resource operations.

Mitigation: Review proposed commands before execution and use the documented diagnostic, check, preview, and approval steps before final rendering or cleanup.

## Reference(s):

- [HyperFrames CLI skill page](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [HeyGen CLI](https://github.com/heygen-com/heygen-cli)
- [Generate a project beat grid](references/beats.md)
- [cloud - HeyGen-hosted rendering](references/cloud.md)
- [Cloud Run rendering on Google Cloud](references/cloudrun.md)
- [Compare and batch rendering](references/compare-and-batch.md)
- [doctor, browser](references/doctor-browser.md)
- [init, capture, skills](references/init-and-scaffold.md)
- [Lambda rendering on AWS](references/lambda.md)
- [lint, check, snapshot](references/lint-validate-inspect.md)
- [preview, play, render, publish](references/preview-render.md)
- [info, upgrade, compositions, docs, benchmark, telemetry, asset preprocessing](references/upgrade-info-misc.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and command contracts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agent use of local and cloud HyperFrames CLI commands and may produce command sequences, diagnostic steps, render instructions, and workflow recommendations.]

## Skill Version(s):

1.0.26 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
