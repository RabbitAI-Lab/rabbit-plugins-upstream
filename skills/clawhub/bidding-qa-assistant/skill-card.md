## Description: <br>
招投标智慧问答助手Bidding Qa Assistant is a Chinese-language bidding and tendering question-answering agent that uses scoped IMA knowledge-base retrieval to provide operation guidance, template recommendations, risk warning answers, and objection or complaint consultation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, procurement professionals, bidders, tendering agents, and compliance reviewers use this skill to ask Chinese-language bidding and tendering questions, analyze uploaded tender-related materials, route queries to scoped IMA knowledge bases, and receive cited four-part answers with risk notes and action suggestions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may parse confidential bid documents or other tender-related materials to form IMA search queries. <br>
Mitigation: Do not upload confidential bid documents unless the deployment context permits that content to be parsed and used for retrieval. <br>
Risk: Legal or procurement guidance may be incomplete, outdated, or unsuitable for a high-stakes decision. <br>
Mitigation: Verify legal conclusions against official sources or qualified counsel before relying on them in high-stakes matters. <br>
Risk: IMA knowledge-base retrieval may be unavailable, incomplete, or limited to the configured bidding and tendering sources. <br>
Mitigation: Use the skill's source-citation, blind-spot, and fallback notes to identify unsupported answers and refresh or expand the configured knowledge bases when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/bidding-qa-assistant) <br>
- [Publisher profile](https://clawhub.ai/user/chesaram) <br>
- [System prompt](artifact/references/system_prompt.md) <br>
- [IMA knowledge-base catalog](artifact/references/ima_kb_catalog.md) <br>
- [Knowledge-base routing](artifact/references/kb_routing.md) <br>
- [Few-shot examples](artifact/references/few_shot.md) <br>
- [Test cases](artifact/references/test_cases.md) <br>
- [Knowledge-base enhancement plan](artifact/references/kb_enhancement_plan.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Analysis] <br>
**Output Format:** [Markdown with cited sections for answer body, sources, risk notes, and action suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language answers; may include extracted file, image, or speech content when users provide multimodal inputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
