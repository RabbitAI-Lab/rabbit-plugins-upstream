## Description:

AI-powered pet sleep quality analysis from a fixed bed/rest-area camera that distinguishes sleeping and awake states, estimates sleep duration, counts roll-overs and startle-awakenings, and produces a 0-100 sleep-quality score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, animal hospitals, and boarding centers use this skill to analyze pet sleep-period video and review sleep duration, roll-over counts, startle-awakening frequency, sleep-quality scoring, and related guidance. Results are visual sleep indicators and are not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private pet-camera footage and report history may be sent to the publisher's service.

Mitigation: Use only with footage approved for sharing with the publisher, and avoid private household video unless the service's data handling is acceptable.

Risk: Unsafe default HTTP or test endpoints can expose video, account data, or reusable tokens in transit.

Mitigation: Configure HTTPS production endpoints before use and block local or test HTTP defaults in deployment.

Risk: Reusable identity and token values may be stored locally.

Mitigation: Run in an isolated account and workspace, rotate credentials after testing, and clear local token or user state when retiring the skill.

Risk: Sleep-quality findings could be mistaken for veterinary diagnosis.

Mitigation: Treat results as visual sleep indicators and seek veterinary review for persistent or severe abnormalities.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-sleep-quality-analysis-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and structured JSON report text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the report text to a user-specified output file.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
