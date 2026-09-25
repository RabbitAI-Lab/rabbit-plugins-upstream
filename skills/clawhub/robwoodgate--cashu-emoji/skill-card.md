## Description:

Encode and decode Cashu tokens that are hidden inside emojis using Unicode variation selectors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robwoodgate](https://clawhub.ai/user/robwoodgate)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to encode Cashu bearer tokens or short text into emoji variation selectors, decode received emoji messages, and optionally inspect Cashu token metadata without spending funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decoded Cashu tokens are bearer assets and may represent spendable value.

Mitigation: Treat decoded token strings like cash; do not place them in public chat transcripts, logs, screenshots, or issue reports.

Risk: Messaging systems can truncate or normalize Unicode variation selectors, making the hidden payload unrecoverable or corrupt.

Mitigation: When decoding fails or returns partial text, ask for the emoji token to be resent and prefer delivery formats that preserve hidden characters.

Risk: Local metadata parsing can show mint, unit, and amount, but cannot prove a Cashu token is valid or unspent.

Mitigation: Use metadata-only handling for inspection and verify token status with an appropriate wallet or mint before relying on value.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/robwoodgate/skills/cashu-emoji)
- [ClawHub publisher profile](https://clawhub.ai/user/robwoodgate)
- [Unicode Variation Selectors](https://unicode.org/charts/nameslist/n_FE00.html)
- [Unicode Variation Selectors Supplement](https://unicode.org/charts/nameslist/n_E0100.html)
- [Paul Butler emoji-encoder technique](https://github.com/paulgb/emoji-encoder)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Decoded Cashu metadata is produced by local parsing and does not prove token validity or spend status.]

## Skill Version(s):

0.1.0 (source: package.json and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
