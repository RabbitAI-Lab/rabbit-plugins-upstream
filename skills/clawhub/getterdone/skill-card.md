## Description:

GetterDone lets agents hire paid human gig workers for physical-world tasks or specialized human work, with proof submission, explicit approval defaults, and server-side spending controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getterdone](https://clawhub.ai/user/getterdone)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs a paid human worker to perform physical errands, on-site verification, delivery, photography, or specialized remote work such as writing, design, translation, proofreading, or video editing.

### Deployment Geography for Use:

Global, subject to GetterDone worker availability and applicable local requirements.

## Known Risks and Mitigations:

Risk: The skill depends on an external GetterDone MCP package that runs locally with a GetterDone API key.

Mitigation: Verify the npm package publisher, pinned version, repository, and provenance before setup, and keep the API key scoped and revocable.

Risk: Paid task creation, approval, and disputes can move money or release escrow.

Mitigation: Keep the default in-conversation confirmation flow unless the owner intentionally opts into autonomous review, and rely on server-side per-task and daily spending caps.

Risk: Webhook testing through development tunnels can expose a local handler to the internet.

Mitigation: Use tunnels only for isolated development webhook handlers and use stable HTTPS endpoints with signature verification for production.

## Reference(s):

- [ClawHub GetterDone skill page](https://clawhub.ai/getterdone/skills/getterdone)
- [GetterDone platform](https://getterdone.ai)
- [GetterDone agent setup](https://getterdone.ai/register-agent)
- [GetterDone API documentation](https://getterdone.ai/docs/api)
- [GetterDone OpenAPI specification](https://getterdone.ai/api/openapi)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with inline bash, JSON, and tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GETTERDONE_API_KEY for authenticated workflows; paid actions default to explicit user confirmation.]

## Skill Version(s):

1.34.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
