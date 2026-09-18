## Description:

Gong helps agents retrieve Gong calls, transcripts, users, and call outcomes through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business users with an OOMOL-connected Gong account use this skill to search and read Gong call records, transcripts, users, and call outcomes without handling raw API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include pipe-to-shell installer commands for the oo CLI.

Mitigation: Use an official package manager or a downloaded installer with a verified checksum or signature before running the CLI.

Risk: Read-oriented Gong actions can access sensitive business records, including calls, transcripts, users, and outcomes.

Mitigation: Run only the requested read actions, inspect the live action schema before execution, and share retrieved Gong data only with authorized recipients.

## Reference(s):

- [ClawHub Gong Skill](https://clawhub.ai/oomol/skills/oo-gong)
- [Gong Homepage](https://www.gong.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live action schemas before connector requests; read-oriented Gong actions can expose sensitive business records.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
