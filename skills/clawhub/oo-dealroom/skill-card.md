## Description:

Dealroom helps agents search and read Dealroom company, investor, and transaction data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Dealroom action schemas and perform read-only searches over companies, investors, and transactions with an OOMOL-connected Dealroom account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an OOMOL-connected Dealroom account and the oo CLI.

Mitigation: Install only when that connector is intended, and review the CLI installation and authentication steps before use.

Risk: Future connector actions could be marked write or destructive.

Mitigation: Confirm the exact payload and effect with the user before allowing any write action, and require explicit approval for destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-dealroom)
- [Dealroom Homepage](https://dealroom.co)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires fetching each Dealroom action's live schema before constructing payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
