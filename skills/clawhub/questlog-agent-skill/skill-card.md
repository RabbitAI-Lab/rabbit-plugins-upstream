## Description:

Maintain an explicit Markdown commitments ledger with a local cockpit for NOW, next actions, deadlines, waiting items, workstream states and inbox capture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antreasantoniou](https://clawhub.ai/user/antreasantoniou)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Questlog to maintain a local Markdown ledger of active commitments, next actions, deadlines, waiting items, workstream state, and inbox capture without relying on external services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local HTTP cockpit is not a remotely authenticated multi-user service.

Mitigation: Bind and use it only on loopback, do not expose the port through a network or reverse proxy, and do not run it as root.

Risk: Queued instruction drafts may be mistaken for executed automation.

Mitigation: Treat pending drafts as untrusted notes until a separate reviewed and authorized automation path consumes them.

Risk: Mutable install commands and unpinned sources can change between review and installation.

Mitigation: Install from a pinned, inspected revision when possible and review the repository before installation.

Risk: Commitment data may contain private local state.

Mitigation: Use a dedicated private QUESTLOG_ROOT, keep ledgers and local paths out of public reports, and back up state independently.

## Reference(s):

- [Ledger format](references/ledger-format.md)
- [README](README.md)
- [Security](SECURITY.md)
- [ClawHub skill page](https://clawhub.ai/antreasantoniou/skills/questlog-agent-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with inline shell commands and ledger Markdown updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local commitment-capture guidance and bounded ledger changes; it does not execute pending instruction drafts.]

## Skill Version(s):

1.0.0 (source: changelog and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
