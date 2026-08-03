## Description: <br>
Detects aggressive interactions in livestock and poultry from continuous barn videos, including fighting, biting, chasing and butting, and outputs behavior type, intensity level and alert level. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and farm operations teams use this skill to analyze barn image or video inputs for livestock and poultry conflict behavior, then review structured alerts, behavior segments, intensity levels, and historical reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Barn media, supplied URLs, and identity-linked analysis data may be sent to the provider's cloud API. <br>
Mitigation: Use only media approved for provider-side processing, avoid sensitive footage where possible, and confirm that the provider's handling of uploaded media is acceptable before deployment. <br>
Risk: The skill can silently create or reuse identity state and store tokens or profile data in a workspace SQLite database. <br>
Mitigation: Run the skill only in approved workspaces, restrict access to local state files, and monitor or rotate identity and token state according to local security policy. <br>
Risk: Behavior recognition results are advisory alerts and may be incomplete or incorrect. <br>
Mitigation: Treat reports as screening outputs and require farm operations, animal welfare, or veterinary review before intervention decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-aggressive-behavior-detection-analysis) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-compatible structured analysis summaries, with command-line examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include behavior types, intensity levels, alert levels, report links, and historical report tables.] <br>

## Skill Version(s): <br>
1.0.5 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
