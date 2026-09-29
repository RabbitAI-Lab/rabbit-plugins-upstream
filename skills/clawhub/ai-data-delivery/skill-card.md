## Description:

Helps teams turn partial data structures and business definitions into evidence-backed semantic models, checks, evaluations, and staged delivery artifacts for AI-powered data questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[franklinxkk](https://clawhub.ai/user/franklinxkk)

### License/Terms of Use:

MIT

## Use Case:

Field engineers, product managers, and data teams use this skill to define business entities and metrics from incomplete inputs, validate data relationships and constraints, diagnose incorrect data answers, and prepare staged handoffs with traceable evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included rebuild utility can stop local services and run supplied shell commands.

Mitigation: Review scripts before use; run the rebuild utility only when service interruption is intended, using trusted commands and project paths.

Risk: Incomplete or stale model and data evidence can lead to misleading validation conclusions.

Mitigation: Review the supporting inputs and reports, and keep claims unverified until the relevant data and evaluations are available.

## Reference(s):

- [Source repository](https://github.com/franklinxkk/ai-data-delivery)
- [ClawHub release](https://clawhub.ai/franklinxkk/skills/ai-data-delivery)
- [Semantic contract and validation guide](https://github.com/franklinxkk/ai-data-delivery/blob/74702dbd11994594a5a1fc9fda24a05d2cb3a40d/references/contract.md)
- [Delivery playbook](https://github.com/franklinxkk/ai-data-delivery/blob/74702dbd11994594a5a1fc9fda24a05d2cb3a40d/references/delivery-playbook.md)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, Validation reports]

**Output Format:** [Markdown guidance and commands; YAML semantic models and JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Validation conclusions depend on the available model, cases, and data evidence.]

## Skill Version(s):

0.1.0 (source: ClawHub release; bundled skill metadata: 0.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
