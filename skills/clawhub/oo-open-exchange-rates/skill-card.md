## Description:

Open Exchange Rates (openexchangerates.org). Use this skill for ANY Open Exchange Rates request: searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve Open Exchange Rates currency lists, latest rates, historical rates, time-series rates, and currency conversions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that could execute arbitrary code if run automatically.

Mitigation: Have a human install the OOMOL oo CLI from a verified package or reviewed installer before allowing an agent to use the skill.

Risk: The skill depends on a signed-in OOMOL account and a connected Open Exchange Rates credential.

Mitigation: Run authentication or connection setup only after an action fails with an auth, missing-scope, expired-credential, or app-not-ready error.

## Reference(s):

- [Open Exchange Rates homepage](https://openexchangerates.org)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-open-exchange-rates)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the Open Exchange Rates connector through the OOMOL oo CLI; normal actions are read-only and return JSON data.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
