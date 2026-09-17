## Description:

Checks material-cost variance allocation tables for row-level arithmetic, totals, duplicate rows, blanks, and source-cited findings in the free tier.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting staff use this skill during month-end close or reconciliation to review material-cost variance allocation tables. It recalculates stated table relationships, reports duplicates or missing fields, and avoids unsupported conclusions when input is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reviewed free checker is local, but the skill text advertises a separate paid install-and-purchase workflow that runs unpinned third-party code.

Mitigation: Use the free checker only for local table checks; independently verify source, version, payment terms, permissions, and code provenance before running paid install commands or purchasing upgrades.

Risk: A clean result covers only the free-tier checks and does not include the withheld paid checks or accounting-policy judgments.

Mitigation: Treat output as limited to the listed executed checks and review withheld or out-of-scope accounting checks separately before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/material-cost-variance-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON command output with cited findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed free checks, missing-input status, and withheld checks; uses local input files or sample data.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
