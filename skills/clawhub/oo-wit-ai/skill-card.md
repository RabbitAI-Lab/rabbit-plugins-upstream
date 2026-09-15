## Description:

This skill helps an agent operate Wit.ai through OOMOL's oo CLI to read, create, update, and delete apps, intents, entities, traits, utterances, language detection results, and message analysis data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage Wit.ai resources through an OOMOL-connected account. It supports app, intent, entity, trait, utterance, language detection, and message analysis workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can run a remote installer directly on the user's machine.

Mitigation: Review official installation instructions and verify the installer or use a trusted package manager before execution.

Risk: The skill includes write and destructive Wit.ai actions that can change or delete account data.

Mitigation: Confirm the exact action, target, and payload with the user before allowing write or destructive commands.

Risk: Use requires trusting the OOMOL oo CLI and granting access to a Wit.ai-connected account.

Mitigation: Install only in environments where OOMOL CLI use and Wit.ai account access are approved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-wit-ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Wit.ai Homepage](https://wit.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payload and response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run through the OOMOL oo CLI; connector responses are JSON when --json is used.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
