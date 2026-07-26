## Description: <br>
Runs medical-insurance LLM prompts for claim-document compliance review and insurance-fee calculation tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and healthcare workflow integrators use this skill to submit medical-insurance questions for claim-document compliance review or insurance-fee calculation support. Outputs are model-assisted answers and should be reviewed before operational use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Insurance, medical, patient, claim, billing, or policyholder data may be sent to the configured model service. <br>
Mitigation: De-identify real data before use, follow institutional handling procedures, and send requests only to the default or another trusted endpoint. <br>
Risk: Custom system prompts or API URLs can change behavior or route data to untrusted services. <br>
Mitigation: Restrict overrides to reviewed prompts and trusted endpoints, and review model answers before relying on them in medical-insurance workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-med-insurance-fee) <br>
- [Default model API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [JSON by default, with optional plain text answer output and NDJSON for batches] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a task selection and an app key for non-dry-run model calls; supports file, stdin, and direct question inputs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
