## Description:

Turns US rental move-out inspection findings into priced make-ready tasks, vendor scopes, and owner approval estimates using Tektolo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tektolo](https://clawhub.ai/user/tektolo)

### License/Terms of Use:

MIT-0

## Use Case:

Property managers and rental owners use the skill to turn move-out findings into estimated turnover costs, trade-specific work scopes, and owner approval requests.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Property details and inspection findings are sent to Tektolo for estimates.

Mitigation: Send only the ZIP-level details and relevant findings; exclude tenant names, street addresses, credentials, and unrelated private photos unless sharing is authorized.

Risk: Estimated ranges or hazardous-condition flags could be mistaken for firm quotes or professional diagnoses.

Mitigation: Label ranges as estimates, surface assumptions and quote-required items, and refer suspected hazards to licensed professionals.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/tektolo/skills/property-turnover)
- [Tektolo property turnover capability](https://tektolo.com/capabilities/property-turnover)
- [Tektolo catalog and schemas](https://tektolo.com/catalog.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown estimate summary and trade-specific scopes with download links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cost ranges, assumptions, unknowns, and professional referrals; estimates are not quotes.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
