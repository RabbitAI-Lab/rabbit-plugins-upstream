## Description:

Nasdaq Data Link helps agents search and read Nasdaq Data Link data through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect live Nasdaq connector schemas and run read-oriented Nasdaq Data Link actions for market data, datatable metadata, exports, analyst ratings, dividends, and end-of-day quotes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute changing internet-hosted code.

Mitigation: Prefer an official package or release that can be verified, review installers before execution, and limit routine use to an already-installed oo CLI.

Risk: Nasdaq Data Link access depends on OOMOL-managed credentials and live connector behavior.

Mitigation: Inspect the live action schema before each run and confirm any action that changes state before execution.

## Reference(s):

- [Nasdaq Data Link](https://data.nasdaq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-nasdaq)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routine use returns oo CLI connector JSON responses when actions are executed.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
