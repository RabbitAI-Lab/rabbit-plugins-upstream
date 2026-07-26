## Description: <br>
Reviews insurance claim case text and asks a configured medical model to classify a specified body part as chronic injury, new injury, no injury, or not mentioned. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Claims reviewers and insurance workflow developers use this skill to submit OCR or manually prepared imaging-report text and receive an auxiliary injury-category assessment in the requested format. It is intended to support review, not to provide forensic determination or the final claim decision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user-provided medical claim text to the configured medical-model endpoint. <br>
Mitigation: Use it only when that transfer is allowed, and remove names, IDs, imaging numbers, and other sensitive identifiers before use. <br>
Risk: The optional output file can save the full question and model result. <br>
Mitigation: Use --output only when persistent storage is intended and the destination is approved for the case content. <br>
Risk: The model response is an auxiliary review signal and may be unsuitable as a final claim or forensic decision. <br>
Mitigation: Keep human review in the workflow and apply the insurer's normal medical, legal, and claims controls before acting on the result. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-chronic-injury) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration] <br>
**Output Format:** [JSON by default, plain text with --text-only, and optional UTF-8 JSON or NDJSON file output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an app key except in dry-run mode; accepts question text, JSON, JSONL, plain text files, or stdin.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
