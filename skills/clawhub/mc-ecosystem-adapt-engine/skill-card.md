## Description:

One-stop Minecraft mod ecosystem management skill for mod search, environment setup, Mixin conflict scanning, crash analysis and repair, translation, migration assessment, save sync, licensing, payments, an admin dashboard, and operational reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liang030214](https://clawhub.ai/user/liang030214)

### License/Terms of Use:

MIT-0

## Use Case:

External Minecraft mod players, modpack authors, and developers use this skill to inspect mod packages, find compatible mods, diagnose crashes, assess migrations, translate resources, synchronize saves, and manage commercial access workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Networked language geolocation, licensing, and payment behavior may contact services or enforce access flows the user did not expect.

Mitigation: Install only after reviewing the release behavior, avoid setting MC_SKILL_SERVER_URL unless the server is trusted, and prefer explicit language selection.

Risk: Save synchronization, restore, mod upgrade, and repacking features can change local Minecraft files.

Mitigation: Use these features only with trusted backups, trusted sync directories, and review generated changes before relying on them.

Risk: Local authorization state can affect usage limits, license status, and machine identification.

Mitigation: Inspect or reset data/auth_state.json before first use when evaluating or reinstalling the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liang030214/skills/mc-ecosystem-adapt-engine)
- [Publisher profile](https://clawhub.ai/user/liang030214)
- [Modrinth API endpoint](https://api.modrinth.com/v2)
- [CurseForge API endpoint](https://api.curseforge.com/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, shell command snippets, and file or configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce reports, fix suggestions, generated payment/admin pages, translated resources, backups, and mod or save file changes depending on the selected feature.]

## Skill Version(s):

1.0.4 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
