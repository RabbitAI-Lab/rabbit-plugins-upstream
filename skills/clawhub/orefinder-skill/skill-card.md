## Description:

Estimate where Minecraft ores are most likely to concentrate and the best mining Y level for a given seed, version, and player position, using the offline orefinder-estimate tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nazzal5448](https://clawhub.ai/user/nazzal5448)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to estimate likely Minecraft ore concentration areas and recommended mining Y levels from a version, ore, biome, radius, and player position. The skill supports planning mining routes and reminds users that outputs are statistical estimates rather than exact seed-based block locations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run the orefinder-estimate package through npx or pip.

Mitigation: Review package installation and execution in the target environment before enabling the skill.

Risk: The skill can point users to orefinder.io for exact coordinates.

Mitigation: Confirm that external site usage is acceptable for the deployment context before directing users there.

Risk: The skill trigger is somewhat broad around Minecraft mining and ore-related queries.

Mitigation: Scope activation to Minecraft ore-finding requests and check that the response remains relevant to the user's requested game edition, version, ore, and location.

Risk: The estimates do not simulate world generation, ore veins, structures, or exact block coordinates.

Mitigation: Present outputs as statistical estimates and tell users when exact seed-based lookup is required.

## Reference(s):

- [Minecraft Ore Finder](https://orefinder.io)
- [ClawHub skill page](https://clawhub.ai/nazzal5448/skills/orefinder-skill)
- [ClawHub publisher profile](https://clawhub.ai/user/nazzal5448)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides offline statistical estimates, ranked candidate areas, probability percentages, and reminders to use orefinder.io for exact seed-based locations.]

## Skill Version(s):

0.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
