## Description:

Triage and answer CI Tools components catalog support issues and help requests in GitLab discussions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

CI Tools maintainers and support agents use this skill to triage GitLab support requests and provide actionable answers grounded in public component documentation, repository content, or the request itself.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may reopen a locked support discussion without checking the moderation reason or confirming authorization.

Mitigation: Before reopening a locked discussion, review its moderation reason and confirm the support workflow authorizes the action; ask a human maintainer if either is unclear.

Risk: The security scan was partial because a referenced path was missing, and the bundled component reference directory is not present in the supplied artifact.

Mitigation: Verify each answer against accessible public documentation or repository sources; if the needed reference is unavailable, ask a focused question or request maintainer review instead of guessing.

## Reference(s):

- [CI Tools Components documentation](https://ci-tools.xrow.de/Components/)
- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown support replies with explanations, ordered checks, and references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers and next steps grounded in available public evidence; avoid repeating private details.]

## Skill Version(s):

4.239.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
