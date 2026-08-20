## Description:

Map candidate skills to an interview plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting teams use this skill to compare a candidate profile with role requirements and create a concise interview plan covering matched requirements, missing requirements, and interview topics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Candidate profiles can contain personal or sensitive HR information.

Mitigation: Provide only the candidate and role details needed for interview planning and avoid unnecessary private data.

Risk: The generated interview plan could omit relevant role requirements or overstate a candidate's fit.

Mitigation: Have a recruiter or hiring team member review the plan before using it in an interview process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/candidate-interview-agenda-identifier)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Structured interview_plan object with candidate_id, matched_required, missing_required, and topics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses only candidate and role information supplied in the current request.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
