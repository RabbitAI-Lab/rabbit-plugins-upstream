## Description:

Provides safety-focused guidance for pushing a selected workspace project to GitHub without accidentally publishing unrelated or sensitive files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huanmeng9527](https://clawhub.ai/user/huanmeng9527)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when publishing workspace files to GitHub, GitLab, or Bitbucket from a shared or parent Git repository. It helps verify repository boundaries, stage only intended files, configure basic ignore rules, and use a GitHub Contents API fallback when ordinary git push repeatedly times out.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workspace files could be published with secrets, unrelated projects, or large generated folders if the wrong directory or staged file list is used.

Mitigation: Confirm the exact target directory, repository visibility, and explicit staged file list before pushing; inspect git status for secrets and unrelated files.

Risk: A project inside a parent Git repository could pollute the parent history or expose files outside the intended project.

Mitigation: Compare the Git top-level directory with the target directory and initialize an isolated repository when the target is nested inside a parent repository.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes command sequences, safety checks, and fallback upload guidance; does not produce files directly.]

## Skill Version(s):

1.0.0 (source: target metadata and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
