## Description:

Combines facial blood flow and emotional characteristics to analyze stress index, anxiety tendency, and depression tendency for mental health monitoring scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to analyze face images or videos for stress index, anxiety tendency, depression tendency, recommendations, report links, and cloud report history. The outputs are mental-health assessment references and should not be treated as clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images, videos, and derived psychological-stress assessments may be sent to configured lifeemergence.com services.

Mitigation: Use only with explicit consent and after verifying the provider, retention policy, deletion policy, and data handling requirements.

Risk: Automatic history lookup and local account or token persistence may expose prior assessment records or credentials in shared environments.

Mitigation: Run in an isolated environment, review local identity and token storage before deployment, and clear stored credentials according to policy.

Risk: Stress, anxiety, and depression tendency outputs may be mistaken for clinical diagnosis.

Mitigation: Present results as screening references only and direct sustained or concerning findings to qualified mental-health professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychological-stress-assessment-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands]

**Output Format:** [Markdown text with structured JSON report content and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the returned report text to a local output file when the output option is used.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
