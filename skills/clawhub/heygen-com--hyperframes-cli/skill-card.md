## Description: <br>
Guides agents through HyperFrames CLI workflows for project creation, validation, preview, rendering, publishing, cloud execution, diagnostics, feedback, and media utilities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate HyperFrames projects end to end: scaffold or capture projects, run lint/check/preview loops, render locally or through HeyGen, AWS, or Google Cloud paths, diagnose failures, and share rendered outputs after approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud rendering, deployment, cleanup, publishing, issue filing, and skill-pack installation can spend credits, modify infrastructure, upload assets, publish project material, or change the local AI skill environment. <br>
Mitigation: Require explicit user approval before running cloud deploy/render, AWS or GCP destroy, publish, feedback --file-issue, or skill-pack installation commands. <br>
Risk: Feedback and public sharing flows can disclose project details when logs, paths, credentials, or source assets are submitted. <br>
Mitigation: Use only consented sharing paths, redact secrets and absolute paths, and keep reproduction packets privacy-preserving before submission. <br>


## Reference(s): <br>
- [HyperFrames CLI skill source](artifact/SKILL.md) <br>
- [init, capture, skills](artifact/references/init-and-scaffold.md) <br>
- [lint, check, snapshot](artifact/references/lint-validate-inspect.md) <br>
- [Compare and batch rendering](artifact/references/compare-and-batch.md) <br>
- [preview, play, render, publish](artifact/references/preview-render.md) <br>
- [cloud - HeyGen-hosted rendering](artifact/references/cloud.md) <br>
- [AWS Lambda rendering](artifact/references/lambda.md) <br>
- [Cloud Run rendering on Google Cloud](artifact/references/cloudrun.md) <br>
- [doctor and browser management](artifact/references/doctor-browser.md) <br>
- [info, upgrade, compositions, docs, benchmark, telemetry, asset preprocessing](artifact/references/upgrade-info-misc.md) <br>
- [Generate a project beat grid](artifact/references/beats.md) <br>
- [HeyGen CLI](https://github.com/heygen-com/heygen-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct creation or verification of video, image, JSON, and project files through HyperFrames CLI commands.] <br>

## Skill Version(s): <br>
1.0.22 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
