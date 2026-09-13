## Description:

Errand AI helps an agent send a real person to a physical place in Seoul's Gangnam area to check, photograph, verify, queue, or pick something up and return GPS and photo evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chloepark85](https://clawhub.ai/user/chloepark85)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill when they need on-site observation or simple physical assistance in the supported Seoul area, such as checking store status, photographing a menu, verifying shelf availability, queueing, or picking up an item.

### Deployment Geography for Use:

South Korea (Seoul Gangnam district and nearby supported areas)

## Known Risks and Mitigations:

Risk: The skill requires an Errand API key and sends task and location details to errand.be and a human worker.

Mitigation: Use it only for locations and task details the user is comfortable sharing with Errand and the dispatched worker.

Risk: Dispatching a mission escrows prepaid KRW, and a mission cannot be cancelled after a worker accepts it.

Mitigation: Check coverage and quote first, state the total price, and dispatch only after the user explicitly approves the cost.

Risk: Mission results can include signed photo URLs and location evidence.

Mitigation: Present or store result evidence promptly and avoid unnecessary sharing of signed links or precise location details.

## Reference(s):

- [Errand homepage](https://errand.be)
- [ClawHub skill page](https://clawhub.ai/chloepark85/skills/errand-ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return mission status updates, structured answers, signed photo URLs, GPS evidence, and verification verdicts from Errand missions.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
