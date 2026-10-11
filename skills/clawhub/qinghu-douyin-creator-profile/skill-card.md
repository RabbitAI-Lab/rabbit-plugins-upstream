## Description:

Looks up Douyin creator profiles by homepage URL and reports follower counts, likes, posts, location, and biography.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting creators and marketers use this skill to retrieve and summarize a Douyin creator's public profile metrics from a supplied homepage URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profile lookups incur variable credit charges.

Mitigation: Estimate charges and obtain user approval before paid calls; report actual credits used.

Risk: Automatic installation or upgrades can modify the host environment.

Mitigation: Approve host changes explicitly and prefer a preinstalled, pinned qhkit version.

Risk: Configuring the external tool may persist an access token.

Mitigation: Prefer an ephemeral QHKIT_TOKEN and review credential handling before installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-douyin-creator-profile)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown summary; optional tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits consumed for paid calls.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
