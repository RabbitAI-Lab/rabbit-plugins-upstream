## Description:

Read war.app (Warzone) game and player information from a shell or a signed-in browser tab; the workflows are read-only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

War.app and Warzone players can use the skill to check game state, map details, player statistics, and shared game records from an agent without the warapp-mcp server. Developers can also use its shell recipes for one-off or scripted, read-only lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends the configured war.app email and API token to the API destination.

Mitigation: Confirm that war.app is the intended destination and that you are comfortable using the account credentials for these read-only queries.

Risk: The security scan had medium confidence and only partial coverage of the skill components.

Mitigation: Review the partially inspected components before relying on the scan verdict.

## Reference(s):

- [war.app GameFeed API](https://war.app/API/GameFeed)
- [Get a war.app API token](https://war.app/API/GetAPIToken)
- [Fetchproxy CLI](https://www.npmjs.com/package/@fetchproxy/cli)
- [scout.mjs](artifact/references/scout.mjs)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON query results and concise text, with shell command examples in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookups; game visibility follows the authenticated player's fog of war.]

## Skill Version(s):

0.11.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
