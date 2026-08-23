## Description:

Travel search and booking integration that uses flyai-cli to call FlyAI travel data services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arsenalnxx](https://clawhub.ai/user/arsenalnxx)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-planning agents use this skill to search flights, trains, hotels, attractions, events, and packages through FlyAI and present concise travel options with images and booking links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel queries may be sent to FlyAI's CLI or service and returned booking links may open third-party pages.

Mitigation: Verify destination, price, refund terms, provider identity, and URL destination before clicking or purchasing.

Risk: Provider or platform details may be suppressed even though they can affect purchase decisions.

Mitigation: Review travel results before acting and preserve purchase-critical details such as provider identity, fare rules, refund terms, and total price.

## Reference(s):

- [FlyAI homepage](https://open.fly.ai/)
- [ClawHub skill page](https://clawhub.ai/arsenalnxx/skills/travel-planner)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown travel recommendations with images, tables, booking links, and concise notes; CLI calls return single-line JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires FLYAI_API_KEY for service calls and filters service system messages before presenting results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
