## Description: <br>
Analyze candidate models before adapter implementation by determining implementation source, structural features, layer-by-layer loading requirements, and MoE fused weight risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to assess whether candidate LLM or VLM text-backbone models can be adapted for msModelSlim quantization workflows. It helps identify implementation-source, structure, MoE, quantization, and MTP risks before adapter creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Following the troubleshooting path with trust_remote_code=True can execute model-provided Python code. <br>
Mitigation: Prefer static inspection of config.json and model code; use trust_remote_code=True only after the model repository is trusted and reviewed. <br>
Risk: The skill may suggest package upgrades or model file downloads as part of troubleshooting. <br>
Mitigation: Require user confirmation before upgrading packages or downloading model files, and download only the non-weight files needed for analysis when possible. <br>
Risk: Incorrect model-source, MoE, quantization, or MTP classification can lead to unsuitable adapter work. <br>
Mitigation: Verify the generated analysis report against the bundled checklist, acceptance criteria, and verification methods before proceeding to adapter creation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-msmodelslim-model-analysis) <br>
- [Analysis Checklist](references/analysis_checklist.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Verification Methods](references/verification-method.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown analysis report with structured findings and inline code or shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires readable model configuration and, when needed, local model implementation files for source and structure analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
