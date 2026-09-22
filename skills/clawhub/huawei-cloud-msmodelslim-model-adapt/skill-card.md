## Description:

Create basic Transformers model adapters for msModelSlim and verify W8A8/W4A16 quantization workflows for decoder-only LLMs and VLM text backbones.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create msModelSlim adapters for new Transformers models, register them, and run the four-step verification workflow before quantizing for Ascend deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Model-loading and quantization steps may execute model-supplied code when remote code is enabled.

Mitigation: Use only trusted, pinned model repositories or reviewed local model files, and avoid enabling remote code for untrusted models.

Risk: Adapter registration can require running installation scripts that modify the local environment.

Mitigation: Review install.sh effects and run registration in a controlled environment before deployment.

Risk: Unsafe or unexpected model weight formats may increase local execution or loading risk.

Mitigation: Prefer safetensors over pytorch_model.bin when preparing model files.

## Reference(s):

- [Model Analysis Guide](artifact/references/model_analysis.md)
- [Implementation Guide](artifact/references/implementation_guide.md)
- [Registration Guide](artifact/references/registration_guide.md)
- [Verification Guide](artifact/references/verification_guide.md)
- [Interface Checklist](artifact/references/interface_checklist.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with Python templates, YAML examples, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce adapter implementation steps, verification commands, and configuration edits for msModelSlim workflows.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
