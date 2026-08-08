## Description: <br>
Create basic Transformers model adapters for msModelSlim and verify W8A8/W4A16 quantization workflows for decoder-only LLMs and understanding VLM text backbones. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create msModelSlim adapters for custom decoder-only LLMs or understanding VLM text backbones, register those adapters, and run the required four-step quantization verification workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Model loading during adapter verification may execute code from model artifacts. <br>
Mitigation: Use trusted and reviewed model sources only, pin model revisions, and run verification in an isolated development environment. <br>
Risk: Verification scripts and registration workflows may be run against arbitrary downloaded model directories. <br>
Mitigation: Review model files and generated adapter changes before execution, and avoid running the workflow on untrusted Hugging Face, ModelScope, or local model directories. <br>
Risk: Registration requires running install.sh after config changes. <br>
Mitigation: Inspect install.sh and related configuration updates before running them. <br>


## Reference(s): <br>
- [Model Analysis Guide](artifact/references/model_analysis.md) <br>
- [Implementation Guide](artifact/references/implementation_guide.md) <br>
- [Interface Reference](artifact/references/interface_reference.md) <br>
- [Registration Guide](artifact/references/registration_guide.md) <br>
- [Verification Guide](artifact/references/verification_guide.md) <br>
- [Verification Methods](artifact/references/verification-method.md) <br>
- [Acceptance Criteria](artifact/references/acceptance-criteria.md) <br>
- [Troubleshooting](artifact/references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python code, YAML configuration, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Focuses on adapter creation, registration, and four-step verification for msModelSlim quantization workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
