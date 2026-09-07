## Description:

Diagnose GitHub Personal Access Token failures across GitHub API, Contents API, GitHub Pages, and skill mirror push workflows before declaring a token expired or revoked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to troubleshoot GitHub PAT authentication failures, distinguish local runtime and environment propagation issues from GitHub-side revocation or policy causes, and safely validate repository writes after authentication is fixed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may read a local GitHub PAT and test it against GitHub.

Mitigation: Install only when that access is acceptable, use a fine-grained short-lived PAT when possible, and never print, paste, commit, or log the full token.

Risk: After authentication is fixed, the skill includes a repository write-path validation step.

Mitigation: Before any write, require confirmation of the exact repository, branch, file path, proposed diff, and rollback plan; prefer a disposable test repository.

## Reference(s):

- [Token Failure Mode Decision Tree](references/token-failure-modes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and diagnostic steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Avoids printing full secrets; records status, scopes, root cause, and command corrections.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
