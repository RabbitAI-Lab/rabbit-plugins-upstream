## Description:

Baserow (baserow.io). Use this skill for Baserow requests that read, create, update, or delete data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Baserow tables, fields, and rows through an authenticated OOMOL connector. It supports reads, writes, and destructive deletes, with user confirmation expected before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes all Baserow requests through OOMOL as an intermediary for Baserow data.

Mitigation: Install only after reviewing the OOMOL connector posture and use least-privilege Baserow credentials.

Risk: The setup guidance includes remote installer commands for the oo CLI.

Mitigation: Review safer installation options before running installer commands.

Risk: The skill can create, update, and delete Baserow records.

Mitigation: Require explicit user confirmation for exact write and delete targets and payloads before execution.

Risk: Secrets or sensitive values could be sent in row data, filters, or connector payloads.

Mitigation: Avoid placing secrets in Baserow row data or query filters and inspect payloads before submission.

## Reference(s):

- [ClawHub Baserow Skill](https://clawhub.ai/oomol/skills/oo-baserow)
- [Baserow Homepage](https://baserow.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; requires explicit confirmation before writes or deletes.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
