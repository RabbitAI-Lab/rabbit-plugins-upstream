## Description: <br>
Expands the disease identification library to cover economic-crop-specific diseases such as corn northern and southern leaf blight, potato late blight, peanut leaf spot, and tomato viral disease for precise leaf-disease recognition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agricultural developers use this skill to analyze crop leaf images, videos, or URLs for economic-crop-specific disease identification and structured report retrieval. It focuses on visual recognition and report output, not treatment or prevention recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Leaf images, videos, URLs, and report requests are sent to a remote Life Emergence service. <br>
Mitigation: Review the service and data handling expectations before installation, and avoid submitting sensitive or unrelated media. <br>
Risk: The skill can silently create or reuse a local identity and persist session tokens in a workspace SQLite database. <br>
Mitigation: Install only in trusted workspaces, review local persistence before use, and remove stored identity or token data when the skill is no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-crop-specific-disease-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis reports with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include disease type, confidence, symptom description, report links, and Markdown tables for historical reports.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter says 1.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
