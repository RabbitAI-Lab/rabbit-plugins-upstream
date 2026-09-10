## Description:

Helps users document recurring noise issues by logging incidents, analyzing patterns, flagging quiet-hours events, scoring impact, exporting CSVs, and drafting factual complaint letters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users such as tenants, condo owners, landlords, and people responding to a noise complaint use this skill to build a contemporaneous record of recurring noise and prepare calm, fact-based escalation materials for landlords, HOAs, mediation, or city noise offices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Noise logs and complaint letters can include addresses, phone numbers, neighbor identifiers, and sensitive dispute notes stored in local plain files.

Mitigation: Store logs in a private directory, use the --file option for controlled locations, and review CSV exports and letters before sharing.

Risk: Quiet-hour, municipal-limit, and decibel language may be inaccurate for a user's jurisdiction or measurement setup.

Mitigation: Verify local ordinances and use calibrated measurements where exact decibel claims matter; treat default limits and uncalibrated phone readings as general context.

## Reference(s):

- [Noise Ordinances, Evidence, and Escalation Reference](references/ordinances-and-evidence.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown and plain text with bash command examples; generated artifacts include local JSON logs, CSV exports, and complaint-letter text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local JSON storage by default and supports configurable file path and quiet-hour settings.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
