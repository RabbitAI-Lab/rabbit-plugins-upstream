## Description:

Helps data-delivery teams turn partial data structures and business definitions into reviewable semantic models, validation evidence, and phased delivery assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[franklinxkk](https://clawhub.ai/user/franklinxkk)

### License/Terms of Use:

MIT

## Use Case:

Field engineers, product managers, and data teams use this skill to model business entities and metrics from incomplete schemas, check data and join assumptions, diagnose question-answering failures, and package evidence for staged delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The deployment helper can stop a service and start a detached process; its shell fallback may execute more than intended.

Mitigation: Run only with explicit authorization in an isolated project environment; review the build and start commands and avoid the helper where service disruption is unacceptable.

Risk: A started process may inherit sensitive environment settings.

Mitigation: Use a restricted environment with only the credentials and permissions required for the task.

Risk: Endpoint tools can send requests to configured services, and generated reports can contain sensitive prompts, SQL, or results.

Mitigation: Use only services you are authorized to test and redact sensitive content before sharing outputs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/franklinxkk/skills/ai-data-delivery)
- [Semantic contract and validation boundaries](references/contract.md)
- [Onboarding from partial materials](references/onboarding.md)
- [Diagnosis playbook](references/diagnosis-playbook.md)
- [Delivery playbook](references/delivery-playbook.md)
- [Tool commands and boundaries](references/tools.md)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Code, Shell commands, Reports]

**Output Format:** [Markdown guidance, YAML semantic models, commands, and generated validation or delivery files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts and mock results require review and evidence before production acceptance.]

## Skill Version(s):

0.1.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
