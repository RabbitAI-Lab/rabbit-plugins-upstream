## Description:

Metabase (metabase.com). Use this skill for ANY Metabase request — reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to let an agent inspect, query, search, create, and update Metabase content through an OOMOL-connected account. It is suited for managing databases, collections, dashboards, cards, questions, metrics, MBQL queries, and native SQL where the connected Metabase instance permits those actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in setup instructions could execute unverified code.

Mitigation: Review official OOMOL installation documentation first, prefer a pinned or package-manager installation when available, and run the remote installer only when the oo CLI is actually missing.

Risk: Write-capable Metabase actions can create or update collections, dashboards, questions, metrics, and related content.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write-capable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-metabase)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Metabase homepage](https://www.metabase.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before constructing JSON payloads and to handle connector responses containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
