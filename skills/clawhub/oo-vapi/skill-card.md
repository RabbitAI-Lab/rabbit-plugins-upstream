## Description:

Vapi (vapi.ai). Use this skill for ANY Vapi request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Vapi action schemas and run Vapi connector actions for assistants, calls, chats, sessions, phone numbers, tools, files, analytics, evaluations, scorecards, monitoring policies, insights, and provider resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes pipe-to-shell installer commands.

Mitigation: Avoid running those installer commands unless the oo CLI installer has been independently trusted and verified.

Risk: The test_code_tool_execution action can execute TypeScript code in Vapi's sandbox.

Mitigation: Treat it as high risk and run only code the user explicitly intended to execute.

Risk: Write and destructive actions can change or delete Vapi resources.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running any action tagged write or destructive.

## Reference(s):

- [Vapi Homepage](https://vapi.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-vapi)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI to inspect live action schemas before running Vapi connector actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
