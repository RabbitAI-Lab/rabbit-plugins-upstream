## Description:

Look up a public hostname on Agent Help Network when a web step is blocked or failing (403 or access denied, 429, 5xx or timeout, a login wall, a CAPTCHA or 'verify you are human' page), or when asked 'is this site down?' or 'does this site block agents?'. Returns the host's declared agent policy, official developer or customer path, provider status, and one recommended next action. Read-only; sends only the hostname.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agent-help-network](https://clawhub.ai/user/agent-help-network)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to investigate unexplained website access failures or answer whether a public site is down or blocks agents. It returns the host's declared agent policy, curated official paths, provider status, and a suggested next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A lookup sends the public hostname and limited diagnostic metadata to a third-party service.

Mitigation: Send only the bare public hostname and fixed diagnostic codes; omit URL paths, queries, page text, credentials, personal details, and private or local hostnames.

Risk: Optional observation or feedback submissions share additional diagnostic information.

Mitigation: Submit a report or feedback only after the user explicitly approves that specific submission.

Risk: Live service behavior could not be independently verified, and lookup results are advisory.

Mitigation: Treat results as guidance, follow platform rules and user instructions, and report service unavailability rather than claiming a lookup succeeded.

## Reference(s):

- [Agent Help Network](https://agenthelpnetwork.com)
- [Agent instructions](https://agenthelpnetwork.com/agent-instructions.txt)
- [API schema](https://agenthelpnetwork.com/openapi.json)
- [Agent Help Network MCP server](https://agenthelpnetwork.com/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Concise troubleshooting guidance with a recommended next action]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory; based on a read-only hostname lookup.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
