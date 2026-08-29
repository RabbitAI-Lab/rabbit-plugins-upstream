## Description:

Diagnoses GitHub Personal Access Token authentication failures by checking command syntax, environment propagation, request parameters, independent client results, and then GitHub-side permission or revocation causes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to diagnose GitHub REST API, Contents API, and HTTPS push authentication failures without exposing the full PAT. It helps distinguish local shell or runtime issues from token revocation, permission, SSO, organization policy, or account-state causes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A full GitHub PAT could be exposed in logs, chat, shell history, or diagnostic output.

Mitigation: Inspect only byte count, prefix, suffix, and presence signals; never print or paste the full token, and rotate any token that was exposed.

Risk: A diagnosis could incorrectly treat one failed request as proof that the token is expired or revoked.

Mitigation: Cross-validate with independent clients using the same secret, then investigate GitHub-side causes only after local command, environment, and request issues are ruled out.

Risk: Contents API write commands could overwrite a remote file with stale state.

Mitigation: Fetch the current remote blob SHA before writing, review the proposed write, and verify the raw file after the update.

## Reference(s):

- [Token Failure Mode Decision Tree](references/token-failure-modes.md)
- [GitHub REST API User Probe Endpoint](https://api.github.com/user)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown diagnosis with inline shell commands and verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not output or require printing full GitHub PAT values.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
