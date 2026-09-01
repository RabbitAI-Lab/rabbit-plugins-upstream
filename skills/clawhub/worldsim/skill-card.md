## Description:

WorldSim is an agent skill for running persistent local story worlds, importing SillyTavern-compatible character cards, advancing interactive narrative state, and managing saves, loads, rollback, and state repair.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use WorldSim to let an assistant create, maintain, and narrate persistent roleplay worlds with autonomous characters, scene state, and long-running story continuity. The skill is intended for explicit world-simulation requests tied to a specific world, not for general chat or unrelated roleplay prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WorldSim persists local narrative, state, snapshot, and imported-character-derived files.

Mitigation: Install only when local story persistence is desired, use a dedicated worlds directory, and delete the relevant world directory to remove saved world records.

Risk: Roleplay content can contain secrets, sensitive personal information, or other private material that would be written to local world files.

Mitigation: Do not enter passwords, secrets, or sensitive personal information into stories or imported character material.

Risk: Imported SillyTavern-compatible character cards are untrusted input.

Mitigation: Review imported character cards for prompt-injection, sensitive, or copyright-sensitive content before accepting the import.

Risk: Reset, load, and deletion workflows can alter or remove saved world data.

Mitigation: Use the documented confirmation, rollback, and world-directory controls when managing saved data.

## Reference(s):

- [README.en.md](README.en.md)
- [WorldSim command reference](references/commands.md)
- [Write protocol](references/write_protocol.md)
- [Session recovery and world lifecycle](references/session_recovery.md)
- [SillyTavern character card import](references/import_cards.md)
- [Disclosure and confirmation protocol](references/disclosures.md)
- [Gate and audit protocol](references/gates.md)
- [Output quality evaluations](evals/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown narrative output, structured status text, local state files, YAML configuration, and shell commands for maintenance scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces persistent local world data under worlds/ or WORLDSIM_WORLDS_DIR, including narrative archives, state YAML, scene files, snapshots, and imported character-derived files.]

## Skill Version(s):

0.24.0 (source: ClawHub release evidence, released 2026-08-31)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
