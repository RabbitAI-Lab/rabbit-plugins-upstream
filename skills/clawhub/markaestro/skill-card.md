## Description:

Schedule, publish, and review social posts through Markaestro across Facebook, Instagram, TikTok, Threads, Pinterest, LinkedIn, and X, while reading analytics and managing Intelligent Evergreen queues through its MCP server or public API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[markaestro](https://clawhub.ai/user/markaestro)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing teams use this skill to manage Markaestro-connected social accounts, create or schedule posts, review publishing status, analyze performance, and manage recurring Evergreen content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can schedule or publish public social content through connected Markaestro accounts.

Mitigation: Connect only the brands the agent should manage, confirm immediate publishing actions with the user, and report post IDs, statuses, channels, and UTC schedule times after mutations.

Risk: An all-brands connection can act across every brand in the workspace.

Mitigation: Use single-brand consent where possible, list available products before acting, and ask the user to confirm the brand when a request is ambiguous.

Risk: Headless or local setup can involve bearer tokens or running the MCP package directly.

Mitigation: Prefer browser OAuth when available; for headless or local setup, pin or verify the MCP package and avoid exposing API keys in chat or logs.

Risk: Analytics may be scoped, clamped by plan history, rate limited, or missing platform metrics.

Mitigation: Report coverage, sample size, plan window caps, null metrics, and refresh limits instead of treating incomplete analytics as complete results.

## Reference(s):

- [Markaestro skill page](https://clawhub.ai/markaestro/skills/markaestro)
- [Markaestro MCP tools](references/tools.md)
- [Delivery modes, statuses, and platform settings](references/settings.md)
- [Markaestro agent setup](https://markaestro.com/developers/agents?client=headless)
- [Markaestro MCP endpoint](https://markaestro.com/api/public/v1/mcp)
- [Markaestro public REST API](https://markaestro.com/api/public/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples; MCP tools and REST API calls return JSON text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool outputs include opaque IDs, post statuses, analytics metrics, scheduled UTC times, and publish job results.]

## Skill Version(s):

0.3.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
