## Description: <br>
Conducts open-ended Q&A on image content based on computer vision and large language models, supporting natural language responses to questions about image content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to ask open-ended questions about uploaded or URL-hosted visual media and receive natural language or structured analysis results. It also supports retrieving account-linked visual question-answering history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided images, videos, questions, and account-linked history may be sent to the publisher's cloud service. <br>
Mitigation: Avoid sensitive media unless the publisher provides clear retention, deletion, and account-control terms. <br>
Risk: The skill may create or reuse a local identity and persist backend tokens in the workspace data directory. <br>
Mitigation: Run it in an isolated workspace and review or remove persisted identity and token data after use. <br>
Risk: Model-generated visual answers can be incomplete or incorrect. <br>
Mitigation: Verify important conclusions against the source media or another trusted source before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-visual-qa-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files] <br>
**Output Format:** [Markdown-style report text or JSON, with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model-generated answers, structured analysis data, report links, or account-linked history results.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release metadata; artifact frontmatter is 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
