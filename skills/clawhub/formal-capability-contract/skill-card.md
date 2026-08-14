## Description:

Defines executable precondition, postcondition, and invariant contracts for agent capabilities and verifies execution traces with deterministic clause-level results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to define formal contracts for actions, functions, or planning steps and evaluate whether execution traces satisfy those contracts. It is most relevant when users ask for formal verification, provable correctness, capability contracts, or precondition/postcondition/invariant checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled learning module can create or update local history containing usage records, errors, notes, and user preferences.

Mitigation: Review the skill before installation and avoid recording sensitive document contents, identifiers, secrets, or private user details in learner notes or preferences.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/formal-capability-contract)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python and shell command examples; verifier functions return JSON-serializable dictionaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The contract verifier reports capability, total, passed, provable_score, verdict, and per-trace failed clauses.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
