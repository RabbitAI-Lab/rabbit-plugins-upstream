## Description:

Creates a source-linked, five-section draft for researching a company before its financial results are released, with each claim tied to quoted source text and an anchor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Equity analysts and researchers use the skill to turn a company name or ticker and source materials into a structured preliminary research note. It requires quoted evidence and source anchors for claims, and excludes ratings, target prices, and share-price forecasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional remote tool discovery uses the CUE retrieval channel; the security review does not establish whether remote requests succeed or what data they transmit.

Mitigation: Configure CUE_API_KEY only when channel retrieval is needed; otherwise use user-supplied materials, and review the data involved before using remote tools.

Risk: The security review reports note-checker weaknesses and is partial because one local reference was missing.

Mitigation: Treat checker results as a format check, review the cited source documents and claims independently, and account for the incomplete scan when assessing the skill.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-cn-equity-research-note)
- [CUE tool catalog (optional retrieval channel)](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown research note with quoted claims, source anchors, and a source list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five content sections plus a key-figure table; claims carry source references. No ratings, target prices, or share-price forecasts.]

## Skill Version(s):

0.2.2 (source: server-resolved release metadata, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
