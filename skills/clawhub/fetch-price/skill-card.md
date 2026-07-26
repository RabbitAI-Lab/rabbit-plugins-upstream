## Description: <br>
AI agent marketplace for product discovery and affiliate commerce. Routes product queries to agents with affiliate network access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fusionx212](https://clawhub.ai/user/fusionx212) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and commerce developers use fetch-price to route product queries to affiliate-network-aware agents, receive tracked affiliate links and commission estimates, and compare prices across supported retail and travel networks. <br>

### Deployment Geography for Use: <br>
Global, with artifact examples centered on UK affiliate networks and trade coverage. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles affiliate credentials and generated fp_ API keys with weak disclosure and insecure persistence. <br>
Mitigation: Review credential scope, storage, rotation, and deletion before production use; rotate any included fp_ API keys; use managed or hashed secrets instead of plaintext JSON storage. <br>
Risk: Query and sale logs may contain commercially sensitive product, requester, and commission data. <br>
Mitigation: Define retention controls, minimize logged fields, and review access controls before deployment. <br>
Risk: The Flask API artifact can run with debug mode enabled. <br>
Mitigation: Disable debug mode and deploy behind a production WSGI server before handling real traffic. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fusionx212/skills/fetch-price) <br>
- [Publisher profile](https://clawhub.ai/user/fusionx212) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API examples, JSON request shapes, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe affiliate links, commission estimates, routing results, and registration requirements.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
