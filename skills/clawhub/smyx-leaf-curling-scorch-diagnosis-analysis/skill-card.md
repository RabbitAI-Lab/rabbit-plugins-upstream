## Description: <br>
Uses plant leaf images or videos to detect curling direction and margin scorch patterns, then returns likely causes such as drought stress, disease, pesticide damage, or fertilizer burn with directional recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External growers, agronomists, and developers use this skill to analyze plant leaf imagery, identify curling and margin-scorch patterns, and receive likely-cause rankings with practical next-step guidance. It can also query cloud-hosted historical diagnosis reports associated with the skill account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends supplied media or URLs to lifeemergence.com services for analysis. <br>
Mitigation: Use only with images, videos, and URLs that are acceptable to process through that external service. <br>
Risk: The skill can silently initialize or reuse an account identity and query cloud-hosted report history. <br>
Mitigation: Review account linkage expectations before installation and use an isolated account or workspace when testing. <br>
Risk: The skill may create or reuse a local workspace database and store returned service tokens there. <br>
Mitigation: Restrict local filesystem access, inspect stored credentials after use, and remove or rotate tokens when they are no longer needed. <br>


## Reference(s): <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-leaf-curling-scorch-diagnosis-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON analysis reports with diagnosis details, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write report output to a user-specified file when --output is used.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
