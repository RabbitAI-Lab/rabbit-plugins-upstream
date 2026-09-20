## Description:

OpenAI connector skill for reading, creating, updating, and deleting OpenAI data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect OpenAI connector schemas and run OpenAI account actions through the oo CLI, including model lookup, Responses API calls, embeddings, images, moderation, audio, and batch operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run broad read, write, and destructive actions against a credentialed OpenAI account.

Mitigation: Confirm the exact action, payload, cost impact, and target resource before any write or destructive command is run.

Risk: The first-time setup section includes remote shell install commands for the oo CLI.

Mitigation: Install the oo CLI only through a verified package or reviewed installer before relying on this skill.

Risk: OpenAI usage can affect paid or sensitive workloads.

Mitigation: Review the skill before installation and limit use to accounts and data appropriate for the intended workload.

## Reference(s):

- [OpenAI API](https://openai.com/api/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-openai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when the skill runs commands with --json.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
