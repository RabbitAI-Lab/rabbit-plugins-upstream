## Description:

Apify (apify.com). Use this skill for ANY Apify request — searching and reading data. Whenever a task involves Apify, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to operate Apify through an OOMOL-connected account, inspect live connector schemas, retrieve actor, user, dataset, and run information, and start actor runs when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can start Apify actor runs through the connected account, which may change external state or incur cost.

Mitigation: Require explicit user confirmation before run_actor, including the actor id, full payload, expected cost, and external effects.

Risk: The skill includes remote installer commands for the oo CLI.

Mitigation: Do not let an agent run remote installer commands automatically; install the CLI through a verified source where possible.

Risk: The security verdict is suspicious due to unclear confirmation around actor runs and unverified installer commands.

Mitigation: Install only if the user trusts OOMOL and understands that the connected Apify account may be used to start actor runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-apify)
- [Apify homepage](https://apify.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector schema inspection commands, Apify action requests, JSON payload guidance, and recovery steps for authentication, connection, or billing errors.]

## Skill Version(s):

1.0.3 (source: evidence.release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
