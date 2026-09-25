## Description:

Guides an agent through verifying tests, detecting Git environment state, presenting integration choices, and cleaning up a completed development branch.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill after implementation and tests are complete to decide whether to merge locally, create a pull request, or keep the branch. It emphasizes user confirmation before integration, branch deletion, or worktree cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled pre-merge helper can expose detected secrets in logs.

Mitigation: Do not run it where logs may capture secrets unless secret matches are suppressed or redacted.

Risk: The bundled pre-merge helper can make failed tests look non-fatal.

Mitigation: Do not use it as a CI gate, and require a separate passing project test run before merge or pull request creation.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown workflow with command snippets and integration menus]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces decision guidance for Git branch completion; does not itself execute repository changes.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
