## Description: <br>
Analyze candidate models before adapter implementation to determine implementation source, structural features, layer-by-layer loading requirements, and MoE fused weight risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to assess model adaptation feasibility before building msModelSlim adapters, including source detection, model structure classification, MoE compatibility, and quantization-related risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may require enabling trust_remote_code=True for model-local implementations, which can execute third-party model code. <br>
Mitigation: Only enable remote model code for trusted, pinned, and reviewed model repositories, preferably inside an isolated environment. <br>
Risk: Model analysis can produce incomplete adaptation guidance when implementation files, dequantization scripts, or MTP handling details are unavailable. <br>
Mitigation: Stop or mark blockers when required model code or scripts are missing, and require the user to provide readable implementation code or dequantization steps before continuing adaptation. <br>


## Reference(s): <br>
- [Analysis Checklist](references/analysis_checklist.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Verification Methods](references/verification-method.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-msmodelslim-model-analysis) <br>
- [Publisher Profile](https://clawhub.ai/user/erickeyhu-hug) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown analysis report with inline code and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces model feasibility findings, risk notes, blockers, and recommended next steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
