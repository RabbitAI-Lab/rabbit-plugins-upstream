## Description:

Read Warzone game state, maps, settings, player activity, and opponent statistics from a shell using the war.app API and a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Players and developers can use the skill to inspect a Warzone game's state, map, settings, and waiting players, or review another player's public game statistics. It provides read-only shell workflows for one-off queries and scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan is partial: only 1 of 3 components was fully inspected, and two had analysis limitations.

Mitigation: Review the scan limitations and inspect the remaining components before installation, as the report does not establish that uninspected portions are safe.

Risk: The shell helper uses a war.app API token from the environment or a local configuration file.

Mitigation: Keep the token private, do not print or commit the configuration file, and rotate the token if it is exposed.

## Reference(s):

- [war.app](https://war.app)
- [Fetchproxy CLI](https://www.npmjs.com/package/@fetchproxy/cli)
- [scout.mjs](references/scout.mjs)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Guidance]

**Output Format:** [JSON game and player data, with formatted text and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only query workflows; results are limited to the signed-in player's access.]

## Skill Version(s):

0.14.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
