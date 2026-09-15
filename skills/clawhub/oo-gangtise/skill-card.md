## Description:

Gangtise (gangtise.com). Use this skill for ANY Gangtise request — searching and reading data. Whenever a task involves Gangtise, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read Gangtise market, company, announcement, meeting summary, and broker research data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute code from OOMOL-hosted URLs.

Mitigation: Review the setup path before installing and independently verify the installer source, version, and integrity before running remote installer commands.

Risk: Using the skill requires account login and connecting a Gangtise API key through OOMOL.

Mitigation: Use the skill only when the user trusts OOMOL and Gangtise access through the oo CLI, and keep credential setup limited to explicit first-time or recovery flows.

## Reference(s):

- [Gangtise homepage](https://www.gangtise.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gangtise)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and an executionId under meta.]

## Skill Version(s):

1.0.2 (source: server evidence release.version and skill metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
