## Description: <br>
Create basic Transformers model adapters for msModelSlim and verify them through test-model generation, fallback quantization, weight comparison, and quantization-description validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create and register msModelSlim adapters for decoder-only LLMs and understanding VLM text backbones, then verify W8A8/W4A16 quantization readiness before Ascend deployment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can load model repositories with trust_remote_code=True, which may execute code from the selected model repository. <br>
Mitigation: Use only trusted and reviewed model repositories, pin exact revisions, avoid trust_remote_code=True for untrusted models, and run verification in an isolated environment. <br>
Risk: Adapter registration and installation can change the local msModelSlim setup through config.ini edits and install.sh execution. <br>
Mitigation: Review registration changes before installation, keep backups or use a disposable environment, and install only after the four-step verification workflow is understood. <br>


## Reference(s): <br>
- [Model Analysis Guide](references/model_analysis.md) <br>
- [Implementation Guide](references/implementation_guide.md) <br>
- [Registration Guide](references/registration_guide.md) <br>
- [Verification Guide](references/verification_guide.md) <br>
- [Interface Checklist](references/interface_checklist.md) <br>
- [Core Workflow](references/core_workflow.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with Python templates, shell commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended to guide adapter implementation and verification rather than execute autonomously.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
