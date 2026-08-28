## Description:

Voicemaker helps an agent use an OOMOL-connected Voicemaker account to generate text-to-speech audio and list available voices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to fulfill Voicemaker text-to-speech requests from a connected account, including generating speech audio and discovering available voices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text-to-speech generation may consume account credits even though the skill presents the action alongside read-style operations.

Mitigation: Treat generate_tts as a user-approved billable action and confirm the requested text, voice options, and account-credit implications before execution.

Risk: The skill operates through the user's OOMOL-connected Voicemaker account.

Mitigation: Install and use the skill only when the user is comfortable with agents invoking Voicemaker through that connected account.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-voicemaker)
- [Voicemaker Homepage](https://voicemaker.in/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated audio URLs and usage details returned by Voicemaker actions.]

## Skill Version(s):

1.0.0 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
