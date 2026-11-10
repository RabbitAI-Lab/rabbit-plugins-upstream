## Description:

Diagnoses GitHub Personal Access Token failures by checking command and environment handling, request details, and independent clients before concluding that a token is expired or revoked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to diagnose GitHub API and repository push authentication failures across shells and programming languages. It guides secret-safe checks, permission troubleshooting, and verification before repository updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The troubleshooting workflow may make remote repository changes without clear user authorization.

Mitigation: Require clear user authorization before writes, retrieve the current remote blob SHA before updating, and verify the resulting file.

Risk: Security scan coverage is partial because some referenced material could not be resolved.

Mitigation: Review the unresolved references and scan the complete skill materials before installation.

## Reference(s):

- [Token Failure Mode Decision Tree](references/token-failure-modes.md)
- [GitHub authenticated user endpoint](https://api.github.com/user)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Code]

**Output Format:** [Markdown with inline command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes secret-safe diagnostic and verification steps.]

## Skill Version(s):

1.0.6 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
