## Description: <br>
参与政府采购的投标人自判中小企业等资格、正确填写《中小企业声明函》、识别专门面向项目并避开虚假声明骗标风险的辅助自检工具。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External bidders in Chinese government-procurement processes use this skill to self-check SME and related policy-benefit eligibility, prepare safe declaration guidance, and identify false-declaration risks before bidding. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is specialized for Chinese government-procurement policy and may be misleading outside that legal and language context. <br>
Mitigation: Use it only as an auxiliary policy-checking tool for relevant procurement scenarios, and verify conclusions against original procurement documents or qualified legal counsel. <br>
Risk: Users may upload unrelated confidential documents while seeking eligibility guidance. <br>
Mitigation: Limit uploaded material to procurement documents and company facts needed for the self-check. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chesaram/skills/bid-policy-checker) <br>
- [README](artifact/README.md) <br>
- [Test Cases](artifact/references/test-cases.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with structured eligibility findings, policy-benefit checks, declaration guidance, warnings, and citations when the configured knowledge base has matching source text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Chinese-language bidder-facing self-check guidance and should ask for missing procurement and company-profile details before making key determinations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence; artifact manifest/frontmatter also report 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
