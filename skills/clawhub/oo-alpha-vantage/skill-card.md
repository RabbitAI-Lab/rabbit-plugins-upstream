## Description:

Use this skill to search and retrieve Alpha Vantage market and company data through OOMOL-authenticated oo CLI connector actions instead of calling the Alpha Vantage API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Alpha Vantage market, company fundamentals, forex, crypto, commodity, macroeconomic, options, news sentiment, market status, and symbol-search data through OOMOL-authenticated oo CLI connector actions without handling raw Alpha Vantage API keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path tells agents or users to run unverified remote installer scripts for the oo CLI.

Mitigation: Review the skill before installing if oo is not already installed; install the oo CLI through a verified, pinned, or inspectable method and do not let an agent run remote installer commands automatically.

Risk: Alpha Vantage access depends on an authenticated OOMOL account and a connected Alpha Vantage credential.

Mitigation: Run authentication and connection setup only after an actual auth or connection failure, and keep credential connection steps user-controlled.

## Reference(s):

- [Alpha Vantage homepage](https://www.alphavantage.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL Alpha Vantage skill page](https://clawhub.ai/oomol/skills/oo-alpha-vantage)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
