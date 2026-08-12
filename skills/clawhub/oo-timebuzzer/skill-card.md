## Description:

timeBuzzer (timebuzzer.com). Use this skill for ANY timeBuzzer request — reading, creating, updating, and deleting data. Whenever a task involves timeBuzzer, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate timeBuzzer through an OOMOL-connected account, including reading users, activities, layers, and tiles, and creating, updating, or deleting activities when confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create and update timeBuzzer activities through the connected OOMOL account.

Mitigation: Confirm the exact action, payload, and expected effect with the user before running write actions.

Risk: The delete activity action can permanently remove timeBuzzer data.

Mitigation: Require explicit user approval for the target activity ID before running destructive actions.

Risk: The first-time setup path uses a remote oo CLI installer.

Mitigation: Use the installer only when needed and only if the user trusts OOMOL's CLI distribution path.

Risk: Incorrect JSON payloads or stale assumptions about connector fields could affect the wrong data.

Mitigation: Fetch the live action schema with `oo connector schema` before constructing payloads and verify identifiers before execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-timebuzzer)
- [timeBuzzer homepage](https://timebuzzer.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL timeBuzzer connection](https://console.oomol.com/app-connections?provider=timebuzzer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI connector calls that return JSON responses from the connected timeBuzzer account.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
