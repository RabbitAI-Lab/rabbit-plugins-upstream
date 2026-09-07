## Description:

Operate the live Tartarian.ai world collaboratively with a human through Tartarian WebMCP Site Tools for observation, navigation, inventory awareness, resource gathering, world interaction, targeting, and Command Bar actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tartarian-admin](https://clawhub.ai/user/tartarian-admin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent operating their authenticated Tartarian.ai browser session, including reading current world state, moving, selecting targets, interacting with resources or objects, and activating prepared commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide state-changing actions in a persistent Tartarian.ai game world, including movement, resource interaction, target activation, and Command Bar actions.

Mitigation: Use clear human instructions before state-changing actions and review structured Tartarian Site Tool results after each meaningful action.

Risk: The workflow relies on the human operator's authenticated browser session.

Mitigation: Do not paste session cookies, magic-link tokens, bearer tokens, or other private authentication material into chat.

Risk: Stale observations may lead to incorrect movement, target, inventory, or combat assumptions in a live world.

Mitigation: Observe current structured world state before meaningful actions, after failures or human actions, and whenever targets or inventory may have changed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tartarian-admin/skills/tartarian-webmcp-prototype)

## Skill Output:

**Output Type(s):** [guidance, text]

**Output Format:** [Markdown instructions with tool-use procedures and concise status reporting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is grounded in current Tartarian Site Tool results and the human operator's active browser session.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
