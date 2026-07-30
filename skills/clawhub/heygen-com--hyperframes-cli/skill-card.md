## Description: <br>
Use the HyperFrames CLI development loop for scaffolding, checking, previewing, rendering, publishing, cloud rendering, diagnostics, upgrades, and related video workflow tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content engineers use this skill to guide agents through HyperFrames CLI workflows for creating, validating, previewing, rendering, publishing, and troubleshooting video compositions across local, hosted, AWS Lambda, and Google Cloud Run paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may submit public feedback, publish artifacts, upload project archives, or invoke cloud rendering paths. <br>
Mitigation: Require explicit user approval before feedback, publish, cloud render, or file-issue actions, and review what project files, logs, credentials, or billing resources will be affected. <br>
Risk: Some commands can read or use HeyGen credentials and API keys. <br>
Mitigation: Confirm the intended credential source before authentication or cloud commands, avoid exposing secrets in logs, and prefer status checks that do not reveal credential values. <br>
Risk: AWS Lambda and Google Cloud Run workflows can create, modify, or destroy cloud infrastructure. <br>
Mitigation: Use the matching reference workflow, verify the target account or project, and require explicit confirmation before deploy or destroy commands. <br>
Risk: Telemetry and usage classification data may be sent unless disabled. <br>
Mitigation: Disable telemetry with HYPERFRAMES_NO_TELEMETRY=1 or the telemetry command when the user does not want usage or environment classification data sent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-cli) <br>
- [HeyGen publisher profile](https://clawhub.ai/user/heygen-com) <br>
- [cloud - HeyGen-hosted rendering](references/cloud.md) <br>
- [preview, play, render, publish](references/preview-render.md) <br>
- [lint, check, snapshot](references/lint-validate-inspect.md) <br>
- [init, capture, skills](references/init-and-scaffold.md) <br>
- [Lambda rendering on AWS](references/lambda.md) <br>
- [Cloud Run rendering on Google Cloud](references/cloudrun.md) <br>
- [doctor, browser](references/doctor-browser.md) <br>
- [Compare and batch rendering](references/compare-and-batch.md) <br>
- [Generate a project beat grid](references/beats.md) <br>
- [info, upgrade, compositions, docs, benchmark, telemetry, asset preprocessing](references/upgrade-info-misc.md) <br>
- [heygen-cli repository](https://github.com/heygen-com/heygen-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration notes, and workflow checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that affect credentials, telemetry, uploads, cloud infrastructure, project files, and rendered media outputs.] <br>

## Skill Version(s): <br>
1.0.23 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
