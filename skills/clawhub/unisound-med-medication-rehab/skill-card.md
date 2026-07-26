## Description: <br>
Provides medication consultation, personalized medication education, and rehabilitation guidance Q&A through task-specific prompts for a configured medical LLM. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and clinical application teams use this skill to route medication, treatment-plan, medication-education, and rehabilitation questions to a medical LLM and return structured answers. The output is model-assisted information and is not a substitute for formal prescribing, diagnosis, or clinical decision-making. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Medical questions may contain patient identifiers or regulated health information that are sent to the configured API service. <br>
Mitigation: Remove patient identifiers and regulated health information unless the organization has approved the endpoint, key handling, and retention policy. <br>
Risk: Model answers could be mistaken for formal diagnosis, prescribing instructions, or clinical decisions. <br>
Mitigation: Use the output as assistive information only and require qualified clinical review before relying on it for patient care. <br>
Risk: The skill requires an API key for non-dry-run calls to the configured medical LLM endpoint. <br>
Mitigation: Provide credentials through approved secret-management practices and avoid logging or sharing API keys in prompts, files, or command history. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-med-medication-rehab) <br>
- [Configured medical LLM API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [JSON, NDJSON for batch output, or plain text when text-only output is requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports task selection, question input from arguments, files, or stdin, dry-run parsing, and optional result file output.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
