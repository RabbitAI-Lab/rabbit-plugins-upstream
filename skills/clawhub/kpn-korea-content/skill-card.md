## Description: <br>
When an agent needs judgment about Korean content such as K-pop, drama, webtoon, beauty, games, or film, this skill submits a decision-oriented question to the KPN advisory network and relays the verified verdict, sources, trust score, and audit information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bitcard1-art](https://clawhub.ai/user/bitcard1-art) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and developers use this skill when they need a business or regulatory judgment about Korean content, IP commercialization, market entry, partnerships, contracts, or cultural context. It is intended for risky decisions where the agent should relay a verified Go, Conditional Go, or Hold verdict rather than make its own unsupported call. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Korean-content business questions are sent to an external advisory service. <br>
Mitigation: Use the skill only for questions the user is comfortable sending to persona-mcp-server.onrender.com, and avoid including unnecessary sensitive details. <br>
Risk: Optional contact registration may transmit email, webhook, wallet, or operator details. <br>
Mitigation: Provide contact fields only when the user explicitly asks to be notified about paid-tier resumption. <br>
Risk: A returned advisory verdict could be mistaken for authorization to act. <br>
Mitigation: Relay the verdict as advice only, preserve HOLD outcomes, and do not make payments, sign contracts, or negotiate on the user's behalf. <br>


## Reference(s): <br>
- [KPN homepage](https://kpn.mysoma.space) <br>
- [ClawHub skill listing](https://clawhub.ai/bitcard1-art/skills/kpn-korea-content) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown summary with returned JSON fields and citations relayed from the advisory result] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Async advisory workflow; submit a question, poll for completion, then present the returned verdict, sources, trust score, and audit ID without overriding HOLD outcomes.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
