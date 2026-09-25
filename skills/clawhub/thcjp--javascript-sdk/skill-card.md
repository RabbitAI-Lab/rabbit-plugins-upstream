## Description:

Guides agents and developers through installing and using the inference.sh JavaScript/TypeScript SDK to call AI applications, build agent workflows, and integrate model outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill for guidance on adding the inference.sh JavaScript/TypeScript SDK to projects, configuring API access, and producing model-call examples and workflow integration notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests read, write, and command execution authority while guiding npm installation and project-file edits.

Mitigation: Review generated commands and file changes before execution, and use it only in workspaces where npm commands and project edits are acceptable.

Risk: SDK use can involve API keys, private prompts, source code, or regulated data being sent through an external inference workflow.

Mitigation: Avoid providing secrets, private code, regulated data, or production credentials until the SDK package, provider terms, and data-handling requirements have been verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/javascript-sdk)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bash, TypeScript, and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include npm install commands, SDK initialization snippets, API key environment variable guidance, and structured result examples.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
