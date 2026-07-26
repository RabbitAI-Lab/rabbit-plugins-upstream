## Description: <br>
Huawei Cloud Ascend model deployment and testing skill for large language models on Ascend DevServer 910B series, supporting single- and dual-machine deployment for LLM, vision-language, embedding, and rerank models with inference testing, logs, status monitoring, model matching, and deployment command generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to deploy, test, and monitor supported LLM, vision-language, embedding, rerank, and open-source models on Huawei Cloud Ascend 910B DevServers. The skill helps select model-specific deployment scripts, validate prerequisites, generate shell and API test commands, and inspect deployment status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated deployment commands download and execute remote shell scripts on Ascend DevServers. <br>
Mitigation: Inspect downloaded script source before execution and prefer pinned versions with checksums or signatures. <br>
Risk: Deployment and test commands can start long-running processes or affect active DevServer workloads. <br>
Mitigation: Review the full generated command, confirm the target host, port, model, and NPU allocation, and require explicit user confirmation before execution. <br>
Risk: Process-management guidance may terminate services if the wrong process is selected. <br>
Mitigation: Verify process identity and ownership before terminating any process, and avoid running deployment commands as root where possible. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ascend-models-deploy) <br>
- [Deployment Task Steps](references/task-deploy-model.md) <br>
- [Testing Task Steps](references/task-test-model.md) <br>
- [Model Catalog](references/model-catalog.md) <br>
- [API Parameter Reference](references/api-parameters.md) <br>
- [Prerequisites Checklist](references/prerequisites.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Troubleshooting Guide](references/troubleshooting.md) <br>
- [Model Matching Helper](scripts/deploy_helper.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash, curl, JSON, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes model match results, deployment commands, inference test commands, prerequisite checks, log/status guidance, and confirmation prompts before sensitive execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
