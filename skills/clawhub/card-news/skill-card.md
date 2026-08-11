## Description:

Returns material news about one major US credit card from the last three months, including direct card changes, relevant issuer updates, and major approved-site coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiahongc](https://clawhub.ai/user/jiahongc)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to get a concise, current news brief for one exact major US credit card variant, focused on changes that materially affect how the card should be understood.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Current web lookups can surface outdated or low-quality card news if source freshness or materiality checks are missed.

Mitigation: Use issuer-first source selection, the three-month inclusion window, and date confirmation against issuer newsroom or approved secondary coverage.

Risk: The artifact relies on shared card-policy files for source selection and formatting that are not included in this release evidence.

Mitigation: Review the shared card-policy dependencies before deployment when full transparency into source rules is required.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown sections with hidden YAML sources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focused on a single exact card variant and a three-month news window.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
