## Description:

Gangtise enables agents to search and read Gangtise market data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Gangtise securities, reports, announcements, market data, and company fundamentals through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may invoke the OOMOL oo CLI for Gangtise requests, and first-time setup can run an external installer if the CLI is missing.

Mitigation: Install only when Gangtise access through OOMOL is intended, inspect connector schemas before running actions, and use first-time setup commands only after an auth, connection, or missing-CLI failure.

## Reference(s):

- [Gangtise homepage](https://www.gangtise.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
