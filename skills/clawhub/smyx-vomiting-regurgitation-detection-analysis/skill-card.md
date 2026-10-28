## Description:

Analyzes indoor pet videos for signs of vomiting or regurgitation and summarizes observed events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and veterinary care teams can review indoor camera footage for suspected vomiting or regurgitation, including event timing and visible vomit characteristics. Results are visual observations for follow-up, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared account handling could expose private footage or reports if caller isolation is incomplete.

Mitigation: Confirm caller isolation and access controls before using private footage or a shared agent.

Risk: Footage storage, deletion, login-token protection, and service charges are not clear from the available evidence.

Mitigation: Confirm storage and deletion practices, token protection, and applicable charges before uploading footage.

Risk: The security guidance reports that an export-only execution flag may be ignored.

Mitigation: Confirm that the flag is enforced before relying on it to limit execution.

Risk: Similar movements such as stretching or coughing may be mistaken for vomiting, and visual results do not establish a diagnosis.

Mitigation: Treat results as behavioral observations, check them against the footage and visible material, and consult a veterinarian for health concerns.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-vomiting-regurgitation-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON analysis reports and Markdown history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include event times, frequency, visible material descriptions, and report links; findings are observational and may be mistaken.]

## Skill Version(s):

1.0.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
