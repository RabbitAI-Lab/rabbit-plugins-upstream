## Description:

途牛+同程+美团+RollingGo五平台直飞航班实时比价，按航班号自动匹配同一航班跨平台报价，一次出结果含预订链接。暑期机票比价、出行省钱。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers and travel-planning agents use this skill to compare direct mainland China flight prices across supported OTA sources and return a concise comparison with booking links. It is intended for price discovery, not ticket booking or itinerary servicing.

### Deployment Geography for Use:

China domestic flight search use cases

## Known Risks and Mitigations:

Risk: Trip query details are sent through the publisher's Tencent Cloud proxy to flight providers.

Mitigation: Install only when that data flow is acceptable for the user or organization, and disclose it before use.

Risk: The release ships a plaintext proxy token.

Mitigation: Rotate the exposed token, remove secrets from source, and use runtime environment variables or a secret store before treating the skill as low risk.

Risk: Flight prices, taxes, availability, and platform coverage can differ across providers or change after the comparison is generated.

Mitigation: Ask users to verify final fare details on the booking platform before purchase and preserve the skill's caveats in returned results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/china-flight-price-compare)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-formatted text with flight listings, price comparisons, caveats, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are scoped to direct flights from supported Chinese city mappings and may include platform availability warnings.]

## Skill Version(s):

4.2.5 (source: server release evidence; artifact _meta.json says 4.2.4 and artifact/version says 1.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
