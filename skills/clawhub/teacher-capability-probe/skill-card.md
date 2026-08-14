## Description:

Probe and evaluate teacher models to map capability boundaries and failure modes before or after model distillation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate capability probes from teacher model signatures, score probe results, and produce structured capability profiles that guide distillation and follow-up validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled learner module can keep local usage history, errors, notes, and user preferences.

Mitigation: Do not enter secrets, personal data, customer details, or sensitive business context in learner notes or preferences; delete or disable learned_patterns.json when persistent memory is not needed.

## Reference(s):


## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON reports and Markdown guidance with bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Probe generation and evaluation run locally; learner commands may update learned_patterns.json.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
