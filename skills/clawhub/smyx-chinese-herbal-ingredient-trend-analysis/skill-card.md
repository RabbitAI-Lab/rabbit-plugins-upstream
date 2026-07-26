## Description: <br>
AI-powered active-ingredient accumulation trend assessment for medicinal herbs using high-resolution leaf images to estimate visual indicators, compare them with cultivar reference features, and report an accumulation trend level for harvest-window decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users in medicinal herb cultivation bases, GAP planting bases, herb cooperatives, and pharmaceutical raw-material operations use this skill to analyze leaf images or video and receive active-ingredient accumulation trend levels and harvest timing guidance. Agents can also query prior cloud-hosted analysis reports for the same skill workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends media and report-history requests to external services. <br>
Mitigation: Review destination services, network policy, and data handling requirements before installation or use. <br>
Risk: The skill can silently create or reuse a service identity and associate reports with that identity. <br>
Mitigation: Run only in environments where this account linkage is approved, and avoid using sensitive media unless the linked cloud account is acceptable. <br>
Risk: The skill stores authentication tokens in a local workspace database. <br>
Mitigation: Limit workspace access, rotate or remove tokens when decommissioning the skill, and avoid shared workspaces unless token persistence is acceptable. <br>
Risk: The skill includes unrelated pet-health or generic analysis components alongside the herb-analysis workflow. <br>
Mitigation: Review the packaged components and exposed commands before deployment to confirm only the intended workflow is enabled. <br>
Risk: The analysis estimates herb quality trends from visual features and does not provide chemical testing data. <br>
Mitigation: Use results as harvest-decision support and confirm formal quality claims with appropriate chemical or regulatory testing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-chinese-herbal-ingredient-trend-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis text with report links and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call external analysis and report-history services; local inputs are limited to supported image/video formats and documented file-size constraints.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
