## Description: <br>
Helps doctors choose the most likely ICD/DRG grouping from discharge-note text and candidate DRG options using a configured medical model endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and clinical evaluation teams use this skill to submit DRG candidate-selection prompts, compare the model's selected grouping with reference cases, and capture structured results for review. The output is an auxiliary grouping suggestion, not a formal insurance settlement or hospital grouping decision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Medical case text sent to the configured model endpoint may contain patient data. <br>
Mitigation: Use the skill only where that processing is permitted, de-identify real patient data before use, and follow the organization's medical data handling process. <br>
Risk: The DRG grouping answer could be mistaken for an official billing or hospital grouping result. <br>
Mitigation: Treat the answer as an auxiliary model suggestion and require qualified review before using it in operational or reimbursement workflows. <br>
Risk: Standard output and files written with --output can contain sensitive case text, metadata, and model answers. <br>
Mitigation: Avoid piping full JSON traces into shared logs, use --text-only when the trace is unnecessary, and store output files as sensitive records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-drg-grouping) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files] <br>
**Output Format:** [JSON on stdout by default; plain text with --text-only; optional JSON or NDJSON file with --output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The model answer is expected as a single DRG code/name line; batch JSONL input emits one JSON object per line.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
