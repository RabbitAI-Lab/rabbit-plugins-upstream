## Description:

Reliably ships content, code, or packages from source to a live target by guiding build, input validation, manifest registration, deployment, live verification, and announcement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tooled-app](https://clawhub.ai/user/tooled-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release operators use this skill to turn publish requests for content, code, or packages into a repeatable workflow that validates inputs, builds, deploys, verifies the live target, and logs or announces the release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide real publishing and deployment workflows that may make changes live publicly.

Mitigation: Use an explicit preview or confirmation step before production deploys, especially for public releases.

Risk: Missing target environment, deploy command, rollback command, or announcement channel details can lead to incomplete or incorrect release execution.

Mitigation: Document these project-specific details before using the skill for production publishing.

Risk: A release may be treated as complete even when the build, deployment, or live verification step failed.

Mitigation: Require the build to exit successfully, verify the live target returns healthy rendered content, and roll back using the documented command if verification fails.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tooled-app/skills/publish-pipeline)
- [OpenClaw](https://openclaw.ai)
- [Tooled](https://tooled.pro)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown with ordered workflow guidance, checklists, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers preflight, validation, manifest registration, build, deploy, live verification, announcement, changelog logging, failure handling, and rollback guidance.]

## Skill Version(s):

1.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
