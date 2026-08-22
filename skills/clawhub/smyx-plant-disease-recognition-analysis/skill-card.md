## Description:

Identifies plant diseases from image or video inputs using computer vision and returns structured diagnostic reports with disease type, likely cause, and prevention suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farmers, gardeners, plant-protection staff, and developers use this skill to analyze plant disease symptoms in images or videos, retrieve structured diagnosis reports, and review prevention or control suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media and report metadata are sent to the provider's cloud service.

Mitigation: Use the skill only when the provider's retention and deletion practices are acceptable, and avoid submitting sensitive farm, location, account, or personally identifying media.

Risk: The skill may create or reuse persistent local identity state and store service tokens.

Mitigation: Review identity and token handling before deployment, restrict local state access, and clear stored credentials when decommissioning the skill.

Risk: Bundled configuration includes insecure private development endpoints.

Mitigation: Review and replace endpoint configuration with approved production HTTPS services before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-disease-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON diagnostic reports, with shell commands for invoking analysis and history queries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file paths or public URLs for plant images and videos; history queries can return report links.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
