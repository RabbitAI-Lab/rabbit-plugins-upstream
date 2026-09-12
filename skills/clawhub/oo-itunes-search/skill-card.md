## Description:

Use this skill for iTunes Search API requests, including searching and reading iTunes Store and Apple Books Store data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to search and look up iTunes Store and Apple Books Store records through the OOMOL itunes_search connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Have a human inspect and install the oo CLI from a trusted, verified channel instead of allowing an agent to run installer commands automatically.

Risk: Search and lookup payloads pass through OOMOL as an intermediary service.

Mitigation: Avoid sending secrets or sensitive personal text in iTunes search payloads, and install only when this intermediary use is acceptable.

## Reference(s):

- [iTunes Search API homepage](https://performance-partners.apple.com/search-api)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-itunes-search)

## Skill Output:

**Output Type(s):** [guidance, shell commands, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect the live action schema before constructing a connector payload.]

## Skill Version(s):

1.0.0 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
