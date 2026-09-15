## Description:

AnyDB helps an agent read, create, update, list, and search AnyDB records through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate AnyDB data from an agent workflow through OOMOL's oo CLI, including record lookup, search, creation, and updates. It is intended for accounts that already have AnyDB connected through OOMOL, with first-time setup used only when authentication or connection commands fail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to execute remote installers directly in the shell without verification.

Mitigation: Prefer a signed or checksum-verified oo CLI installation method, and use the direct curl|bash or irm|iex installer only after independently trusting and verifying the installer source.

Risk: The skill can create or update AnyDB records through OOMOL-connected access after user confirmation.

Mitigation: Confirm the exact payload and intended effect before write actions, and fetch the live action schema before constructing the JSON payload.

Risk: Using the skill grants OOMOL-connected AnyDB access for agent-driven operations.

Mitigation: Use it only when the user is comfortable granting that access and keep credentials managed through OOMOL rather than exposing raw tokens.

## Reference(s):

- [ClawHub AnyDB Skill](https://clawhub.ai/oomol/skills/oo-anydb)
- [AnyDB Homepage](https://www.anydb.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: evidence metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
