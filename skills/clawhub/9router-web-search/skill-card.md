## Description:

Provides guidance and a shell wrapper for querying a configured 9Router web-search endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform current-information and news searches through a configured 9Router instance. It is most useful when the environment provides NINEROUTER_URL and, when authentication is enabled, NINEROUTER_KEY.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The displayed package description is stale and may hide that the skill performs external web searches.

Mitigation: Review the artifact before installing and present the skill as a 9Router web-search integration, not as a changelog update.

Risk: Search queries and an optional bearer token may be sent to the configured 9Router instance.

Mitigation: Use a trusted 9Router endpoint, provide credentials only through environment variables, and avoid sending secrets or sensitive personal data in queries.

## Reference(s):

- [9Router setup skill](https://raw.githubusercontent.com/decolua/9router/refs/heads/master/skills/9router/SKILL.md)
- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/9router-web-search)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with bash, JavaScript, JSON examples, and shell command output from the wrapper]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search output depends on the configured 9Router provider, query, max_results setting, and optional authentication.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
