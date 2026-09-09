## Description:

AppGrowing Global intelligent ad creative analysis assistant finds relevant global ad creatives from user instructions, returns automated analysis, and supports Inspire ideation mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcloud](https://clawhub.ai/user/youcloud)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, app teams, and analysts use this skill to request AppGrowing Global ad creative searches, receive multilingual creative strategy analysis, and optionally download creatives from an authenticated analysis session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ad-analysis prompts and API-key-authenticated requests are sent to AppGrowing/Youcloud services.

Mitigation: Use the skill only where sharing those prompts with YouCloud is acceptable, store YOUCLOUD_API_KEY in the environment, and rotate the key if it is exposed.

Risk: The skill can download creative media locally after a materials scope is selected.

Mitigation: Use explicit download scopes, review downloaded files before redistribution, and keep downloaded materials in an appropriate local workspace.

Risk: Broad natural-language triggers may invoke analysis when a user intended only general discussion.

Mitigation: Prefer explicit commands such as /aggclaw, /aggclaw-game, /aggclaw-app, or /agg_inspire when starting a session.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/youcloud/skills/aggclaw)
- [AppGrowing](https://appgrowing.net/)
- [Usage Examples](references/example.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis responses, plain-text errors, PowerShell command examples, and local downloaded media files when materials are requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the caller's language, requires YOUCLOUD_API_KEY, waits up to 600 seconds for analysis, and saves requested downloads locally.]

## Skill Version(s):

1.2.2 (source: server release evidence; artifact frontmatter reports 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
