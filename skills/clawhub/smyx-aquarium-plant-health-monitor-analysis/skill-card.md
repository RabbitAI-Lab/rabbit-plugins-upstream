## Description: <br>
Analyzes aquarium plant images or videos to identify visual health issues such as discoloration, leaf damage, algae, and deficiency symptoms, then returns a structured assessment with care suggestions and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Aquarium keepers, aquascaping shops, and support agents use this skill to analyze plant media for visible health symptoms and retrieve structured health reports. It supports local files, public media URLs, and report-history queries through the skill's configured services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Aquarium media or supplied URLs may be sent to external lifeemergence.com or open.lifeemergence.com services. <br>
Mitigation: Install and run the skill only when that external transfer is acceptable for the media being analyzed. <br>
Risk: The skill may create or reuse a local/backend identity and retain authentication tokens locally. <br>
Mitigation: Review the workspace data directory before and after use, and clear persisted identity or token data when retention is not desired. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-plant-health-monitor-analysis) <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write an optional result file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
