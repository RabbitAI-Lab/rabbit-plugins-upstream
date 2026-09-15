## Description:

openFDA (open.fda.gov) helps agents search, read, and count values in supported openFDA drug datasets through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query openFDA drug records and field-value counts through an OOMOL-connected account. Results are informational and should not be treated as medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: openFDA queries are routed through OOMOL as a third-party intermediary and require an OOMOL-connected account.

Mitigation: Install only when use of OOMOL as an intermediary is acceptable, and confirm the account connection and credential handling model before use.

Risk: The setup guidance includes remote shell and PowerShell installer commands that could execute unreviewed code.

Mitigation: Prefer a verifiable installer, pinned release, checksum, or manual review before running installer commands.

Risk: Drug dataset results are informational and could be mistaken for clinical or medical advice.

Mitigation: Use results for data lookup only and require qualified review before applying them to medical decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-openfda)
- [openFDA homepage](https://open.fda.gov/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
