## Description:

Triage and answer CI Tools components catalog support issues and help requests in GitLab discussions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to answer CI Tools component support requests in GitLab with concise, evidence-based guidance and public references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The instructions tell the agent to unlock an already locked discussion, which could override a moderation decision.

Mitigation: Require maintainer authorization before removing any existing discussion lock.

Risk: The agent handles GitLab support issues that may contain private details.

Mitigation: Limit GitLab access to intended support projects, make issues confidential before discussing private details, and never copy private details into public issues, merge requests, or snippets.

Risk: The skill relies on bundled component documentation to ground support answers.

Mitigation: Verify the promised reference documentation is present before relying on its answers.

## Reference(s):

- [CI Tools component documentation](https://ci-tools.xrow.de/Components/)
- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with links and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actionable support answers grounded in public references or request-provided details.]

## Skill Version(s):

4.228.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
