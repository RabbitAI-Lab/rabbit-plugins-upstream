## Description:

Routes Snipe-IT search and read requests through the OOMOL oo CLI connector without exposing raw API credentials to the agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Snipe-IT connector schemas and retrieve current-user, category, company, hardware, status-label, and user data through OOMOL-connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that could execute arbitrary code if run without verification.

Mitigation: Use a verified installation method for the oo CLI instead of blindly running curl-to-bash or PowerShell iex commands.

Risk: The skill routes Snipe-IT data through OOMOL and depends on trust in that connector.

Mitigation: Install only when that routing is intended, and keep the connected Snipe-IT API key least-privileged and read-only where possible.

## Reference(s):

- [Snipe-IT homepage](https://snipeitapp.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-snipe-it)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI schema-inspection and connector-run commands for read-only Snipe-IT actions.]

## Skill Version(s):

1.0.2 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
