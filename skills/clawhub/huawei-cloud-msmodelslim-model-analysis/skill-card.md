## Description:

Analyzes candidate models before msModelSlim adapter implementation by identifying implementation source, model structure, layer-loading needs, and MoE fused-weight risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to assess whether decoder-only LLMs and VLM text backbones are suitable for msModelSlim adapter work before implementation. It produces a structured analysis of implementation source, architecture, MoE layout, quantization and MTP risks, and next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may involve inspecting model-local Python files or troubleshooting with trust_remote_code=True, which can execute code from a model repository.

Mitigation: Use the skill only with trusted or reviewed model repositories, prefer static inspection of config.json and modeling files, and run any required remote-code execution in a disposable sandbox without secrets or writable host access.

Risk: The analysis can be incomplete when model implementation files, dequantization scripts, or MTP implementation code are unavailable.

Mitigation: Stop or mark the analysis as blocked when required files are missing, and require the user to provide readable implementation code or dequantization/MTP handling before continuing adapter work.

## Reference(s):

- [Analysis Checklist](references/analysis_checklist.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Verification Method](references/verification-method.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown analysis report with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a model path or repository identifier and config.json; may request model-local implementation files when source detection cannot proceed.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
