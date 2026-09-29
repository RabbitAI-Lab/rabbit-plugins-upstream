## Description:

Scaffolds a new GitHub repository with project documentation, issue and pull request templates, CI workflows, and a local initial commit; publishing requires explicit approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qikairo7](https://clawhub.ai/user/qikairo7)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create a new open-source repository with documentation, contribution templates, CI configuration, and a local Git commit before deciding whether to publish it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled CI templates can enable release or package-publishing jobs beyond basic lint and test checks.

Mitigation: Review or remove publish and release jobs before pushing, especially workflows using NPM_TOKEN, GITHUB_TOKEN, contents: write, or id-token: write.

Risk: Scaffolding creates a new repository and a local Git commit.

Mitigation: Run only when a new repository and initial commit are intended; confirm the target directory before proceeding.

## Reference(s):

- [oss-scaffold on ClawHub](https://clawhub.ai/qikairo7/skills/oss-scaffold)
- [Repository settings profile](references/settings-profiles/PROFILE.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Repository scaffold files and a Markdown status report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a local initial commit; publishing requires explicit approval.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
