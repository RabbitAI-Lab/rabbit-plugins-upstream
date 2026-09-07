## Description:

Guides a GitLab agent to identify focused improvements for the helm-openclaw project and manage related merge requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab agents use this skill to propose focused improvements to the helm-openclaw project as merge requests and clean up stale self-created merge requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or close GitLab merge requests in the linked project.

Mitigation: Install it only for that intended project workflow, use a minimally scoped GitLab token, and review each merge-request creation or closure before allowing it.

Risk: The self-improvement framing is vague and could lead to broad, low-value, or unrelated changes.

Mitigation: Require each proposed merge request to address one focused issue and reject cosmetic or unsupported changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)
- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance and GitLab merge-request actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and a GitLab token for merge-request creation or closure.]

## Skill Version(s):

1.86.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
