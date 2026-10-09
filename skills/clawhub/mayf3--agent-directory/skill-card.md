## Description:

Manages and maintains JSON profiles for agents, including roles, pipeline ownership, status, and long-term goals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mayf3](https://clawhub.ai/user/mayf3)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations maintainers use this skill to create, validate, update, and index agent profile JSON files for an agent team directory and pipeline views.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsafe path handling in helper scripts can allow crafted local filenames to execute code during validation.

Mitigation: Review the scripts before use, run them only against trusted workspace paths and trusted docs/agent-profiles files, and update them to pass paths as Python arguments and use mktemp before automation or CI use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mayf3/skills/agent-directory)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update or generate agent profile index JSON when its helper scripts are run.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
