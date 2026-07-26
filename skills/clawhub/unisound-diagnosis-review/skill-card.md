## Description: <br>
Reviews diagnosis codes against structured medical case records, coding rules, and chart evidence, then returns an audit decision and concise rationale. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and clinical coding teams use this skill to audit submitted diagnosis codes against a structured case record, rule-library evidence, and medical-document support. It is intended as insurance coding assistance and does not provide diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes medical case records that may contain patient data. <br>
Mitigation: Install and run it only in environments approved for patient data, and redact direct identifiers before input. <br>
Risk: Rules, model calls, or saved outputs may send or persist sensitive medical information when configured that way. <br>
Mitigation: Configure GUIDELINE_API_BASE and --base only to trusted internal services, use --no-llm when external processing is not allowed, and avoid --save-prepared or output paths unless persistence is intentional. <br>
Risk: Coding audit output may be incomplete or uncertain for ambiguous clinical evidence. <br>
Mitigation: Treat pass, fail, and manual-review decisions as coding assistance and require human review for uncertain or high-impact cases. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-diagnosis-review) <br>
- [Internal medical model API base](https://maas-api.hivoice.cn/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [JSON response with final_decision and reasoning fields; setup and usage guidance may include Markdown with shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI prints JSON only. Decisions are limited to pass, fail, or manual review, and reasoning is concise user-facing evidence rather than chain-of-thought.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
