## Description:

Loop Returns enables an agent to search and read Loop Returns return and destination data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operations teams use this skill to retrieve Loop Returns return details and destination records from a Loop Returns account connected through OOMOL. The skill guides agents to inspect the live connector schema before constructing payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions use mutable remote installer scripts directly from a shell.

Mitigation: Prefer a signed or package-manager installation path for the oo CLI, verify the source, and avoid running the installer from an elevated shell.

Risk: The skill accesses Loop Returns through OOMOL as an intermediary.

Mitigation: Install only if that access model is acceptable, and review the connector schema and payload before any action involving business return data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-loop-returns)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Loop Returns homepage](https://www.loopreturns.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; connector action responses are JSON when commands are run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an OOMOL account, and a connected Loop Returns credential; action payloads should be based on the live connector schema.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
