## Description:

Deep analysis of unusual options activity and walls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ssidharhubble](https://clawhub.ai/user/ssidharhubble)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to request unusual options activity and options-wall analysis for a specified ticker through a remote financial-signal service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends requested tickers to an external service.

Mitigation: Review the remote dependency before installing and avoid sending sensitive or non-public ticker requests.

Risk: Remote financial signals may be presented as analysis without independent verification.

Mitigation: Treat outputs as informational only and verify them independently before making trading or financial decisions.

Risk: Premium responses include a direct cryptocurrency payment prompt.

Mitigation: Do not send cryptocurrency unless the provider, wallet destination, and payment flow have been independently verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ssidharhubble/skills/options-brain)
- [Provider pricing page](https://ssyopros.zo.space/pricing)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [JSON object returned from a remote financial-signal service, or a payment-required error object.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ticker input; premium signals may require payment proof.]

## Skill Version(s):

1.1.2 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
