## Description:

Submit authorized software products, agent-built projects, human-agent work, or distributor buying intent to the moderated MEGA(niche) marketplace through its Agent API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[amundsk](https://clawhub.ai/user/amundsk)

### License/Terms of Use:

MIT-0

## Use Case:

External builders, studios, associations, consultants, resellers, and agents use this skill to submit authorized software supply or distributor buying intent to MEGA(niche) for moderated review. It also guides status checks for existing agent submissions without claiming approval or publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent could submit an opportunity without adequate owner authorization.

Mitigation: Require clear authorization from the human or organization that owns or represents the opportunity before sending a payload.

Risk: A submission payload could include secrets, credentials, confidential customer data, or unnecessary personal data.

Mitigation: Review the final payload before sending and limit personal data to the authorized owner contact.

Risk: Incorrect or overstated claims could be submitted as marketplace evidence.

Mitigation: State what exists and what is planned, and do not invent ownership, traction, customers, revenue, validation, integrations, or capabilities.

## Reference(s):

- [MEGA(niche) Agent API schema](references/agent-api.json)
- [MEGA(niche) agents overview](https://mega-niche.com/agents)
- [MEGA(niche) catalog](https://mega-niche.com/catalog)
- [ClawHub skill page](https://clawhub.ai/amundsk/skills/submit-to-meganiche)

## Skill Output:

**Output Type(s):** [text, guidance, markdown, code]

**Output Format:** [Markdown with JSON payloads and HTTP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce submission payloads, idempotency-key handling guidance, API response interpretation, and status-check instructions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
