## Description:

A Chinese K12 chemistry lab coaching skill that helps students reason through apparatus choice, operation order, observed phenomena versus conclusions, testing and impurity removal, experiment safety, and exam preparation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students and education agents use this skill for Chinese middle-school and early high-school chemistry lab tutoring, especially experiment reasoning, safety boundaries, required-lab review, and operation-exam preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Students may request unsafe at-home chemistry procedures or ways to bypass lab safety rules.

Mitigation: The skill should keep the artifact's safety boundary: explain principles, refuse at-home hazardous steps, refuse shortcuts around safety norms, and direct real experiments to supervised school labs.

Risk: Long-term profile memory, cross-skill sharing, and reminders can involve minor student data.

Mitigation: Enable those behaviors only after student or guardian consent, keep each consent channel independent, and honor view, correction, deletion, pause, sharing-control, and export requests.

Risk: Emergency, crisis, or active lab-accident situations may exceed normal tutoring scope.

Mitigation: Stop tutoring flow, avoid diagnosis or treatment instructions beyond basic classroom safety, involve a trusted adult or teacher, and localize emergency contacts for the deployment region.

Risk: Using the skill during an active exam or operation test could undermine assessment integrity.

Mitigation: Do not answer or hint during an active exam; ask the learner to return after the assessment for review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-lab-coach)
- [化学实验指南：气体制取、必做实验与操作考试](references/chemistry-lab-guide.md)
- [实验安全约定（理化生通用）](shared/lab-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text tutoring responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide consent-gated profile, handoff, and reminder guidance when the deployment supports those behaviors.]

## Skill Version(s):

2.3.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
