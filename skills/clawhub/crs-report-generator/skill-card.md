## Description:

Use when a client needs to estimate China individual income tax on overseas brokerage or bank statements, prepare documents for the tax bureau, or offset annual stock gains and losses from local agent chats such as WorkBuddy or 豆包 Work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[masterbenc](https://clawhub.ai/user/masterbenc)

### License/Terms of Use:

MIT-0

## Use Case:

External advisers or local agent users use this skill to estimate China individual income tax from overseas brokerage or bank statements, identify missing cost-basis records, and prepare a reviewable document set for the tax bureau. It is a tax-estimate workflow, not tax advice or an official CRS filing generator.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brokerage and bank statements may contain names, addresses, account numbers, balances, and transaction history.

Mitigation: Use only in a trusted local environment, redact unnecessary account identifiers when practical, and do not upload ID documents.

Risk: The tax estimate may be incomplete when buy records or earlier statements are missing.

Mitigation: Mark unmatched sales as missing buy records and exclude them from the estimated tax until supporting statements are available.

Risk: The result could be mistaken for a formal tax opinion or official CRS filing.

Mitigation: State that the output is an estimate worksheet and require qualified human review before filing or paying tax.

## Reference(s):

- [小白问询话术](artifact/references/interview.md)
- [成本匹配](artifact/references/matching.md)
- [测算口径](artifact/references/tax-estimate.md)
- [税局材料建议](artifact/references/documents.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown summary with optional local JSON parser output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes missing-document notes, sensitive-document handling guidance, and a human-review caveat before filing or payment.]

## Skill Version(s):

3.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
