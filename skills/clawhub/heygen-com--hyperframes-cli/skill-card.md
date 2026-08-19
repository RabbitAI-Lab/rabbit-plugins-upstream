## Description:

Use the HyperFrames CLI development loop for scaffolding, checking, previewing, rendering, publishing, cloud rendering, diagnostics, and related project operations across local, HeyGen-hosted cloud, AWS Lambda, and Google Cloud Run workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate HyperFrames projects: scaffold projects, author and validate compositions, preview and render outputs, run batch or cloud renders, publish results, manage diagnostics, and collect feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud, publish, feedback, auth, and infrastructure workflows can upload project files, use external provider accounts, or disclose operational details.

Mitigation: Before using those workflows, confirm the intended upload or publication scope, whether telemetry or feedback should be disabled, and which cloud account or credential should be used.

Risk: The skill covers broad rendering and diagnostic workflows where static checks may not catch every sub-composition or runtime issue.

Mitigation: Follow the documented final preview, snapshot, and output verification steps before rendering or delivering final media.

## Reference(s):

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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to run CLI commands, inspect generated files, produce rendered media, submit feedback, or use cloud provider credentials when the user approves those workflows.]

## Skill Version(s):

1.0.29 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
