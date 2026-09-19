## Description:

Codacy (codacy.com). Use this skill for ANY Codacy request: searching and reading data through an OOMOL-connected Codacy account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to inspect Codacy connector schemas and retrieve Codacy users, organizations, repositories, analyses, tools, patterns, and supported languages through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup instructions may execute unverified code.

Mitigation: Install the oo CLI only through a trusted, reviewed process, preferably using a pinned version or verified installer; do not allow an agent to run installer commands automatically.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-codacy)
- [Codacy homepage](https://www.codacy.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Codacy action responses are JSON objects with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
