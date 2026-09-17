## Description:

Vapi (vapi.ai) skill for reading, creating, updating, and deleting Vapi data through the OOMOL oo CLI connector instead of direct API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Vapi assistants, calls, chats, sessions, phone numbers, tools, files, analytics, evaluations, monitoring policies, scorecards, insights, and provider resources through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands are included for first-time setup.

Mitigation: Verify the installer independently and use it only when the oo CLI is missing.

Risk: The skill can create, update, or delete Vapi resources.

Mitigation: Confirm the exact payload, target resource, and expected effect before running write or destructive actions.

Risk: The skill can execute TypeScript through Vapi's code tool sandbox.

Mitigation: Require explicit user approval before code execution and review the code and expected output first.

## Reference(s):

- [Vapi homepage](https://vapi.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Vapi skill page](https://clawhub.ai/oomol/skills/oo-vapi)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON request or response payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing and destructive Vapi actions require explicit user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
