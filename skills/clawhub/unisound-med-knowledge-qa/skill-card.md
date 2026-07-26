## Description: <br>
Runs medical knowledge Q&A tasks for exams, specialty questions, literature comprehension, terminology explanation, and synonym matching by sending caller-provided questions to a configured medical model API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and healthcare application integrators use this skill to pass medical questions into a task-specific prompt wrapper and receive model-generated answers or parsed dry-run output. Outputs are model-assisted information and are not formal clinical decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted medical questions may contain identifiable patient information and are sent to the configured model API. <br>
Mitigation: Do not submit identifiable patient data unless the endpoint and workflow are approved by the organization; use --dry-run to inspect parsed inputs without making a network call. <br>
Risk: Model-generated medical answers may be incomplete, incorrect, or unsuitable for a specific patient context. <br>
Mitigation: Treat answers as assistive information only and require qualified human review before clinical or operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-med-knowledge-qa) <br>
- [Configured medical model API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, files] <br>
**Output Format:** [JSON or NDJSON by default, plain answer text with --text-only, and optional UTF-8 output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports single-question input, JSON/JSONL/text/stdin input, jsonl batching, dry-run parsing, and configurable model API parameters.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
