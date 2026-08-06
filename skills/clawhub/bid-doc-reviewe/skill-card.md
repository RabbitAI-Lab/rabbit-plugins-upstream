## Description: <br>
招标文件审查智能助手Bid Doc Reviewe helps users review Chinese tendering and bidding documents against referenced compliance knowledge bases and produce risk findings, compliance ratings, and actionable revision guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External procurement, bidding, and compliance users use this skill to review tender announcements, prequalification documents, bidding documents, invitations, clarifications, evaluation reports, and candidate-award notices for Chinese tendering-law compliance. It is intended to support human review with risk lists, compliance grades, revision suggestions, and items requiring confirmation, not to provide final legal advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reviews tendering and bidding compliance, but its output could be mistaken for final legal advice. <br>
Mitigation: Treat results as AI-assisted review only and have the responsible procurement, legal, or compliance professional verify conclusions before use. <br>
Risk: Uploaded procurement documents may contain confidential or commercially sensitive information. <br>
Mitigation: Avoid uploading confidential materials unless the user is comfortable with the platform and referenced knowledge-base workflow handling them. <br>
Risk: Regulatory guidance may be incomplete or outdated when the referenced knowledge bases do not cover a specific rule or recent change. <br>
Mitigation: Require knowledge-base anchoring for legal claims, disclose unsupported points, and verify current laws, local rules, or administrative guidance before relying on the report. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/bid-doc-reviewe) <br>
- [招投标实务与合规 knowledge base](https://ima.qq.com/wiki/?shareId=6bd8e274955cb1493860613dbaed87ceb170158b2ac6ac32bbca7f9a4f534a6a) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown report with risk tables, compliance grading, recommendations, confirmation items, and disclaimer text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask up to three structured follow-up questions when required project information is missing; urgent or long-file reviews may begin with a high-risk summary.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter and manifest report 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
