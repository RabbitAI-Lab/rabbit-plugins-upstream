## Description:

Guides publishing SKILL.md files to ClawHub and diagnosing publication failures across the history, ai-custom-skills, and ai-thoughts repositories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Maintainers of the referenced repositories use this skill to publish skill updates through GitHub Actions, troubleshoot skipped or failed runs, and verify the published version on ClawHub.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A workflow run could publish public skill updates from an unintended repository or account.

Mitigation: Before following the workflow, confirm the target repository, remotes, GitHub Actions owner guard, and ClawHub token; verify the live version after publishing.

## Reference(s):

- [Publish Skills on ClawHub](https://clawhub.ai/j3ffyang/skills/publish-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explains publishing steps, workflow failures, and checks of the published version.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
