## Description:

Searches and analyzes Swedish real estate on hemnet.se, including active listings, sold prices, listing details, photos, market statistics, address lookup, and Swedish mortgage calculations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research Swedish properties on Hemnet, compare active and sold listings, inspect market statistics, resolve addresses, and estimate Swedish monthly housing costs.

### Deployment Geography for Use:

Sweden

## Known Risks and Mitigations:

Risk: Hemnet market statistics can be based on thin samples and may mislead valuation decisions.

Mitigation: Check sample_size before relying on medians, averages, or price-per-square-meter conclusions.

Risk: Use of public Hemnet data may be subject to hemnet.se terms of service.

Mitigation: Use the skill within Hemnet's terms and avoid workflows that exceed permitted public lookup behavior.

Risk: The skill may be invoked for broad Swedish real-estate questions, not only explicit Hemnet requests.

Mitigation: Confirm that public Hemnet lookup is appropriate before treating results as the basis for advice or decisions.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text with structured property details, comparison summaries, URLs, and calculation results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Hemnet listing details, sold-price comparisons, photo URLs, market statistics, address matches, and mortgage-cost calculations.]

## Skill Version(s):

0.6.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
