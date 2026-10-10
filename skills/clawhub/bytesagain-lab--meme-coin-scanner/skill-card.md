## Description:

Scan new meme coins for risks and opportunities, including liquidity, trading activity, and holder-safety checklist review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bytesagain-lab](https://clawhub.ai/user/bytesagain-lab)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect meme-coin token listings, price and liquidity data, and checklist-style scam indicators before deciding what additional manual due diligence is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may overstate automated meme-coin safety checks.

Mitigation: Treat outputs as preliminary signals only and verify tokens with independent scanners, contract review, and manual due diligence before acting.

Risk: The bundled local security utility can persistently log sensitive inputs.

Mitigation: Do not enter secrets, passwords, private keys, seed phrases, or confidential values into the bundled hash, encrypt, password, or related utility commands.

Risk: Token addresses and listing queries may be sent to DexScreener.

Mitigation: Avoid querying sensitive or confidential token addresses when external API disclosure is unacceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bytesagain-lab/skills/meme-coin-scanner)
- [BytesAgain homepage](https://bytesagain.com)
- [DexScreener token API](https://api.dexscreener.com/latest/dex/tokens/{})

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Terminal text and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query DexScreener for token and listing data; informational output only and not financial advice.]

## Skill Version(s):

2.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
