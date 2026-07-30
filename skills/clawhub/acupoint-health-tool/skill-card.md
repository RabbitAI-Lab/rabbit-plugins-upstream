## Description: <br>
Connects agents to the AI_Health MCP service for classical-text-backed Chinese acupoint massage consultations, multi-turn symptom clarification, reference-book listing, and shareable consultation results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dengkane](https://clawhub.ai/user/dengkane) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect an agent or MCP client to the AI_Health service for acupoint consultation workflows, including clarification questions, sourced final guidance, and sharing of consultation transcripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Symptom descriptions and consultation transcripts may be sent to the remote AI_Health service. <br>
Mitigation: Review the service behavior before installation and avoid entering sensitive personal health details unless that data sharing is acceptable. <br>
Risk: The skill instructs agents to derive a persistent client ID from local machine identifiers, hostname, and username, which can link consultations from the same device over time. <br>
Mitigation: Send only the derived hash as described by the skill and avoid sending raw machine identifiers, hostnames, usernames, MAC addresses, or other fingerprint source values. <br>
Risk: Share links may expose consultation conversations to anyone who receives the URL. <br>
Mitigation: Create and distribute share links only when the user intends to share the transcript and understands that recipients can view the conversation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dengkane/skills/acupoint-health-tool) <br>
- [AI_Health service](https://health.geeyo.com) <br>
- [AI_Health MCP endpoint](https://health.geeyo.com/mcp) <br>
- [AI_Health legacy SSE endpoint](https://health.geeyo.com/mcp/sse) <br>
- [AI_Health MCP raw protocol examples](references/protocol_examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to call remote MCP tools that return JSON text and final Markdown consultation responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
