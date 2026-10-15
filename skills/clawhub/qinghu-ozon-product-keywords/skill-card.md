## Description:

Queries Ozon product IDs for organic traffic keywords, topic tags, and advertising keywords using Qinghu data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ozon sellers and analysts use this skill to examine which organic, topic-tag, and advertising keywords drive traffic to a product or competitor listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade tooling and modify the user's environment beyond the keyword query.

Mitigation: Review before installing; prefer an environment-managed, version-pinned qhkit rather than automatic Node installation or unpinned npm/npx commands.

Risk: Queries require an API token and may consume paid credits.

Mitigation: Use trusted token setup, check estimated charges, and obtain user approval before paid calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-ozon-product-keywords)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written findings with optional tabular export for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports relevant platform, period, sample size, and credits consumed when available.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
