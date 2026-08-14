## Description:

Temu EU Ads API skill that helps agents call Partner EU advertising endpoints through the LinkFox gateway for ad creation, modification, detail queries, reporting, operation logs, ROAS prediction, and ad-eligible goods lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and Temu EU merchants use this skill to operate and inspect Temu advertising workflows from an agent, including creating ads, adjusting budgets or ROAS, retrieving reports, and checking logs. It is intended for users who already have appropriate LinkFox and Temu merchant credentials.

### Deployment Geography for Use:

Europe (Temu EU Partner APIs)

## Known Risks and Mitigations:

Risk: The skill sends LinkFox and Temu merchant credentials through the LinkFox gateway.

Mitigation: Install and use it only when the user trusts the LinkFox gateway and has confirmed the credentials are appropriate for this workflow.

Risk: Scripts can modify Temu ads, budgets, and ROAS settings.

Mitigation: Review request payloads before execution and prefer scoped merchant credentials with only the permissions needed for the intended advertising task.

Risk: The skill stores Temu access tokens and full API responses locally.

Mitigation: Keep token storage and generated response directories access-controlled, and remove stored tokens or response files when they are no longer needed.

Risk: Generic proxy scripts and gateway override environment variables can broaden where requests are sent.

Mitigation: Avoid generic proxy use for non-Ads APIs and do not set gateway override environment variables unless the destination host is trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-ads-eu)
- [API reference](references/api.md)
- [Temu access token guide](references/access-token.md)
- [Partner EU Ads catalog](references/partner-eu-catalog.md)
- [Onboarding and billing guidance](references/onboarding.md)
- [Ads API documentation index](references/apis/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance, shell command examples, and JSON API responses or saved response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save full API responses under a local linkfox session data directory and may print summaries for larger responses.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
