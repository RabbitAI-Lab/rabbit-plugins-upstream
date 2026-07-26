## Description: <br>
TencentCloud Oceanus Ops helps agents operate TencentCloud Oceanus workspaces for SQL and JAR job lifecycle tasks, configuration publishing, run and stop actions, dependency resources, folders, catalogs, events, and logs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tencent-adm](https://clawhub.ai/user/tencent-adm) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and Oceanus operators use this skill to run TencentCloud Oceanus workspace-level operations through the bundled CLI, including job creation, configuration updates, runtime control, dependency management, and observability queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform real TencentCloud Oceanus mutations, including job creation, job runs, resource uploads, and configuration publishing. <br>
Mitigation: Install only for trusted Oceanus operators and require least-privilege TencentCloud CAM credentials with confirmation gates for mutation and destructive actions. <br>
Risk: Draft publishing can change job behavior if reviewers miss SQL, resource, or configuration differences. <br>
Mitigation: Review every draft summary before publishing and avoid bypassing draft review unless the user explicitly opts out. <br>
Risk: Credential values, workspace variables, and COS log download URLs may expose sensitive operational data. <br>
Mitigation: Do not echo credentials, redact accidental secrets, keep OCEANUS_ENDPOINT unset unless verified as trusted, and avoid sharing outputs that contain variable values or COS presigned URLs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tencent-adm/skills/tencentcloud-oceanus-ops) <br>
- [TencentCloud CAM console](https://console.cloud.tencent.com/cam/capi) <br>
- [Agent operating protocol](references/agent-operating-protocol.md) <br>
- [Command catalog](references/command-catalog.md) <br>
- [Command map](references/command-map.md) <br>
- [Credential setup](references/credential-setup.md) <br>
- [Error handling](references/error-handling.md) <br>
- [Oceanus product model](references/oceanus-product-model.md) <br>
- [Job runtime operations playbook](references/playbooks/job-runtime-ops.md) <br>
- [Job observability playbook](references/playbooks/job-observability.md) <br>
- [Modify job configuration playbook](references/playbooks/modify-job-config.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and CLI output summaries with inline shell commands and JSON or table command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include TencentCloud operation summaries, draft review details, and redacted diagnostic output.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
