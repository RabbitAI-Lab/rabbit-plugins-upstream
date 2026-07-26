## Description: <br>
Analyzes plant leaf images or videos to identify curling direction, margin scorch patterns, likely causes such as drought or disease, and directional recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, growers, agricultural IoT operators, and developers use this skill to send plant leaf images, videos, or URLs for cloud-assisted diagnosis of leaf curling and margin scorch symptoms. It returns structured findings, likely cause rankings, guidance, and links to reports or historical report data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends plant media or media URLs to lifeemergence cloud services for analysis and report retrieval. <br>
Mitigation: Use it only with images, videos, and URLs that are approved for that external service, and avoid submitting sensitive location, farm, or account information unless the workspace accepts that data sharing. <br>
Risk: The skill silently creates or reuses an internal user identity and can query cloud history associated with that identity. <br>
Mitigation: Confirm that automatic account linkage and cloud history access are acceptable before installing or running the skill in shared workspaces. <br>
Risk: The skill stores returned service tokens in a local SQLite database. <br>
Mitigation: Treat the workspace data directory as credential-bearing, restrict access to it, and clear or rotate stored tokens when the skill is removed or moved between environments. <br>
Risk: Diagnosis output is advisory and can misclassify visually similar drought, disease, pesticide injury, fertilizer burn, or cold-stress symptoms. <br>
Mitigation: Use the result as decision support and confirm serious disease or treatment decisions through field inspection or a qualified crop advisor. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-leaf-curling-scorch-diagnosis-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Leaf curling and scorch API documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured text with optional report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write analysis output to a local file when requested; historical report output is retrieved from the configured cloud service.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter says 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
