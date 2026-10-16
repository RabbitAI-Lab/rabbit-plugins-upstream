## Description:

Access RoxyAPI readings, charts, calendars, forecasts, and usage information through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to request RoxyAPI tarot readings, astrology and personal charts, Chinese calendar information, and forecasts through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested CLI installers execute remotely fetched shell code.

Mitigation: Review and verify the OOMOL installer source before running an installation command.

Risk: Personal birth details, location, time zone, or relationship data may be sent through the connected RoxyAPI/OOMOL flow.

Mitigation: Share only necessary personal details and confirm the connected service's data-handling terms before submitting sensitive inputs.

## Reference(s):

- [RoxyAPI homepage](https://roxyapi.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [ClawHub RoxyAPI skill listing](https://clawhub.ai/oomol/skills/oo-roxyapi)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON connector results, presented to users as text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results vary by action and the live connector schema.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
