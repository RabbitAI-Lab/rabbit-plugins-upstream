## Description:

Make (make.com). Use this skill for ANY Make request - reading, creating, updating, and deleting data. Whenever a task involves Make, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Make action schemas and operate scenarios through an OOMOL-connected Make account, including listing scenarios, reading account context, checking usage, activating or deactivating scenarios, and running a scenario once.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can affect live Make automations through activation, deactivation, and run-once actions.

Mitigation: Require explicit user confirmation of the target scenario, payload, and intended effect before running write or destructive actions.

Risk: The first-time setup guidance includes remote installer commands.

Mitigation: Prefer a verified installer or package manager path before executing remote installation scripts.

Risk: The skill depends on an OOMOL-connected Make account with server-side credential injection.

Mitigation: Install and use the skill only when the publisher and connected Make account are trusted, and review requested scopes or authorization errors before retrying.

## Reference(s):

- [Make homepage](https://www.make.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-make)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before constructing Make action payloads.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
