## Description:

Fluxguard lets an agent inspect live Fluxguard action schemas and run account, page, category, webhook, and crawl operations through an OOMOL-connected CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Fluxguard resources and retrieve Fluxguard account data from an agent session while keeping Fluxguard credentials mediated by OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include curl-to-bash and irm-to-iex installer commands that can execute remote code locally.

Mitigation: Do not allow an agent to run those installer commands automatically; use a verified installation path for the oo CLI when available.

Risk: The skill can create, update, or delete Fluxguard pages, sites, categories, and webhooks.

Mitigation: Require user confirmation for write actions and explicit approval of the exact target and payload before destructive actions.

Risk: Fluxguard operations are mediated through OOMOL, which means actions depend on the user's OOMOL-connected account and service availability.

Mitigation: Install only when OOMOL-mediated Fluxguard access is acceptable and review account, connection, and billing errors before retrying.

## Reference(s):

- [Fluxguard homepage](https://fluxguard.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fluxguard)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include Fluxguard action names, request payloads, command output summaries, and confirmation prompts for write or destructive actions.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
