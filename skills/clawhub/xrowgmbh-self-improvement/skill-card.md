## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab agents use this skill to review their recent work on the helm-openclaw project, capture useful improvement ideas, and manage focused merge requests for those improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to create or close GitLab merge requests using a token.

Mitigation: Use a narrowly scoped GitLab token and confirm every merge request creation or closure before it is executed.

Risk: Broad automatic invocation based only on self-improvement language could trigger unintended GitLab workflow automation.

Mitigation: Install and invoke the skill only for the named helm-openclaw workflow where this behavior is intended.

## Reference(s):

- [helm-openclaw project](https://gitlab.com/xrow-public/helm-openclaw)
- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-self-improvement)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, GitLab merge requests, guidance]

**Output Format:** [Markdown or plain text with GitLab workflow actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the glab command-line tool and a narrowly scoped GITLAB_TOKEN.]

## Skill Version(s):

1.91.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
