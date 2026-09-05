## Description:

Use when a client needs to estimate China individual income tax on overseas brokerage or bank statements, prepare documents for the tax bureau, or offset annual stock gains and losses from local agent chats such as WorkBuddy or 豆包 Work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[masterbenc](https://clawhub.ai/user/masterbenc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and tax advisors use this skill in a local agent environment to estimate China individual income tax from overseas brokerage or bank statements, identify missing statement records, and prepare plain-language tax-bureau material suggestions. It is a calculation worksheet aid, not tax advice or an official CRS filing generator.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brokerage and bank statements may contain sensitive financial data.

Mitigation: Process statements only in the local agent environment, mask account numbers where practical, and do not upload identity documents.

Risk: Tax estimates can be incomplete or wrong when buy records, foreign withholding evidence, or residence facts are missing.

Mitigation: Clearly list missing records, exclude unmatched sells from the confirmed amount, and have a qualified person review results before filing.

Risk: Users may mistake the worksheet for official CRS or tax-submission material.

Mitigation: Do not generate official CRS forms, CRS XML, or compliance documents with fixed tax-residency claims; present the output as a calculation worksheet only.

## Reference(s):

- [小白问询话术](references/interview.md)
- [成本匹配](references/matching.md)
- [测算口径](references/tax-estimate.md)
- [税局材料建议](references/documents.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Plain-language tax estimate, missing-document notes, and optional local JSON extraction outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs must state that results are calculation worksheets requiring human review before formal filing or submission.]

## Skill Version(s):

3.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
