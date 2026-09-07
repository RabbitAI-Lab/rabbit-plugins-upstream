## Description:

MC Server Plugin Security is a Minecraft server plugin security reference for investigating AuthMe and Bukkit/Paper-family plugin issues, checking jars, validating versions, and choosing safer upgrades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mowenqwq](https://clawhub.ai/user/mowenqwq)

### License/Terms of Use:

MIT

## Use Case:

Developers and Minecraft server administrators use this skill to investigate plugin vulnerability claims, harden Bukkit, Spigot, Paper, Leaf, Folia, Arclight, and NeoForge servers, inspect plugin jars, and plan safer upgrade or configuration changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is a security reference that may try to update its own SKILL.md from future conversations without clear maintainer review.

Mitigation: Install it read-only or require an explicit reviewed patch before any skill update is written.

Risk: The skill can guide agents toward downloading jars or changing production Minecraft server configuration based on investigation commands.

Mitigation: Treat commands as investigation aids, verify official sources before downloading jars, back up server and plugin data, and test changes before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mowenqwq/skills/mc-server-plugin-security)
- [Artifact README](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Code guidance]

**Output Format:** [Markdown with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include investigation steps, jar inspection commands, upgrade advice, configuration hardening guidance, and source-verification reminders.]

## Skill Version(s):

0.1.5 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
