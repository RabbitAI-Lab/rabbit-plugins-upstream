## Description:

Analyzes fixed-camera videos of an older person's resting hand to estimate tremor frequency and amplitude and report a non-diagnostic resting-tremor risk level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers, elder-care operators, and health-monitoring developers use this skill to submit resting-hand videos or URLs for motion analysis and receive structured tremor metrics, risk level, and report links. Results are screening aids and do not replace professional neurological assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive elderly hand videos and report history are processed by a remote service.

Mitigation: Use only with explicit consent from the monitored person or authorized caregiver, and avoid submitting real health videos until the remote-processing terms and retention practices are acceptable.

Risk: Report history is linked to an automatically managed identity.

Mitigation: Confirm the intended account linkage before use and avoid sharing workspaces where the local identity state may be reused unexpectedly.

Risk: The security evidence reports local token persistence and plaintext HTTP development configuration.

Mitigation: Require HTTPS production endpoints and protected or non-persistent token handling before using the skill with real health media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-hand-tremor-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands]

**Output Format:** [Markdown text containing structured analysis results and report links, with JSON available through the detailed output mode.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local video files or video URLs; can also list cloud report history associated with the automatically managed identity.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter declares 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
