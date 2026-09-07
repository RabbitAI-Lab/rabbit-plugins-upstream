## Description:

Detects aggressive interactions in livestock and poultry from continuous barn videos, including fighting, biting, chasing, and butting, and outputs behavior type, intensity level, and alert level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and farm operations teams use this skill to submit livestock or poultry barn videos for aggressive-behavior screening, receive structured findings on fight-like events, and review alert levels or historical analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn videos or video URLs are sent to a configured remote analysis service.

Mitigation: Install only where remote processing of the submitted video data is acceptable, and avoid submitting footage that contains unrelated sensitive content.

Risk: The skill can create or reuse an internal identity and store service tokens in the workspace data directory.

Mitigation: Review account and token handling before deployment, restrict workspace access, and rotate or remove stored tokens when the skill is no longer needed.

Risk: Published defaults include development API endpoints and automatic history-report triggers.

Mitigation: Switch defaults to approved production endpoints and narrow history-report triggers before operational use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-aggressive-behavior-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Aggressive Behavior Detection API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured analysis text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior labels, intensity and alert levels, event lists, report links, and historical report records.]

## Skill Version(s):

1.0.9 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
