## Description:

Zipcodebase lets an agent search postal-code data, list postal codes by city or state, run radius and distance queries, and check account status through an OOMOL-connected Zipcodebase account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need an agent to retrieve Zipcodebase postal-code information, run distance or radius lookups, or check remaining account credits without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands executed directly in a shell.

Mitigation: Review the installer path before installation and prefer official OOMOL CLI documentation, a package manager, or a downloaded installer with checksum or signature verification.

Risk: Setup commands may run with elevated privileges if launched from an elevated shell.

Mitigation: Run setup from a normal user shell unless elevated installation privileges are intentionally required.

## Reference(s):

- [Zipcodebase Skill Page](https://clawhub.ai/oomol/skills/oo-zipcodebase)
- [Zipcodebase Homepage](https://zipcodebase.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas to shape JSON payloads and returns connector responses as JSON when actions are executed.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
