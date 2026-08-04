## Description: <br>
Pairoa helps an agent privately publish a user's two-sided need and offer, connect to the Pairoa MCP service, and check for AI-matched counterparties without creating a public listing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pairoa](https://clawhub.ai/user/pairoa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to publish private matching requests for hiring, jobs, customers, partners, investors, roommates, travel companions, beta testers, and second-hand buying or selling. The skill guides the agent through consent, email verification, match polling, match presentation, and safe handling of counterparties. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The user's stated need, offer, and contact email are sent to Pairoa and may be shared with a matched counterparty. <br>
Mitigation: Show the final need, offer, contact email, and disclosure consequences to the user, remove sensitive details on request, and publish only after explicit consent. <br>
Risk: Pairoa matches by stated intent and does not verify the counterparty's identity or claims. <br>
Mitigation: Tell users to independently verify counterparties, roles, goods, resumes, investment details, and payment arrangements before sharing sensitive information or transacting. <br>
Risk: Retrying an uncertain publish operation may create duplicate needs. <br>
Mitigation: Do not automatically retry write operations after an unclear timeout; check status or recover by verified email before asking the user to confirm any resend. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pairoa/skills/pairoa) <br>
- [Pairoa MCP service](https://mcp.pairoa.com) <br>
- [Pairoa installation guide](https://pairoa.com/install) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, API Calls, Configuration] <br>
**Output Format:** [Markdown guidance with MCP tool-call instructions and user-facing safety text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before publishing needs or disclosing contact information.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
