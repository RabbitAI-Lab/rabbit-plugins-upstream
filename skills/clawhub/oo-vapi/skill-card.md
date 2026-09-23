## Description:

Vapi provides agent access to read, create, update, and delete Vapi resources through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Vapi assistants, calls, chats, evaluations, phone numbers, sessions, tools, files, analytics, and monitoring workflows from an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Install oo from a trusted source and verify the installer separately before allowing the agent to use it.

Risk: The skill can create, update, upload, or delete Vapi resources, including phone numbers, tools, files, assistants, calls, chats, and evaluations.

Mitigation: Require explicit user confirmation of the exact action, target, and payload before write, upload, phone-number, tool-update, or destructive operations.

Risk: The test_code_tool_execution action can run TypeScript code in Vapi's code tool sandbox.

Mitigation: Review the code and intended effect with the user before running test_code_tool_execution.

## Reference(s):

- [Vapi Homepage](https://vapi.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Vapi Skill](https://clawhub.ai/oomol/skills/oo-vapi)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions can return JSON data and execution metadata from the OOMOL Vapi connector.]

## Skill Version(s):

1.0.5 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
