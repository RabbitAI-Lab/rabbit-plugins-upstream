## Description:

Teach agents to register pages into the LYGO Pure-Data lattice through a public register portal pack and a safety-gated CLI that creates local digest witness records, ledger data, Continuum claims, and Star Chart node submission JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external agents use this skill to register public pages or operator-supplied files as digest-based Pure-Data witness records. It is useful when an agent needs to guide a human through the register portal, perform consent-gated archiving, or produce local submission artifacts for later steward review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can archive operator-supplied files or explicitly approved HTTPS URLs, so private files, credentials, cookies, internal URLs, or confidential pages could be captured if the operator points the agent at them.

Mitigation: Use the consent flags deliberately, prefer public or reviewed inputs, and review generated witness outputs before sharing them.

Risk: External full-stack or zip links are outside the inspected ClawHub package.

Mitigation: Treat those links as separate artifacts and scan or review them independently before use.

Risk: The multi-step archive chain writes several local artifacts and may prepare data for later publication workflows.

Mitigation: Prefer stepwise commands when possible; use the chain confirmation and export authorization flags only after human review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/deepseekoracle/skills/lygo-pure-data-witness)
- [ClawHub Release Link](https://clawhub.ai/deepseekoracle/lygo-pure-data-witness)
- [Register Portal](https://deepseekoracle.github.io/lygo-protocol-stack/data-vault/register.html)
- [Pure-Data UI](https://deepseekoracle.github.io/lygo-protocol-stack/data-vault/pure-data.html)
- [Source Mirror Link from Metadata](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/clawhub/mirrors/lygo-pure-data-witness)
- [ClawHub Security Audit](https://clawhub.ai/deepseekoracle/skills/lygo-pure-data-witness/security-audit)
- [Portal Training](references/PORTAL_TRAINING.md)
- [Security Notes](references/SECURITY.md)
- [SkillSpector Audit Response](references/SKILLSPECTOR_AUDIT.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and local JSON artifact paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local witness cards, snapshots, egg fragments, Continuum claims, ledger JSON, export-pack metadata, and Star Chart submission JSON under operator-selected output paths.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
