## Description:

AccuWeather lets agents search locations and retrieve current conditions, daily forecasts, and hourly forecasts through an OOMOL-connected AccuWeather account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent resolve AccuWeather locations and retrieve current conditions or forecasts without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute arbitrary code on a user's machine.

Mitigation: Do not let an agent run curl|bash or PowerShell iex installers automatically; use a reviewed installation path, verify the installer when possible, and run setup manually with normal user privileges.

Risk: The skill depends on trust in OOMOL's CLI and account connection model.

Mitigation: Install only if the user trusts OOMOL and is comfortable using an OOMOL-connected account for AccuWeather access.

## Reference(s):

- [ClawHub AccuWeather skill page](https://clawhub.ai/oomol/skills/oo-accuweather)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [AccuWeather](https://www.accuweather.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before each action; command responses include data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server evidence, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
