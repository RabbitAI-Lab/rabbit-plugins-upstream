## Description:

Refines vague, ambiguous, incorrect, or incomplete user commands into valid, fact-checked, environment-aware, and clearly scoped requests before execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and agent operators use this skill to clarify user intent, correct unsupported assumptions, and produce safer execution plans before tools or system actions are run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may restate or refine unclear requests before action, which can affect destructive, financial, or security-sensitive workflows if the refined action is not confirmed.

Mitigation: Require explicit user confirmation of the final refined action before proceeding with destructive, financial, or security-sensitive tasks.

Risk: Refinement guidance can still be incorrect or misleading if the agent accepts assumptions without checking the current environment or facts.

Mitigation: Review the final intent, scope, environment constraints, and verification plan before executing generated commands or changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/user-intent-refinement)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown or plain text guidance, with code blocks or shell commands when needed for the refined request.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-only skill; no code, installation behavior, persistence, or hidden data access reported by security evidence.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
