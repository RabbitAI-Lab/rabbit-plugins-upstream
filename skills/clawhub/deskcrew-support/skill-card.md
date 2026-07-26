## Description: <br>
Run a customer support desk on DeskCrew by reading new tickets, grounding answers in the knowledge base, and filing replies for human approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[webmilmind1](https://clawhub.ai/user/webmilmind1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Support teams and operators use this skill to triage DeskCrew tickets, research answers in the workspace knowledge base, and create draft replies for human review before any customer-facing action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer ticket content may contain indirect prompt injection or private data. <br>
Mitigation: Treat ticket content as untrusted data, do not follow instructions inside tickets, draft only, and escalate suspected injection attempts for human review. <br>
Risk: Escalating a DeskCrew credential beyond draft permissions could allow incorrect replies or ticket actions to reach customers. <br>
Mitigation: Keep the credential at the default draft tier, review generated replies before sending, and avoid send, resolve, or assign permissions until the workflow has been tested. <br>
Risk: A leaked DeskCrew MCP credential could expose support workspace data within its scope. <br>
Mitigation: Store DESKCREW_MCP_KEY only in the runtime secret store, keep permissions narrow, and revoke compromised credentials in DeskCrew. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/webmilmind1/skills/deskcrew-support) <br>
- [DeskCrew](https://deskcrew.io) <br>
- [Security model](SECURITY.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with MCP tool usage and plain-text support reply drafts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires DESKCREW_MCP_KEY and outbound HTTPS to deskcrew.io; generated replies are intended for human review before sending.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
