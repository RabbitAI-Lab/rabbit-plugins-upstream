## Description:

Wise (wise.com). Use this skill for ANY Wise request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Wise account information through an OOMOL-connected account, including exchange rates, supported transfer currencies, and available personal or business profiles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that run directly in a shell.

Mitigation: Do not let an agent run those installer commands automatically; install the oo CLI only through a trusted, verified method.

Risk: The skill operates through an account-connected Wise integration.

Mitigation: Confirm account connection steps yourself and review connector payloads before allowing any action that could affect account data.

## Reference(s):

- [Wise homepage](https://wise.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wise)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns Wise connector results as JSON.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
