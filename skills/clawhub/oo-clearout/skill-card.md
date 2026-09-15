## Description:

Clearout helps agents verify email addresses, check Clearout credits and limits, and classify addresses through an OOMOL-connected Clearout account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Clearout email verification and account-classification actions through the oo CLI without handling raw Clearout API credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands without documented integrity checks.

Mitigation: Review the installer source before execution and prefer an official pinned package or verifiable download when available.

Risk: Using the skill requires signing in to OOMOL and connecting Clearout, which can persist account access outside the immediate agent run.

Mitigation: Connect only the required Clearout account, review granted scopes, and revoke or rotate credentials when access is no longer needed.

Risk: Email verification queries may involve personal or business contact data.

Mitigation: Submit only data that the user is authorized to verify and avoid sending unnecessary bulk or sensitive address lists.

## Reference(s):

- [Clearout ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-clearout)
- [Clearout Homepage](https://clearout.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions return JSON responses from the oo connector, including data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
