## Description:

Connects agents to Wikipedia and Wikimedia for multilingual article search, summaries, historical facts, citations, media, and article research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use this skill to look up Wikipedia articles, explore related topics and media, check citations and edit history, and discover missing articles across supported languages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup terms, article titles, usernames or IPs, coordinates, and dates are sent to Wikipedia/Wikimedia services.

Mitigation: Avoid entering sensitive information in queries; install only if this data sharing is acceptable.

Risk: The requests dependency is not pinned to an exact version, reducing reproducibility.

Mitigation: Pin and audit the requests dependency before deployment when reproducible installs are required.

## Reference(s):

- [Wikipedia MCP on ClawHub](https://clawhub.ai/evanfoglia/skills/wikipedia)

## Skill Output:

**Output Type(s):** [Text, Research guidance]

**Output Format:** [Plain text with article links and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results vary by tool and selected Wikipedia language.]

## Skill Version(s):

1.6.27 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
