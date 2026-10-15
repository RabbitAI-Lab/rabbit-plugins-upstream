## Description:

Queries Google Trends keyword interest in a selected market to help distinguish rising, stable, declining, and seasonal demand.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and market researchers use this skill to assess search-interest trends for a keyword in a selected market before evaluating product demand.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation or updates may change local Node/npm tooling.

Mitigation: Have an administrator provision and pin Node and qhkit; require approval before any installation or update.

Risk: A locally stored qhkit API token may expose service credentials.

Mitigation: Provision the token securely, limit access to it, and avoid agent-managed persistent credential setup.

Risk: Keyword and marketplace queries go to a paid third-party service, and larger results can cost more.

Mitigation: Disclose query sharing and estimated credits, obtain user consent before paid calls, and limit batch size.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-google-trends)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown text summarizing keyword trends and the credits consumed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected market and the paid qhkit service.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
