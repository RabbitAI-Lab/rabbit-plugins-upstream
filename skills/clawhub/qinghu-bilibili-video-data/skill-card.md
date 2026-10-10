## Description:

Retrieves Bilibili video details and engagement metrics from a video link using the Qinghu data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and analysts use this skill to check a Bilibili video's views, likes, coins, favorites, shares, comments, and other available details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid requests to an external service may incur variable credit charges.

Mitigation: Review the estimate and obtain user approval before paid calls; report actual credits used.

Risk: Using the service requires a local API token.

Mitigation: Use a trusted, contained environment and protect the token from disclosure.

Risk: Setup may install qhkit or Node and persist shell PATH changes.

Mitigation: Prefer an environment with qhkit already installed; review installations and permit shell profile changes only explicitly.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-bilibili-video-data)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise text or Markdown summary, with a tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports paid-call credit consumption when applicable.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
