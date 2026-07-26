## Description: <br>
Audits existing investment content about Chinese listed companies by breaking claims into checkable units, comparing them against official disclosures and market data, and producing a concise fact-check report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ovalpatty](https://clawhub.ai/user/ovalpatty) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, analysts, and reviewers use this skill to audit stock pitches, advisor advertisements, investment commentary, earnings-call retellings, and screenshots for consistency with official A-share and related disclosure sources. It is for public-information fact checking, not for generating investment research, valuation models, or buy/sell advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may mistake public-information consistency checks for investment advice or professional due diligence. <br>
Mitigation: Present outputs as fact-check reports only, preserve the skill's documented boundary against buy/sell advice, and require users to make their own investment judgments. <br>
Risk: Optional market-data or registry tools may be unavailable, which can leave some valuation-percentile or equity-chain claims unresolved. <br>
Mitigation: Report unsupported claims as pending, estimated, or downgraded instead of inventing data or forcing a verdict. <br>
Risk: Fact-check reports can create false confidence if source links or official records are reconstructed from memory. <br>
Mitigation: Use only actually retrieved URLs in reports; when a source is known but not fetched, provide a pending source locator rather than a fabricated link. <br>


## Reference(s): <br>
- [Skill README](artifact/README.md) <br>
- [Evidence Priority and Conflict Resolution](artifact/evidence-rules.md) <br>
- [Claim Normalization Reference](artifact/normalization.md) <br>
- [Narrative Error Taxonomy](artifact/narrative-errors.md) <br>
- [Official Channels and Retrieval Paths](artifact/official-channels.md) <br>
- [AKShare](https://github.com/akfamily/akshare) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown fact-check report with quick-read summary, verdict tables, source notes, and risk signals] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a closed verdict set for claim outcomes and degrades unsupported or unavailable evidence rather than filling gaps.] <br>

## Skill Version(s): <br>
0.1.2 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
