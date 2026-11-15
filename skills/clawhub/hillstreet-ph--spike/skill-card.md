## Description:

Run throwaway prototypes to validate feasibility, compare approaches, and report a verdict.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to test a concrete feasibility question before committing to a production build. It creates a minimal prototype, exercises an edge case, and reports findings with a recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial because a local reference could not be resolved.

Mitigation: Check the unresolved reference and decide whether it affects your use before installing.

Risk: Throwaway prototype code could be mistaken for production-ready implementation.

Mitigation: Rewrite and review spike code before incorporating the approach into production.

## Reference(s):

- [Spike on ClawHub](https://clawhub.ai/hillstreet-ph/skills/spike)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands, Markdown]

**Output Format:** [A small runnable prototype and a Markdown verdict with evidence and a recommendation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prototype artifacts are intended for feasibility checks; production use requires a separate implementation.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
