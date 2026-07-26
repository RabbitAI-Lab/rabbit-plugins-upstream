## Description: <br>
AITOP.NEWS helps agents fetch public AI news updates and daily digests from AITOP without an API key or MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[funewa](https://clawhub.ai/user/funewa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to answer questions about recent AI news, category-specific updates, keyword searches, and AITOP daily digests while preserving source links for verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User news queries may be sent to aitop.news. <br>
Mitigation: Avoid using the skill for sensitive queries and make the external request behavior clear where that matters. <br>
Risk: Returned summaries may be LLM-generated and may omit or misstate details. <br>
Mitigation: Retain source links in outputs and verify important claims against the original articles before relying on or citing them. <br>


## Reference(s): <br>
- [AITOP.NEWS on ClawHub](https://clawhub.ai/funewa/skills/aitop) <br>
- [AITOP.NEWS](https://aitop.news) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown summaries with source links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Retains original source URLs and labels LLM-generated summaries as material to verify before relying on or citing important claims.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
