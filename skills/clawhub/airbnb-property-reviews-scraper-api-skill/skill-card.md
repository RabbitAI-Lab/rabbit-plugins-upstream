## Description:

This skill helps users run the Airbnb Property Reviews Scraper BrowserAct template and extract structured public data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run a BrowserAct Airbnb review extraction template for market research, competitive monitoring, dataset enrichment, and review analysis. It accepts an Airbnb room URL and review count, then returns structured public review fields for downstream reporting or automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill text may encourage users to share a BrowserAct API key conversationally.

Mitigation: Configure BROWSERACT_API_KEY through a secure environment variable or secret manager, never paste the key into chat, and rotate the key if it was already shared.

Risk: Broad invocation wording could lead the skill to be used outside explicit Airbnb review extraction tasks.

Mitigation: Use the skill only when the user clearly asks for Airbnb property review extraction and confirm the target room URL and review count before running it.

Risk: The release was flagged suspicious by the authoritative security evidence.

Mitigation: Review the skill before installing or running it, with particular attention to credential handling and the external BrowserAct API calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/airbnb-property-reviews-scraper-api-skill)
- [BrowserAct API key console](https://www.browseract.com/reception/integrations?co-from=airbnb-property-reviews-scraper)
- [BrowserAct API base endpoint](https://api.browseract.com/v3/bots)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Terminal status logs and JSON response text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned records may include property name, property URL, reviewer name, review publish date, review text, star rating, reviewer location or stay type, and rank when available.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
