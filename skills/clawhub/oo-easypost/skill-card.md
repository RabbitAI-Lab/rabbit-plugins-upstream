## Description:

EasyPost (easypost.com). Use this skill for EasyPost requests involving reading, creating, and updating data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations users use this skill to inspect EasyPost connector schemas and run EasyPost address, tracker, and carrier actions through the oo CLI. It supports read operations directly and requires confirmation before state-changing EasyPost actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path tells users to run remote installer scripts directly.

Mitigation: Review the setup path before installing and prefer a trusted, versioned package or a downloaded installer that is verified before execution.

Risk: Write actions can create EasyPost addresses or trackers and change account state.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write.

## Reference(s):

- [EasyPost homepage](https://www.easypost.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL EasyPost connection](https://console.oomol.com/app-connections?provider=easypost)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-easypost)

## Skill Output:

**Output Type(s):** [shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to fetch live connector schemas before building action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
