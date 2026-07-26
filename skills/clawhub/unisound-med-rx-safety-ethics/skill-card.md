## Description: <br>
Helps route prescription review, medical safety, and medical ethics questions to a configured medical LLM and returns answers in the requested format. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and integrators can use this skill to submit structured prescription review, medical safety, or medical ethics questions to a medical LLM workflow. It supports direct question text, JSON, JSONL, plain-text files, stdin, dry-run parsing, batch selection, and optional text-only output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Question text is sent to the configured external medical-model API. <br>
Mitigation: Do not include patient identifiers or protected health information unless the workflow has been approved by the organization. <br>
Risk: Medical answers may be incomplete, incorrect, or unsuitable for formal clinical decisions. <br>
Mitigation: Treat output as model-assisted information and review it through appropriate clinical and organizational processes before use. <br>
Risk: A live API call requires a valid app key and sends the submitted question over the network. <br>
Mitigation: Use --dry-run when only validating input parsing or task selection. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-med-rx-safety-ethics) <br>
- [Configured medical model API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files] <br>
**Output Format:** [JSON by default, with optional plain-text answers or NDJSON batch output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write UTF-8 result files; --dry-run returns parsed question metadata without calling the external API.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
