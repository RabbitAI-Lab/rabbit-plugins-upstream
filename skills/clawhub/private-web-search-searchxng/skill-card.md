## Description:

Self-hosted private web search using SearXNG for privacy-sensitive search, blocked or paid external search APIs, or search without tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adelpro](https://clawhub.ai/user/adelpro)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to run a local SearXNG instance and retrieve private web search results through curl, jq, and a helper script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill starts and manages a persistent local SearXNG Docker container on port 8080.

Mitigation: Confirm the local container and port binding are acceptable before installation, and use the documented stop or remove commands when the service is no longer needed.

Risk: Search queries still pass from the local SearXNG instance to selected upstream search engines.

Mitigation: Avoid submitting sensitive queries to upstream engines and choose search engines according to the privacy needs of the task.

Risk: Some search engines may be blocked, rate-limited, or return unreliable result counts.

Mitigation: Test with a small result limit before heavy use and prefer engines documented as working for the current environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adelpro/skills/private-web-search-searchxng)
- [Publisher profile](https://clawhub.ai/user/adelpro)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON search-result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Helper script accepts a search query and optional result limit; requires Docker, curl, and jq with a local SearXNG service.]

## Skill Version(s):

1.3.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
