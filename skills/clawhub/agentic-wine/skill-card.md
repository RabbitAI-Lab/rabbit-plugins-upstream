## Description:

Turn a brand, luxury product or event into an original regenerative wine concept, constructor dossier and producer-ready commission through Vin-Q.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vbaulin](https://clawhub.ai/user/vbaulin)

### License/Terms of Use:

MIT-0

## Use Case:

External adult users, brand teams, hospitality teams, event planners, and advisors use this skill to turn a brand, luxury product, institution, or event brief into a producer-ready Vin-Q wine commission dossier. It guides concept selection, wine architecture, evidence requirements, label planning, consent, and next actions for producer feasibility review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prepare wine commission details for an external Vin-Q workflow that shares submitted name, contact email, and dossier information with registered producers.

Mitigation: Obtain explicit user authorization before entering personal or corporate data, before enabling producer sharing, and before final submission.

Risk: Wine commissions and related delivery are adult-use alcohol activities with destination-specific legal, tax, shipping, and age-verification requirements.

Mitigation: Confirm the user is an adult, avoid targeting minors, and require the legal seller and carrier to verify age and destination-specific sale and delivery rules.

Risk: Unverified availability, delivery timing, price, certification, protected designation, or production capacity claims could mislead the user.

Mitigation: Use the current Vin-Q website or constructor for live claims, keep missing evidence visible, and treat the dossier as a request until producer and contract confirmation.

Risk: Sensitive guest lists, passwords, payment details, authentication codes, or confidential brand assets could be exposed if included in the dossier.

Mitigation: Exclude unnecessary sensitive data, let users enter credentials and authentication factors themselves, and submit only fields required for the commission request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vbaulin/skills/agentic-wine)
- [Vin-Q landing page](https://vin-q.com/)
- [Vin-Q live constructor](https://vin-q.com/co-creators#alchemist)
- [Vin-Q agent instructions](https://vin-q.com/agents)
- [Vin-Q agent discovery](https://vin-q.com/.well-known/agent.json)
- [Vin-Q A2A agent card](https://vin-q.com/.well-known/agent-card.json)
- [Vin-Q A2A HTTP+JSON interface](https://vin-q.com/a2a)
- [Vin-Q LLM index](https://vin-q.com/llms.txt)
- [Vin-Q OpenAPI contract](https://vin-q.com/openapi.json)
- [Vin-Q Constructor API](https://vin-q.com/api/constructor/dossier)
- [Vin-Q Method model](references/method-model.md)
- [Vin-Q Constructor Workflow](references/design-workflow.md)
- [Style Routes](references/style-routes.md)
- [Brand and Label Construction](references/brand-label.md)
- [Evidence and Compliance](references/evidence-compliance.md)
- [New Wine Commission Profile](references/commission-profile.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown dossier with optional JSON commission profile and shell validation command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Decision-ready commission dossier; API responses remain drafts for producer feasibility review.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
