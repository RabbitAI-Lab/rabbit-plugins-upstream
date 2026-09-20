## Description:

Helps CHO agents generate CTO/CISO training plans, courseware, exams, certificates, and progress reports for security and compliance training.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmithfan](https://clawhub.ai/user/johnsmithfan)

### License/Terms of Use:

MIT-0

## Use Case:

CHO, CTO, and CISO agents use this skill to turn a training plan into local courseware, exam materials, score records, certificates, progress reports, and action items. It is intended for operational training support, with certificate and audit outputs reviewed before they are used as compliance evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exam, certificate, approval, signature, and audit records may be mistaken for compliance evidence.

Mitigation: Use the outputs as local training support only until real exam records, signer authorization, and cryptographic signatures are independently verified.

Risk: Shared or untrusted TRAINING_WORKSPACE directories may weaken record integrity or path containment assumptions.

Mitigation: Run the skill only in a controlled local workspace with trusted inputs and reviewed workspace configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/johnsmithfan/skills/cto-ciso-training)
- [Publisher profile](https://clawhub.ai/user/johnsmithfan)
- [Artifact README](artifact/README.md)
- [Artifact security review](artifact/SECURITY_REVIEW.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON files with local shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local training artifacts under knowledge-base/training; certificate, signature, audit, and approval fields need independent verification before compliance use.]

## Skill Version(s):

2.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
