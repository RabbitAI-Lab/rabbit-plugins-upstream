## Description:

Google Chat (workspace.google.com). Use this skill for ANY Google Chat request -- searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Google Chat spaces, messages, and message history through an OOMOL-connected account using the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Install the oo CLI only through an official, verifiable installer or package-manager flow, and review the Google Chat connection scopes before use.

Risk: Google Chat access depends on an OOMOL-connected account and server-side credential handling.

Mitigation: Install only when the publisher is trusted and the user is comfortable connecting Google Chat through OOMOL's service.

## Reference(s):

- [Google Chat homepage](https://workspace.google.com/products/chat/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Google Chat connection](https://console.oomol.com/app-connections?provider=googlechat)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action requests; command responses are JSON when run with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
