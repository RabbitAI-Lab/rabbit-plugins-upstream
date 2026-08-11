## Description:

Coordinates skill authoring, testing, security auditing, documentation, and release management to publish installable skill packages to public registries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill publishing teams use this agent configuration bundle to coordinate authoring, evaluation, security review, documentation, and release preparation for installable skill packages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can edit files and run shell commands while preparing packages for release.

Mitigation: Review generated changes, test results, and release artifacts before publishing anything publicly.

Risk: Stored and reused task context may carry incorrect assumptions into later publishing steps.

Mitigation: Confirm release metadata, security guidance, and package contents before using the release-manager role.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/t3ratech/skills/skill-publishing-team)
- [Publisher profile](https://clawhub.ai/user/t3ratech)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, code changes, shell commands, configuration updates, and release guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coordinates five roles: skill author, test engineer, security auditor, documentation writer, and release manager.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
