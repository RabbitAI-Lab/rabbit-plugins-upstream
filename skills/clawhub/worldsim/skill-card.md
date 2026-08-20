## Description:

WorldSim is a local persistent world-simulation, narrative-engine, and roleplay skill that can import SillyTavern character cards, advance interactive stories, and manage saves, loads, rollbacks, and state repair when the user explicitly asks to run a world or roleplay.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaowh](https://clawhub.ai/user/zhaowh)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use WorldSim to run persistent roleplay worlds, create or continue narrative simulations, import character cards, and preserve world state across sessions on local storage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes and retains story state, snapshots, and imported card originals under its worlds directory.

Mitigation: Install it only when local persistent world data is desired, and set WORLDSIM_WORLDS_DIR if world data should live outside the skill install.

Risk: Imported cards and story content may be retained locally.

Mitigation: Do not import cards or story material containing passwords, secrets, or sensitive personal information.

Risk: Reset, load, and delete operations can mutate or remove local world data.

Mitigation: Use the documented reset, load, and delete operations carefully and confirm destructive actions before execution.

## Reference(s):

- [WorldSim ClawHub Page](https://clawhub.ai/zhaowh/skills/worldsim)
- [README.en.md](README.en.md)
- [Commands Reference](references/commands.md)
- [Disclosure and Confirmation Reference](references/disclosures.md)
- [SillyTavern Card Import Reference](references/import_cards.md)
- [Write Protocol Reference](references/write_protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown narrative responses with local state files, YAML configuration, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes and retains world state, snapshots, imported card originals, and narrative archives under the configured worlds directory.]

## Skill Version(s):

0.11.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
