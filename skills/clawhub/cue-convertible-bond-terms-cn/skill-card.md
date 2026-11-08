## Description:

Turns an A-share convertible bond prospectus or issuance announcement into eight verbatim clause cards with source anchors, while leaving investment judgments for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and analysts use this skill to extract and compare the stated terms of one China A-share convertible bond from its prospectus or issuance announcement. It preserves source wording and flags missing terms for review instead of providing investment or transaction advice.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Optional online parsing may involve provider retention or charges, and could expose confidential annotations.

Mitigation: Before enabling online parsing, verify the provider endpoint, retention terms, and charges; do not send confidential annotations without authorization.

Risk: The structural checker does not establish that extracted terms or figures are factually accurate.

Mitigation: Check every quotation, source anchor, and numeric trigger against the original prospectus or announcement.

## Reference(s):

- [Convertible bond clause reference](artifact/references/cb-clauses.md)
- [Cue data service configuration](https://cuecue.cn/hub/mcp)
- [Cue attachment parsing configuration](https://cuecue.cn/hub/omni-reader)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown clause card]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Eight clause entries with verbatim quotations and source anchors; missing terms are labeled, numeric triggers remain verbatim, and investment judgments are marked [待人工].]

## Skill Version(s):

0.1.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
