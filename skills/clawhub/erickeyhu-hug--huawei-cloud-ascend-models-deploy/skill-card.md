## Description: <br>
Huawei Cloud Ascend model deployment and testing skill for large language models on Ascend DevServer (910B series), supporting single-machine and dual-machine deployment for LLM, vision-language, embedding, and rerank models with inference testing, log viewing, status monitoring, model matching, and deployment script generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to deploy, test, and monitor supported models on Huawei Cloud Ascend 910B DevServer environments. It helps select supported model scripts, generate deployment commands, check prerequisites, and produce inference test calls for chat, multimodal, embedding, and rerank endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can generate remote shell commands that download and run Huawei Cloud sample deployment scripts. <br>
Mitigation: Inspect the downloaded script, verify its source or checksum independently, and run only after confirming the target host, port, model, and card count. <br>
Risk: Deployment commands may run long-lived background processes on remote servers. <br>
Mitigation: Use a non-root account where possible, review logs and process status, and prefer graceful shutdown procedures before forceful termination. <br>
Risk: Incorrect deployment parameters can target the wrong host, occupied port, unsupported NPU type, or insufficient card count. <br>
Mitigation: Perform the documented prerequisite checks for Ascend 910B hardware, available cards, SSH access, disk space, and port availability before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-ascend-models-deploy) <br>
- [Deployment Task Steps](references/task-deploy-model.md) <br>
- [Testing Task Steps](references/task-test-model.md) <br>
- [Model Catalog](references/model-catalog.md) <br>
- [API Parameters](references/api-parameters.md) <br>
- [Prerequisites](references/prerequisites.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Huawei Cloud LLM Deployment Script](https://documentation-samples-17.obs.cn-north-9.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-module/quickly-deploy-llm-on-modelarts-lite-devserver/userdata/deploy-large-models/single-machine/deploy-large-models.sh) <br>
- [Huawei Cloud Vision-Language Deployment Script](https://documentation-samples-17.obs.cn-north-9.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-module/quickly-deploy-llm-on-modelarts-lite-devserver/userdata/deploy-vl-model/single-machine/deploy-qwen3-vl-model.sh) <br>
- [Huawei Cloud OpenSource Deployment Script](https://documentation-samples-17.obs.cn-north-9.myhuaweicloud.com/solution-as-code-publicbucket/solution-as-code-module/quickly-deploy-llm-on-modelarts-lite-devserver/userdata/deploy-large-models/single-machine/open_source/deploy-ai-models.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code, API Calls] <br>
**Output Format:** [Markdown guidance with inline bash commands, Python helper invocations, and HTTP API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces remote deployment commands and inference test requests that require user review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
