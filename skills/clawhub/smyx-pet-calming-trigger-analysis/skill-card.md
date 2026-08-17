## Description:

Analyzes pet monitoring media for anxiety, howling, or prolonged loneliness signals and returns structured reports, recommendations, and report links for soothing-trigger decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet camera videos or media URLs for anxiety-related behavior, then review structured results and historical reports before deciding whether to trigger soothing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet monitoring media and report queries are sent to lifeemergence.com services.

Mitigation: Use only with footage appropriate for external processing and with clear consent and retention expectations.

Risk: The skill can create or reuse a local identity and store tokens in the workspace data directory.

Mitigation: Run it in a controlled workspace, review generated data after use, and avoid shared environments for sensitive footage.

Risk: The authoritative security verdict is suspicious because of remote login and local token persistence behavior.

Mitigation: Review the skill and its network endpoints before installation, and restrict execution if the remote analysis service is not required.

## Reference(s):

- [Pet Calming Trigger Analysis API Documentation](artifact/references/api_doc.md)
- [SMYX Analysis API Error Codes](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown text with structured JSON analysis content, recommendations, historical report listings, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local mp4/avi/mov files up to 10 MB and public media URLs; URL media is downloaded by the remote API service.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter: 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
