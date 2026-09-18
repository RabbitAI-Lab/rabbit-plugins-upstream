## Description:

Deck.co (deck.co). Use this skill for ANY Deck.co request: reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Deck.co through an OOMOL-connected account, including creating and retrieving website sources, listing sources and agents, retrieving agent task summaries, and testing API key authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes remote installer commands for the oo CLI, and the security review warns not to let an agent run those installer commands unattended.

Mitigation: Review the installer path before use; prefer a verified package, pinned release, or manual installation method trusted by the user.

Risk: Deck.co write actions can create or change remote service state.

Mitigation: Confirm the exact action payload and intended effect with the user before running actions tagged as write or destructive.

## Reference(s):

- [ClawHub Deck.co skill page](https://clawhub.ai/oomol/skills/oo-deck-co)
- [Deck.co homepage](https://www.deck.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide an agent to inspect live connector schemas before running Deck.co actions and to confirm state-changing payloads with the user.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
