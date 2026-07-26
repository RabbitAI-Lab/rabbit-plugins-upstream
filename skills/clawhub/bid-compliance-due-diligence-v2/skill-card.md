## Description: <br>
Performs public-source procurement and bidding-compliance due diligence on a target company, checking adverse bidding records, penalties, blacklists, related-party risk, and producing a structured risk warning report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement, compliance, and supplier-risk reviewers use this skill before onboarding or evaluating a company to identify public招投标 risk signals, official negative records, and related-party concerns. It supports quick screening and deeper audit-style reporting for business decision support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can be triggered by broad supplier-reliability prompts and may search public records for legal representatives or major shareholders. <br>
Mitigation: Use it only for procurement and bidding-compliance review, and make the review purpose explicit before running related-party checks. <br>
Risk: Public search results, official-site access limits, and knowledge-base coverage can leave important compliance conclusions incomplete or stale. <br>
Mitigation: Manually review important conclusions, cited official records, and legal references before using the report for business decisions. <br>
Risk: The skill is designed for public-source risk screening and does not provide legal advice. <br>
Mitigation: Route material supplier decisions or high-risk findings to qualified legal or compliance professionals for independent review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/bid-compliance-due-diligence-v2) <br>
- [README](artifact/README.md) <br>
- [Validation test cases](artifact/测试用例.md) <br>
- [Revision analysis](artifact/评析结论.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Structured Markdown risk report with tables, source notes, and recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include quick or deep sections, evidence confidence levels, filtered-source notes, legal-reference caveats, and manual-review disclaimers.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
