## Description:

Ably connector skill for reading, creating, updating, and deleting Ably data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Ably channels, presence, history, stats, and push subscriptions, and to publish messages or activate channels through the oo CLI with OOMOL-managed credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer pipelines for the oo CLI.

Mitigation: Install the oo CLI only from a verified, version-pinned source, or manually inspect and verify the installer before execution.

Risk: Write actions can publish messages or activate channels in Ably.

Mitigation: Confirm the exact action payload and expected effect with the user before running any write-tagged action.

Risk: Destructive actions can delete Ably push notification channel subscriptions.

Mitigation: Require explicit approval for the specific subscription target before running any destructive action.

Risk: Connector action schemas may vary at runtime.

Mitigation: Inspect the live connector schema before constructing each action payload.

## Reference(s):

- [ClawHub Ably Skill](https://clawhub.ai/oomol/skills/oo-ably)
- [Ably Homepage](https://ably.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill expects live connector schema inspection before action payloads are constructed.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
