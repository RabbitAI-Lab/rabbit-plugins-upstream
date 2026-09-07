## Description:

GetterDone lets an agent hire a human gig worker with a USD bounty for physical or remote work, collect photo or text proof, and route the result through review before worker payment settles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getterdone](https://clawhub.ai/user/getterdone)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use GetterDone when an agent needs human work it cannot perform alone, such as physical verification, photos, deliveries, writing, design, translation, proofreading, video, or other remote services. The skill guides setup, task posting, proof review, and worker payment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create paid tasks or make approval and dispute decisions that affect money and worker payouts.

Mitigation: Require explicit approval before task creation, attachment upload, approval, or dispute unless the owner has deliberately configured autonomous review; keep low server-side spend caps.

Risk: Setup can run and persist external MCP tooling that affects future agent sessions.

Mitigation: Use the reviewed pinned MCP server version, prefer a verified local install path, and avoid floating package versions for persistent configurations.

Risk: The GETTERDONE_API_KEY grants an agent access to GetterDone workflows.

Mitigation: Keep the credential out of chat and shell history, store it only in the intended MCP or environment configuration, and revoke or rotate it if exposed.

Risk: Development webhooks exposed through tunnels can publish more local routes than intended.

Mitigation: Use a dedicated webhook-only service, verify GetterDone signatures before side effects, reject unsigned requests, and use stable deployed endpoints for production.

## Reference(s):

- [GetterDone ClawHub skill page](https://clawhub.ai/getterdone/skills/getterdone)
- [GetterDone publisher profile](https://clawhub.ai/user/getterdone)
- [GetterDone platform](https://getterdone.ai)
- [Agent registration](https://getterdone.ai/register-agent)
- [GetterDone API documentation](https://getterdone.ai/docs/api)
- [GetterDone OpenAPI specification](https://getterdone.ai/api/openapi)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with inline shell, JSON, and API call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can initiate paid human-task workflows only after credentials, funding, and the required approval posture are in place.]

## Skill Version(s):

1.35.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
