## Description: <br>
Clinical researchers and physicians use this skill to expand provided section notes into Chinese or English IMRaD-style manuscript draft paragraphs with reporting checklist reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External clinicians, clinical researchers, and medical writing teams can use this skill to turn explicitly provided study notes into manuscript section drafts and writing self-check reminders. Authors remain responsible for verifying all scientific content before use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided notes are sent to a remote model API. <br>
Mitigation: Use only when the endpoint and app key handling are approved, and do not include patient identifiers, regulated health information, or confidential unpublished study details without authorization. <br>
Risk: Generated manuscript draft text may be incomplete, misleading, or unsuitable for direct submission. <br>
Mitigation: Require author review, revision, and verification of all scientific claims, statistics, and conclusions before using the draft. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-paper-writing-assist) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/unisound-llm) <br>
- [Remote model API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [JSON object containing Markdown text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes draft section text, selected section and language metadata, note count, and writing self-check reminders.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
