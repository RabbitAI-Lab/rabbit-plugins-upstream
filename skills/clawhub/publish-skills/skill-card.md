## Description:

Guides publishing SKILL.md files to ClawHub and diagnosing publication failures across the history, ai-custom-skills, and ai-thoughts repositories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers maintaining the named skill repositories use this skill to coordinate ClawHub publishing, troubleshoot failed or skipped releases, and verify published versions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository and workflow actions can publish unintended skill changes.

Mitigation: Review skill changes and target repositories before authorizing commits, pushes, or workflow runs.

Risk: Applying this account-specific playbook outside its named publishing setup may trigger the wrong release workflow.

Mitigation: Use it only for the specified ClawHub account and repositories, and verify the resulting version on ClawHub.

## Reference(s):

- [Publish Skills on ClawHub](https://clawhub.ai/j3ffyang/skills/publish-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Publishing and verification steps for the named repositories.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
