## Description:

Determines nine TCM constitution types from facial photos, videos, or URLs and returns constitution scores, tendency analysis, health-risk context, and personalized wellness suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and wellness application developers use this skill to analyze face images or videos for Traditional Chinese Medicine constitution identification and to retrieve prior analysis reports. The output is for wellness reference and should not replace professional medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face photos, videos, or submitted URLs are sent to configured lifeemergence.com cloud APIs.

Mitigation: Confirm the publisher's retention, deletion, account-linking, and data-use policies before installation, and avoid sensitive images unless those terms are acceptable.

Risk: The skill silently creates or reuses an internal identity and stores tokens locally.

Mitigation: Review identity creation, account association, and token-storage behavior before deployment, especially in shared or regulated environments.

Risk: The skill returns wellness and health-related report content that could be mistaken for medical advice.

Mitigation: Present results as Traditional Chinese Medicine wellness reference only and direct users with symptoms or medical concerns to qualified healthcare professionals.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-tcm-constitution-recognition-analysis)
- [Publisher Profile](https://clawhub.ai/user/18072937735)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown text with structured JSON report content and optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include constitution types, scores, health-risk context, recommendations, historical report lists, and export links returned by the configured cloud API.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
