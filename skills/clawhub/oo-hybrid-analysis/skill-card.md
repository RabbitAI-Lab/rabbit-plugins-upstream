## Description:

Hybrid Analysis (hybrid-analysis.com). Use this skill for ANY Hybrid Analysis request - searching and reading data. Whenever a task involves Hybrid Analysis, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security analysts use this skill to query Hybrid Analysis through an OOMOL-connected account for file-hash investigation, sandbox report state, and report summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer scripts for the oo CLI.

Mitigation: Review the setup path before installing and prefer a trusted, versioned source with checksum or signature verification.

Risk: The skill depends on the connected Hybrid Analysis account and OOMOL credentials.

Mitigation: Only connect the Hybrid Analysis account intended for this use and rely on routine read-only lookups after setup is complete.

Risk: Authentication, connection, or billing failures can block connector actions.

Mitigation: Use the documented first-time setup fallback only after a command fails with the matching auth, connection, scope, credential, or billing error.

## Reference(s):

- [Hybrid Analysis homepage](https://www.hybrid-analysis.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-hybrid-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
