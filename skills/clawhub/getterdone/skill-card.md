## Description:

GetterDone lets an agent hire paid human workers for physical errands, on-site verification, deliveries, and remote human work, with submitted proof, user-confirmed paid actions, and server-side spending caps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getterdone](https://clawhub.ai/user/getterdone)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use GetterDone when an AI agent needs to delegate real-world tasks or remote human services to a paid worker. Typical tasks include storefront checks, photos, deliveries, calls, writing, design, translation, proofreading, research, and video work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid task posting can charge a card after user confirmation.

Mitigation: Keep human confirmation enabled for paid actions, rely on server-side per-task and daily spending caps, and avoid recurring funding unless repeated task posting is intended.

Risk: The integration stores a scoped GetterDone API key locally or in the agent environment.

Mitigation: Protect GETTERDONE_API_KEY as a credential, rotate or revoke it from the GetterDone dashboard if exposed, and avoid passing secrets on command lines.

Risk: The skill depends on a pinned external MCP server package.

Mitigation: Verify the npm package integrity and provenance for @getterdone/mcp-server@0.2.26 before installation or update.

Risk: Autonomous approval or dispute decisions can release or contest real payments without human judgment.

Mitigation: Use autonomous review only after deliberate owner opt-in with clear review criteria; otherwise present worker proof to the user before approving or disputing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/getterdone/skills/getterdone)
- [Publisher profile](https://clawhub.ai/user/getterdone)
- [GetterDone platform](https://getterdone.ai)
- [Agent registration](https://getterdone.ai/register-agent)
- [GetterDone API documentation](https://getterdone.ai/docs/api)
- [GetterDone OpenAPI specification](https://getterdone.ai/api/openapi)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown instructions with inline commands and API/tool call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GETTERDONE_API_KEY for paid-service integration; paid task creation and review actions default to explicit user confirmation.]

## Skill Version(s):

1.36.1 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
