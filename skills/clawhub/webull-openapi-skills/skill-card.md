## Description:

Trade stocks, options, futures, crypto, and event contracts on Webull, query real-time and historical market data, and manage accounts and positions across supported Webull regions with configurable risk controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[webull-openapi](https://clawhub.ai/user/webull-openapi)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and external users use this skill to let an AI assistant operate Webull OpenAPI workflows through a CLI, including market data lookup, account review, authentication, and order management. It is intended for users who already have Webull developer credentials and understand brokerage-account trading risk.

### Deployment Geography for Use:

Global, limited to supported Webull regions: US, HK, JP, SG, TH, MY, UK, MX, BR, EU, ZA, and AU.

## Known Risks and Mitigations:

Risk: The skill can affect real brokerage accounts and saved watchlists, and server security evidence notes that confirmation is not enforced by code.

Mitigation: Keep WEBULL_ENVIRONMENT=uat until ready for live trading and require separate human confirmation before every order or watchlist deletion/removal.

Risk: The skill uses Webull API credentials, cached tokens, and optional audit logs.

Mitigation: Protect the .env file, token directory, and audit log location; store credentials outside the project directory when possible.

Risk: Regional endpoint behavior and asset support vary by Webull region.

Mitigation: Verify region configuration and endpoint behavior before using ZA or production accounts, and confirm that the intended asset class is supported in the selected region.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/webull-openapi/skills/webull-openapi-skills)
- [Trading Guide](references/skill_trading.md)
- [Market Data Guide](references/skill_market_data.md)
- [Webull OpenAPI Reference](references/api_reference.md)
- [Webull OpenAPI developer documentation](https://developer.webull.com/apis/docs/webull-open-api-reference)
- [webull-openapi-python-sdk](https://github.com/webull-inc/webull-openapi-python-sdk)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and formatted stdout text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include region-aware disclaimers; errors are emitted to stderr with non-zero exit codes.]

## Skill Version(s):

1.1.9 (source: ClawHub release evidence; artifact pyproject.toml lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
