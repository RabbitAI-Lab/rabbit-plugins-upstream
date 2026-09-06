## Description:

HyperFrames CLI helps agents scaffold, validate, preview, render, publish, and diagnose HyperFrames video projects across local, HeyGen cloud, AWS Lambda, and Google Cloud Run workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to drive the HyperFrames CLI development loop for video projects, including scaffolding, browser checks, preview review, rendering, publishing, cloud execution, and render-failure diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead agents to run unpinned external HyperFrames CLI commands.

Mitigation: Prefer a pinned or local HyperFrames version before running CLI workflows.

Risk: Cloud rendering, publishing, Lambda, or Cloud Run workflows may upload project source and use local or cloud credentials.

Mitigation: Inspect upload contents with dry-run workflows where available and use narrowly scoped AWS, GCP, and HeyGen credentials.

Risk: Feedback and search-miss submissions may send information to a public channel.

Mitigation: Disable telemetry or require explicit approval, then redact paths, project details, secrets, and credentials before submission.

Risk: Preview workflows may start background servers.

Mitigation: Track preview server URLs and stop background preview sessions after review is complete.

## Reference(s):

- [HyperFrames CLI skill page](https://clawhub.ai/heygen-com/skills/hyperframes-cli)
- [beats.md](references/beats.md)
- [cloud.md](references/cloud.md)
- [cloudrun.md](references/cloudrun.md)
- [compare-and-batch.md](references/compare-and-batch.md)
- [doctor-browser.md](references/doctor-browser.md)
- [init-and-scaffold.md](references/init-and-scaffold.md)
- [lambda.md](references/lambda.md)
- [lint-validate-inspect.md](references/lint-validate-inspect.md)
- [preview-render.md](references/preview-render.md)
- [upgrade-info-misc.md](references/upgrade-info-misc.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Markdown]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, JSON diagnostics, and preview or render paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide local preview servers, local renders, hosted renders, AWS Lambda renders, Google Cloud Run renders, telemetry controls, and credential-backed CLI workflows.]

## Skill Version(s):

1.0.33 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
