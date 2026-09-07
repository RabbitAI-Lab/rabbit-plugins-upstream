## Description:

Read-only Lose It nutrition extractor that logs in or reads an export ZIP, fetches the user's Lose It data export, and emits per-day nutrition as JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stozo04](https://clawhub.ai/user/stozo04)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to retrieve a user's own Lose It nutrition history for downstream analysis or storage. It is intended for read-only extraction of daily calories, macros, meal breakdowns, Lose It budget values, and exercise-adjustment figures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Lose It account credentials, session tokens, and exported nutrition data.

Mitigation: Install only if comfortable granting that access; prefer --zip or environment variables over plaintext config.json, use a trusted explicit config path, and keep token directories private and out of backups.

Risk: Server security guidance flags redirect handling and token-file symlink protections for review before unattended use.

Mitigation: Avoid unattended use until those protections are fixed, and review installation behavior before deployment.

Risk: The Lose It export flow may break if Lose It changes authentication or export behavior.

Mitigation: Use the downloaded ZIP fallback when live login/export fails, and monitor repeated export or parse failures.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/stozo04/skills/loseit)
- [Project Homepage](https://github.com/stozo04/loseit-cli)
- [Machine Contract](docs/MACHINE_CONTRACT.md)
- [README](README.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Configuration]

**Output Format:** [JSON object keyed by ISO date for days --json; human-readable text table for default days output; command and configuration guidance in Markdown documentation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [stdout is reserved for parseable data; stderr carries hints, logs, and errors. Secrets are not printed.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
