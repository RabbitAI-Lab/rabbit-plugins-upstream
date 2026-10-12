## Description:

Turns natural-language descriptions of processes, system interactions, states, and data relationships into editable diagrams that users can review and export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can draft flowcharts, sequence diagrams, state diagrams, entity-relationship diagrams, and architecture diagrams from natural language, review their structure, and explicitly request an export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagram prompts and related task data are sent to the AI Skills service.

Mitigation: Avoid including secrets or sensitive internal details unless sharing them with the service is acceptable.

Risk: A generated diagram may omit exceptions or misrepresent processes and relationships.

Mitigation: Have a knowledgeable user review the nodes and relationships before requesting an export.

Risk: API credentials and private exports could be exposed through careless handling.

Mitigation: Keep the API key confidential and share private artifacts only with the requesting user; obtain separate consent before publishing or forwarding them.

Risk: Retrying an uncertain request with a new key could create duplicate paid tasks.

Mitigation: Retry only with the original idempotency key and identical input; stop and reconcile conflicts or uncertain billing states.

## Reference(s):

- [ClawHub diagram-generation release](https://clawhub.ai/youteacher/skills/diagram-generation)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key and pricing](https://ai-skills.open-idea.net/skill-docs/diagram-generation/API-KEY.md)
- [Diagram operations and exports](https://ai-skills.open-idea.net/skill-docs/diagram-generation/OPERATIONS.md)
- [HTTP requests and task polling](https://ai-skills.open-idea.net/skill-docs/diagram-generation/HTTP-REQUESTS.md)
- [Review and delivery guidance](https://ai-skills.open-idea.net/skill-docs/diagram-generation/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [Structured diagram plan and, on explicit request, private SVG, PNG, PDF, or JSON exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to 100 nodes and 200 relationships; exports require user review and an explicit request.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
