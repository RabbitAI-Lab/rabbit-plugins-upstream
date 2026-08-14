## Description:

This skill guides an agent to inspect opportunities for improvement in a GitLab project and create, assign, or close merge requests when appropriate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to have an agent identify meaningful project improvements and prepare narrowly scoped GitLab merge requests. It is most appropriate when merge-request automation is expected and reviewed by a human.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill presents itself as personal self-improvement while instructing an agent to perform GitLab merge-request automation.

Mitigation: Treat it as GitLab merge-request automation, disclose that behavior to users, and require explicit confirmation before any merge request is created, assigned, or closed.

Risk: Use of GITLAB_TOKEN can grant the agent project-modifying access.

Mitigation: Use a GitLab token intentionally scoped to the target project and limited to the permissions needed for reviewed merge-request work.

Risk: The skill can close older merge requests created by the agent.

Mitigation: Require review of the target merge request, last activity date, and review state before allowing closure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [Referenced GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown merge-request content with GitLab CLI actions or guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and GITLAB_TOKEN; may create, assign, or close GitLab merge requests.]

## Skill Version(s):

1.81.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
