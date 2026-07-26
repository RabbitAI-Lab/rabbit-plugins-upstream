## Description: <br>
Interprets abnormal items in health exam reports by explaining what each abnormality means, likely causes, health impact, interventions, and related multi-indicator patterns in JSON plus narrative text. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Health management teams and developers use this skill to generate plain-language abnormal-item interpretations from health exam reports or abnormal indicator lists. The output supports educational review workflows and does not replace clinician diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive health-report content is sent to a configured remote medical model endpoint. <br>
Mitigation: Use the skill only when that transfer is acceptable, and de-identify reports before running it. <br>
Risk: Saved outputs can contain sensitive medical data. <br>
Mitigation: Store outputs in controlled locations, restrict access, and avoid retaining them longer than needed. <br>
Risk: API keys can be exposed when passed on shared systems via command-line arguments. <br>
Mitigation: Use a protected secret-handling workflow where available and avoid command-line keys on shared systems. <br>
Risk: The security summary says privacy behavior is not fully disclosed or implemented as promised. <br>
Mitigation: Review the package before installing and confirm its data-handling behavior matches operational requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-abnormal-items) <br>
- [Publisher profile](https://clawhub.ai/user/unisound-llm) <br>
- [Remote medical model API base](https://maas-api.hivoice.cn/v1) <br>
- [Remote medical model chat completions endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Text, Guidance, Files] <br>
**Output Format:** [JSON followed by narrative text, optionally saved as a UTF-8 file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces one detailed interpretation stream per input report or abnormal-indicator list.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
