## Description:

Use the Linear CLI from an agent to discover commands, inspect setup, run account operations, and read JSON results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use the Linear CLI to find commands, inspect local setup, read Linear data, and perform account operations within the selected profile's permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Linear API includes write and destructive operations that can change or delete service data.

Mitigation: Check the selected profile and operation before running it; use --dry-run before writes and rely on the profile's permissions to limit access.

Risk: Security scan coverage was partial, so the benign verdict has medium confidence.

Mitigation: Review the skill before installing it in a sensitive environment.

## Reference(s):

- [Linear API overview](references/api.md)
- [Linear API queries](references/api/api-query.md)
- [Linear API mutations](references/api/api-mutation.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON command results and errors with CLI usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account operations are subject to the selected profile's permissions.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
