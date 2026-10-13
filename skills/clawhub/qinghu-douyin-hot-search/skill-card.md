## Description:

Retrieves current Douyin hot-search rankings through Qinghu's data tool for trend research and content planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and analysts use this skill to check Douyin hot-search topics and identify timely content opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may install Node/npm tooling or alter shell PATH beyond the data lookup.

Mitigation: Review installation steps before running; prefer an environment where qhkit is already installed.

Risk: Configuring an API token can store credentials locally.

Mitigation: Supply credentials through a scoped, revocable secret mechanism instead of persistent host configuration.

Risk: Hot-search queries can incur Qinghu credit charges that increase with result volume.

Mitigation: Estimate charges and obtain user consent before paid calls or large pulls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-douyin-hot-search)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise ranking summary with optional tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports usage credits for paid calls; larger results may be delivered as a file.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
