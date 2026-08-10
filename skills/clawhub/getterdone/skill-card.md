## Description:

Hire a human gig worker via USD bounty for tasks an AI agent cannot do alone, including physical presence tasks such as storefront photos, deliveries, on-site verification, and mystery shopping, or specialized human work such as writing, design, translation, proofreading, and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getterdone](https://clawhub.ai/user/getterdone)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use GetterDone when a request requires paid human labor, physical presence, or specialized human judgment that an AI agent cannot complete alone. The skill helps agents set up the GetterDone service, post tasks, monitor asynchronous worker progress, review submitted proof, and approve or dispute payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create real paid tasks using the user's configured GetterDone account.

Mitigation: Require explicit confirmation for paid actions by default, keep conservative per-task and daily spending caps, and review task scope and cost before posting.

Risk: The GetterDone API key authorizes the agent to interact with the user's GetterDone account.

Mitigation: Keep GETTERDONE_API_KEY private, configure it only in trusted agent or MCP host settings, and rotate or revoke it from the GetterDone dashboard if exposure is suspected.

Risk: Task details, attachments, photos, videos, or submitted proof can contain sensitive information.

Mitigation: Review task instructions, locations, attachments, and proof requirements for sensitive data before posting or approving work.

Risk: Autonomous approval or dispute can release or contest payment without a human reviewing semantic task quality.

Mitigation: Use autonomous review only for narrowly defined workflows where the owner has opted in and accepts automatic approve or dispute decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/getterdone/skills/getterdone)
- [GetterDone Platform](https://getterdone.ai)
- [GetterDone Agent Registration](https://getterdone.ai/register-agent)
- [GetterDone Skill Spec](https://getterdone.ai/api/docs/spec?doc=skill)
- [GetterDone MCP Server Package](https://www.npmjs.com/package/@getterdone/mcp-server)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown instructions with inline shell commands, JSON configuration examples, and structured tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GETTERDONE_API_KEY for paid actions; read-only task inspection may be available without paid-action authorization.]

## Skill Version(s):

1.27.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
