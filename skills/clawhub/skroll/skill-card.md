## Description:

Skroll helps agents write React/TSX presentation modules and use the Skroll CLI to create, publish, version, and export decks as PDF or PPTX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[benlaval23](https://clawhub.ai/user/benlaval23)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and presentation authors use this skill to create, revise, publish, version, and export Skroll presentation decks through the Skroll CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to operate a Skroll workspace through CLI commands, including deck deletion and visibility changes.

Mitigation: Install only when that workspace access is intended; before delete or visibility-change commands, confirm the exact deck or brand ID/title and prefer archiving where possible.

Risk: Authentication requires a Skroll API key, OAuth token, or browser login for CLI access.

Mitigation: Use the documented Skroll authentication flow and avoid exposing credentials in deck source, logs, or shared output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/benlaval23/skills/skroll)
- [Skroll Product](https://skrollai.com)
- [Skroll CLI Documentation](https://skrollai.com/developers/cli)
- [Skroll MCP Documentation](https://skrollai.com/developers/mcp)
- [Skroll REST Documentation](https://skrollai.com/developers)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and React/TSX code references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Skroll deck source modules and exported PDF or PPTX files through the Skroll CLI.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
