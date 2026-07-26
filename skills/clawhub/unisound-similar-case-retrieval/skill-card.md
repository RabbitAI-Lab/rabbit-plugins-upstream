## Description: <br>
Clinical research assistant for semantic retrieval and explainable ranking of similar cases against an anchor case. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinical researchers and educators use this skill to compare a de-identified anchor case with a prepared candidate pool and receive a ranked Markdown interpretation with similarity rationale and research prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends de-identified clinical summaries to a documented remote model endpoint, which can create privacy and compliance exposure if identifiable patient data or unapproved processing is used. <br>
Mitigation: Use only de-identified summaries and install only when the organization has approved the processor, retention policy, app key handling, and ethics or compliance requirements. <br>
Risk: AI-generated similarity ranking and research prompts may be incomplete or misleading if treated as clinical advice. <br>
Mitigation: Use outputs only for clinical research, teaching, or methodology discussion, and require qualified human review before applying any finding. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-similar-case-retrieval) <br>
- [Unisound-LLM publisher profile](https://clawhub.ai/user/unisound-llm) <br>
- [Configured medical model endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json] <br>
**Output Format:** [JSON object containing structured case metadata and Markdown analysis text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes anchor case echo, candidate count, top_k, candidate IDs, similarity rationale, research prompts, and a research-use disclaimer.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
