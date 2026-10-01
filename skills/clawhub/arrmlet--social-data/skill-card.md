## Description:

Fetches real-time social media data from X and Reddit by keyword, username, date range, and filters with engagement metrics via the Macrocosmos SN13 API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arrmlet](https://clawhub.ai/user/arrmlet)

### License/Terms of Use:

MIT

## Use Case:

Developers and analysts use this skill to guide agents in querying Macrocosmos SN13 for X and Reddit posts by keyword, username, date range, and filters, then interpreting returned engagement metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, usernames, date filters, and the MC_API credential are sent to Macrocosmos during API use.

Mitigation: Use only approved queries and credentials, and avoid confidential, regulated, or sensitive investigative searches unless organizational data-sharing approval exists.

Risk: Some username-only or niche keyword queries may timeout or return sparse results.

Mitigation: Set explicit wider date ranges, prefer keyword searches when possible, and handle timeouts by retrying with broader filters.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/arrmlet/skills/social-data)
- [Macrocosmos MCP Project](https://github.com/macrocosm-os/macrocosmos-mcp)
- [macrocosmos-mcp on PyPI](https://pypi.org/project/macrocosmos-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON, bash, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an MC_API credential and outbound requests to the Macrocosmos API.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
