## Description: <br>
Answer Arknights operator, investment, lore, and stage-strategy questions while maintaining a local Doctor profile. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[morandot](https://clawhub.ai/user/morandot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Arknights players use this skill to get personalized operator investment, stage strategy, lore, terminology, comparison, and resource-planning guidance. It can tailor advice to a local Doctor profile when shell access and the profile file are available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill maintains a local Doctor profile that can include account details such as server, level, UID, resources, goals, and operator investment. <br>
Mitigation: Store only useful account facts, avoid saving UID unless needed, and review or delete ~/.config/arknights-skill/doctor-profile.json when the profile is no longer wanted. <br>
Risk: The quick start includes a manual curl-to-shell install command. <br>
Mitigation: Prefer the package-manager install paths, or inspect the installer before running it in a shell. <br>
Risk: Version-sensitive Arknights guidance can become stale when live lookup is unavailable. <br>
Mitigation: Use live web lookup for current banners, events, and meta questions; otherwise clearly caveat that conclusions are not based on current version data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/morandot/skills/arknights-skill) <br>
- [Server-resolved GitHub source](https://github.com/morandot/arknights-skill/tree/main/arknights-skill) <br>
- [Homepage](https://github.com/morandot/arknights-skill) <br>
- [Quick start guide](references/quickstart.md) <br>
- [Doctor profile schema](references/doctor-profile-schema.md) <br>
- [Answer templates](references/answer-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Natural-language guidance with Markdown structure, optional shell commands, and optional JSON snippets for profile updates.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and update a local Doctor profile JSON when client shell access is available; version-sensitive answers require live lookup or an explicit freshness caveat.] <br>

## Skill Version(s): <br>
1.4.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
