## Description: <br>
Guides agents through HyperFrames CLI workflows for scaffolding, checking, previewing, rendering, publishing, cloud rendering, diagnostics, telemetry, and related media utilities across local, HeyGen-hosted, AWS Lambda, and Google Cloud Run paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to operate the HyperFrames CLI development loop, including project initialization, validation, preview, render, publish, cloud render, and failure diagnosis. It helps agents choose the correct local, managed HeyGen cloud, AWS Lambda, or Google Cloud Run workflow before running commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud render and publish paths may upload project source and assets to hosted services. <br>
Mitigation: Use cloud and publish commands only for explicit HyperFrames tasks where the user accepts upload and persistence behavior; inspect archive contents and size with dry-run workflows when needed. <br>
Risk: Hosted cloud, AWS Lambda, and Google Cloud Run workflows may use credentials and incur billing or persistent infrastructure costs. <br>
Mitigation: Confirm the intended provider before running cloud, Lambda, or Cloud Run commands, use existing credential controls, and clean up self-managed infrastructure when the workflow is complete. <br>
Risk: Feedback and issue-reporting workflows may disclose project details if raw paths, identifiers, secrets, or assets are submitted. <br>
Mitigation: Redact absolute paths, user or machine identifiers, credentials, and sensitive project details; use public issue publication only with explicit consent. <br>
Risk: The skill may cause an agent to run HyperFrames through npx and start local preview servers. <br>
Mitigation: Run commands only in appropriate project directories, follow the required preview and approval gates, and verify generated outputs before delivery. <br>


## Reference(s): <br>
- [HyperFrames CLI skill page](https://clawhub.ai/heygen-com/skills/hyperframes-cli) <br>
- [init, capture, skills](references/init-and-scaffold.md) <br>
- [lint, check, snapshot](references/lint-validate-inspect.md) <br>
- [preview, play, render, publish](references/preview-render.md) <br>
- [cloud - HeyGen-hosted rendering](references/cloud.md) <br>
- [Lambda rendering on AWS](references/lambda.md) <br>
- [Cloud Run rendering on Google Cloud](references/cloudrun.md) <br>
- [Compare and batch rendering](references/compare-and-batch.md) <br>
- [Generate a project beat grid](references/beats.md) <br>
- [doctor, browser](references/doctor-browser.md) <br>
- [info, upgrade, compositions, docs, benchmark, telemetry, asset preprocessing](references/upgrade-info-misc.md) <br>
- [HeyGen CLI](https://github.com/heygen-com/heygen-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with inline bash commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct agents to use JSON CLI output for automation and to verify rendered files before delivery.] <br>

## Skill Version(s): <br>
1.0.24 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
