## Description: <br>
Provides health consultation, medical checkup interpretation, and department-routing guidance by sending user questions to a configurable medical-model chat API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and integrators use this skill to route health-consultation, medical-checkup interpretation, and clinic-department recommendation prompts through a documented medical model endpoint. It supports direct questions, JSON or JSONL input files, stdin input, dry-run inspection, and optional text-only output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Health consultation prompts may contain identifiable patient information and are sent to the documented or configured medical-model API. <br>
Mitigation: De-identify patient data and confirm the organization has approved that data flow before making live API calls. <br>
Risk: Model answers may be mistaken for formal diagnosis or treatment decisions. <br>
Mitigation: Treat outputs as auxiliary information only and require appropriate clinical review before acting on them. <br>
Risk: Incorrect task selection or malformed input can send the wrong prompt context to the model. <br>
Mitigation: Use --dry-run to inspect parsed questions, task selection, and metadata before calling the model. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-med-health-consult) <br>
- [Default medical model API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, guidance] <br>
**Output Format:** [JSON by default, plain answer text with --text-only, or NDJSON for batch output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes status, task, task_title, question, answer, record index, metadata, model, input mode, and optional output-file writing.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
