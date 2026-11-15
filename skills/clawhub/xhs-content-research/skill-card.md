## Description:

A research assistant for exploring Xiaohongshu topics, keywords, trends, competitor content, and useful examples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, brand researchers, and creators can use this skill to investigate Xiaohongshu search results, compare competing content, identify topic and trend patterns, and organize relevant examples for follow-up analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs users to run a mutable third-party CLI that may access credentials and files available in its execution environment if compromised.

Mitigation: Run it only where you are comfortable granting that access, and limit the credentials and files available to the CLI.

Risk: The security scan is partial because several local references could not be resolved.

Mitigation: Review the complete installed skill and referenced files before relying on it.

Risk: Research keywords are sent to SocialDataX when using the service.

Mitigation: Consider whether the query terms are appropriate to share with the service before searching.

## Reference(s):

- [SocialDataX skill and API key information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown research summaries with relevant titles, authors or accounts, source links or content IDs, and follow-up angles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are limited by the selected query and requested pages or item count.]

## Skill Version(s):

0.1.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
