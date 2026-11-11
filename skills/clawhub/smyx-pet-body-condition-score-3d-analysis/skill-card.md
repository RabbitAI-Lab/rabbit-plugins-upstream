## Description:

Analyzes multi-angle pet videos to estimate a 3D body shape and Body Condition Score (BCS, 1–9), and returns standardized observations without diagnosing disease or prescribing treatment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet care platform developers and operators can use the skill to estimate a pet’s body condition from video and review structured observations or cloud-hosted analysis reports. A veterinarian should assess health concerns and confirm body condition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags credential-handling risks and says the credential destination is unclear.

Mitigation: Confirm the credential destination and trusted service endpoint before use; avoid sending private pet footage until they are clear.

Risk: The skill handles user identity and cloud report history beyond its stated video-analysis purpose, and the security review says this behavior needs clarification.

Mitigation: Clarify identity association and history access before enabling analysis or report-list features; explain these behaviors to users.

Risk: Visual BCS estimates may differ from hands-on assessment and are not a veterinary diagnosis.

Mitigation: Treat results as informational and ask a veterinarian to assess health concerns or confirm body condition.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-body-condition-score-3d-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured pet body-condition observations and BCS estimate; JSON output or Markdown report/list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include body type classification, risk observations, recommendations, and report links; results are visual estimates and are not a diagnosis.]

## Skill Version(s):

1.0.14 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
