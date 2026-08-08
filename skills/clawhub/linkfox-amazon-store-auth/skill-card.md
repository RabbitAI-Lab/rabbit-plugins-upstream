## Description:

This skill helps agents authorize and manage Amazon seller stores through LinkFox, including authorization links, authorized-store lists, authorization status checks, and token refresh.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and agents use this skill to connect Amazon seller accounts to LinkFox, choose an authorized store, check authorization status, and refresh authorization tokens before downstream seller-data workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive LinkFox API keys, Amazon seller authorization metadata, and possible legacy access or refresh token fields.

Mitigation: Treat all API keys and token-like values as secrets; do not display or log raw tokens, and prefer status and metadata fields when reporting authorization state.

Risk: Gateway host environment variables can redirect requests away from LinkFox-controlled endpoints.

Mitigation: Use the default LinkFox gateway unless the operator has explicitly reviewed and approved any gateway override.

Risk: The artifact includes onboarding, billing/payment, and feedback-reporting behavior in addition to Amazon store authorization.

Mitigation: Run phone-login, payment, or feedback flows only when they are directly needed for the user's current task and the user has approved that action.

Risk: Local response files may contain account metadata from authorized stores or token-status calls.

Mitigation: Review and periodically delete the local linkfox output directory when it may contain sensitive account metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-auth)
- [Amazon store authorization API reference](artifact/references/api.md)
- [Amazon store authorization flow](artifact/references/authorization-flow.md)
- [Quick start](artifact/references/quick-start.md)
- [Onboarding for authentication and billing](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full responses under a local linkfox output directory and may print summaries for larger responses.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact _meta.json and README list 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
