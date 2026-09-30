## Description:

Helps an agent send a local worker to check, photograph, verify, queue, or pick up something in Seoul and report answers with GPS and photo evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chloepark85](https://clawhub.ai/user/chloepark85)

### License/Terms of Use:

MIT-0

## Use Case:

People who need an on-site check in Seoul can ask an agent to obtain a quote, dispatch a local worker after approving the total price, and receive verified answers and photos. Tasks include checking business hours, queues, signage, and product availability.

### Deployment Geography for Use:

Seoul, South Korea (initially Gangnam / Yeoksam; check live coverage)

## Known Risks and Mitigations:

Risk: Dispatch spends prepaid balance and sends a person to a physical location.

Mitigation: Show the exact total price and wait for the user's explicit approval before dispatch; use a capped or limited key if available.

Risk: Optional source reporting links usage milestones to the Errand account.

Mitigation: Explain the reporting and enable ERRANDAI_CLIENT only with the user's explicit consent.

Risk: MCP setup may store an authorization header in the client's configuration.

Mitigation: Review how the MCP client stores credentials and protect its configuration before enabling the connection.

## Reference(s):

- [Errand AI on ClawHub](https://clawhub.ai/chloepark85/skills/errand-ai)
- [Errand setup and account](https://errand.be/clawhub)
- [Errand analytics and privacy](https://errand.be/privacy#clawhub-analytics)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown with price quotes, status updates, structured answers, and photo links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes GPS/photo verification verdicts; signed photo links expire after one hour.]

## Skill Version(s):

2.0.1 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
