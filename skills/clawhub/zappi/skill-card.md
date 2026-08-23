## Description:

Zappi gives an agent a prepaid Spark USDB spend pot with a hard balance-based cap, where the agent holds the local key and spending stops when the pot is empty.

This skill is ready for commercial/non-commercial use.

## Publisher:

[edogbeatz](https://clawhub.ai/user/edogbeatz)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use Zappi to create, fund, check, and spend from a small prepaid Spark USDB pot for agent payments without exposing a main wallet seed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback helper can download and run remote wallet-signing code that may access the local seed file.

Mitigation: Prefer the bundled sign.mjs and avoid --pull-signer or auto-downloaded signers unless the code integrity and publisher domain have been independently verified.

Risk: The skill handles wallet seed material for a finance workflow.

Mitigation: Use only small prepaid amounts, never use a main wallet seed, and treat the local seed file as sensitive wallet software data.

Risk: Overspending or loss exposure is still possible up to the funded pot balance.

Mitigation: Fund only the intended spend cap and verify the Spark address with --check or --expect before opening, funding, or spending.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/edogbeatz/skills/zappi)
- [Zappi skill manifest](https://pot.zappi.money/skill.json)
- [Bundled signer source](artifact/sign.mjs)
- [Fallback key and signer helper source](artifact/new-key.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate on local seed files and Spark addresses; successful command output is machine-readable JSON.]

## Skill Version(s):

1.0.37 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
