## Description:

PyPlanet plugin development, GitHub installer, and Clan Spirits plugin.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomekdot](https://clawhub.ai/user/tomekdot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and server operators use this skill to create PyPlanet plugins, install plugins from GitHub or ZIP sources, and configure clan scoring workflows for ManiaPlanet servers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing, updating, or removing live PyPlanet plugins from arbitrary GitHub repositories or ZIP URLs can introduce untrusted code or disrupt server state.

Mitigation: Restrict installer commands to trusted admins, use vetted and preferably pinned repositories, avoid arbitrary ZIP URLs, and back up plugin folders before install, update, or remove operations.

Risk: Clan scoring reset and recalculation commands can affect competition data.

Mitigation: Limit reset and recalculation commands to authorized operators and back up competition data before reset or update operations.

## Reference(s):

- [Server-resolved GitHub import](https://github.com/tomekdot/hermes-skills/tree/main/skills/software-development/pyplanet)
- [ClawHub PyPlanet skill page](https://clawhub.ai/tomekdot/skills/pyplanet)
- [Original Skill Sources](references/original-skills.md)
- [PyPlanet Hello World source](https://github.com/tomekdot/pyplanet-hello-world)
- [PyPlanet GitHub Installer source](https://github.com/tomekdot/pyplanet-github-installer)
- [PyPlanet Clan Spirits source](https://github.com/tomekdot/pyplanet-clanspirits)
- [Original PyPlanet Clan Wars source](https://github.com/tomekdot/pyplanet-clanwars)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with Python code snippets, shell-style chat commands, tables, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes PyPlanet plugin requirements and administrative command guidance.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter lists 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
