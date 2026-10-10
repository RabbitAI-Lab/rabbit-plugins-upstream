## Description:

Analyzes keywords that generate exposure and conversions for one or more Amazon ASINs over a selected week or month.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and advertising analysts use this skill to identify converting, declining, and ineffective keywords for ASINs and inform listing and ad optimization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency setup can install Node and qhkit and change the local PATH.

Mitigation: Review the package and installation steps before allowing changes; use a trusted, isolated environment.

Risk: Configuring qhkit can persist an API token on the machine.

Mitigation: Use an approved credential-handling method and review where credentials will be stored before setup.

Risk: Keyword queries are paid and charges can increase with result volume.

Mitigation: Estimate costs and obtain user consent before paid calls; disclose actual credits charged.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-order-keyword)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [Concise Markdown findings; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports marketplace, period, sample size, and credits charged when applicable.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
