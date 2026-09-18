## Description:

HasData lets agents search Google SERP data and scrape public web pages through an OOMOL-connected HasData account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve public web page and Google search result data through HasData without handling raw API credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes unverified remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI manually from a verified, versioned source, inspect installer contents before execution, and do not let an agent run the remote installer commands automatically.

## Reference(s):

- [HasData homepage](https://hasdata.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect each action's live schema before sending JSON payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
