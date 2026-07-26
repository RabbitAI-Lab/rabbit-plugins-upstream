## Description: <br>
Doctors and clinical researchers use this skill to turn clinical questions and supplied literature snippets into PICO-aligned framing, evidence narration, and follow-up search suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinicians and clinical research staff use this skill to draft literature-oriented answers, PICO restructuring, evidence summaries, and search-extension ideas from a clinical question and optional supplied title or abstract excerpts. It is intended as an assisted drafting and retrieval-planning workflow, not as a replacement for systematic review or full-text reading. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided clinical questions, constraints, and literature excerpts are sent to the documented remote medical model API. <br>
Mitigation: Do not include patient identifiers, protected health information, unpublished research, or confidential institutional material unless the organization has approved that data flow. <br>
Risk: The skill requires an app key for the remote medical model API. <br>
Mitigation: Treat the app key as a secret and avoid sharing it in prompts, logs, repositories, or generated outputs. <br>
Risk: Generated literature summaries and search suggestions may be incomplete or not anchored to full-text review. <br>
Mitigation: Use the output as a draft aid and verify conclusions against source literature, systematic review practices, and clinical judgment before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-literature-retrieval) <br>
- [hivoice medical model API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [JSON object containing metadata and Markdown text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Output includes status, normalized input metadata, passage count, and Markdown clinical literature guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
