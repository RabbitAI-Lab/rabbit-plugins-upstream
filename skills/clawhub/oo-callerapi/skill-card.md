## Description:

CallerAPI (callerapi.com). Use this skill for ANY CallerAPI request - searching and reading data. Whenever a task involves CallerAPI, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query CallerAPI through an OOMOL-connected account for phone-number reputation, business details, complaints, HLR carrier data, account email, and credit balance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote shell installer commands for the OOMOL CLI.

Mitigation: Review the installation path and trust the OOMOL CLI distribution channel before running curl|bash or irm|iex installer commands with local user privileges.

## Reference(s):

- [CallerAPI homepage](https://callerapi.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-callerapi)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only CallerAPI query guidance and oo CLI command usage; action responses are JSON from the connector.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
