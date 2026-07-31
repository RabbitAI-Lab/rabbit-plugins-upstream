## Description: <br>
Use when the user asks about Arknights operators, skills, masteries, modules, stages, lore, terms, or resource planning; do not use for other games, non-Arknights gacha advice, or real-time event schedules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[morandot](https://clawhub.ai/user/morandot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Arknights players use this skill to get personalized operator evaluations, skill and mastery priorities, resource planning help, stage strategies, terminology explanations, and spoiler-controlled lore summaries. The skill reads and updates a local Doctor profile when available so advice can reflect the user's account, roster, and goals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The quickstart includes a curl-to-bash shell installer. <br>
Mitigation: Prefer the documented package-manager install paths and review installer commands before running them. <br>
Risk: The skill creates and maintains a persistent local Doctor profile that can include account details such as server, level, UID, goals, resources, and operator status. <br>
Mitigation: Use ARKNIGHTS_MEMORY_DIR to choose an appropriate storage location, avoid saving UID or other account details on shared machines, and store only explicitly provided facts. <br>
Risk: Version-sensitive Arknights guidance can become stale or misleading when live lookup is unavailable. <br>
Mitigation: Check current sources for banners, events, and meta-dependent advice, or state clearly when an answer is not based on current version data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/morandot/skills/arknights-skill) <br>
- [Project Homepage](https://github.com/morandot/arknights-skill) <br>
- [Quick Start](references/quickstart.md) <br>
- [Answer Templates](references/answer-templates.md) <br>
- [Style Examples](references/examples.md) <br>
- [Doctor Profile Schema](references/doctor-profile-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and structured answer sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and update a local Doctor profile JSON file; version-sensitive answers require live lookup or an explicit freshness caveat.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release metadata; artifact frontmatter reports 1.5.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
