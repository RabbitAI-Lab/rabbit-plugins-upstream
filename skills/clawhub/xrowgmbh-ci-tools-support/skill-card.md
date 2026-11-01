## Description:

Triage and answer CI Tools components catalog support issues and help requests in GitLab discussions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

External users and maintainers use this agent to triage and answer CI Tools component support questions in GitLab discussions, grounding replies in component documentation and public references while protecting private issue details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Relevant GitLab discussions may be unlocked without checking the reason they were locked or obtaining moderator approval.

Mitigation: Restrict use to the intended support project and require maintainer approval before unlocking an existing discussion.

Risk: Support answers may be unreliable if the promised component documentation is missing from the release bundle.

Mitigation: Verify that the relevant component references are present before relying on answers; ask a focused question when evidence is incomplete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, GitLab discussion updates]

**Output Format:** [Markdown support response with descriptive references and, when needed, GitLab labels or discussion updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers are grounded in bundled component documentation and public sources; private details are kept out of public replies, and missing context leads to a focused question.]

## Skill Version(s):

4.228.6 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
