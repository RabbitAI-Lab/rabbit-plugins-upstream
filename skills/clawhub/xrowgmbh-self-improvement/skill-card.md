## Description:

A skill for personal growth and self-improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers working on the named GitLab project use this skill to turn useful agent-improvement findings into merge requests, assign them to themselves, and manage older unaccepted merge requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish merge requests and close older merge requests without clearly limiting those actions to work the user authorized.

Mitigation: Use it only for explicitly authorized work on the named project; review findings before publication, approve each closure individually, use a minimally scoped token, and inspect the referenced gitlab-agent skill.

## Reference(s):

- [helm-openclaw GitLab project](https://gitlab.com/xrow-public/helm-openclaw)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, API Calls]

**Output Format:** [Findings and merge request content, with GitLab merge request actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and GITLAB_TOKEN; actions can publish a merge request or close an older merge request.]

## Skill Version(s):

1.121.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
