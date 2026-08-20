## Description:

Drive Skroll decks through the official CLI for Skroll-specific create, edit, generate, version, export, brand, PDF, and PPTX workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[benlaval23](https://clawhub.ai/user/benlaval23)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a user specifically asks to manage Skroll presentations, brands, exports, versions, or generated deck content through the Skroll CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public deck links can expose deck content when deck visibility is changed to public or a public URL is shared.

Mitigation: Verify the deck contents, intended audience, and visibility before running update_deck --visibility public or sharing the publicUrl value.

Risk: Deck deletion, brand deletion, and organization-wide listing can affect or expose account-level Skroll assets.

Mitigation: Confirm the target deck, brand, organization scope, and user intent before running delete_deck, delete_brand, or list_decks --scope org.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/benlaval23/skills/skroll)
- [Skroll Product](https://skrollai.com)
- [Skroll CLI Documentation](https://skrollai.com/developers/cli)
- [Skroll MCP Documentation](https://skrollai.com/developers/mcp)
- [Skroll REST Documentation](https://skrollai.com/developers)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown with inline shell commands and CLI-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce downloaded PDF or PPTX files when the agent runs Skroll export commands.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
