## Description: <br>
帮助用户把寻找联合创始人、技术合伙人、CTO 或创业搭档的需求整理为可匹配的私密发布内容，并通过 Pairoa 在互补需求出现时撮合双方。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pairoa](https://clawhub.ai/user/pairoa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and their agents use this skill when they want to find a cofounder, technical partner, CTO, or other early startup collaborator. The skill clarifies role, stage, commitment, location, user contribution, and contact email before submitting a private Pairoa matching request with explicit user consent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow shares the user's cofounder-search description and contact email with Pairoa and, after a match, with another person. <br>
Mitigation: Show the final i_seek, i_offer, and contact email to the user and obtain explicit consent before publishing. <br>
Risk: Initial requests may include sensitive personal, financial, legal, equity, or identity information. <br>
Mitigation: Omit sensitive documents and sensitive deal terms from the initial request; discuss them only after a match and appropriate verification. <br>
Risk: Pairoa does not verify matched people's identity, résumé, company, financing, or equity claims. <br>
Mitigation: Independently verify identity and claims before discussing equity, money, intellectual property, employment, visas, or sensitive materials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pairoa/skills/pairoa-cofounder) <br>
- [Publisher profile](https://clawhub.ai/user/pairoa) <br>
- [Pairoa MCP connection](https://mcp.pairoa.com) <br>
- [SkillHub install entry](https://pairoa.com/r/skillhub-install) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, API Calls] <br>
**Output Format:** [Conversational text with structured i_seek, i_offer, contact email, consent prompts, and Pairoa MCP tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user consent before publishing contact details; does not browse public candidate lists.] <br>

## Skill Version(s): <br>
1.0.2 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
