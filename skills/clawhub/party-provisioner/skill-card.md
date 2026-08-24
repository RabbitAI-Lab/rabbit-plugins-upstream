## Description:

Party Provisioner calculates purchasable quantities of drinks, ice, food, glassware, and supplies for parties and events from headcount, duration, guest mix, and weather.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External hosts and event planners use this skill to estimate event shopping lists for private parties, BBQs, weddings, holiday dinners, and similar gatherings. It is intended for planning quantities, not for commercial cash-bar operations, liquor-law compliance, or dietary menu design.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Alcohol quantity estimates can be mistaken for serving guidance or used without considering local laws and responsible-hosting duties.

Mitigation: Use the output for purchasing estimates only; follow local alcohol laws, provide food and water, arrange transportation options, and stop service before the event ends.

Risk: Incorrect guest counts, drinker mix, event duration, weather, or pour-size assumptions can make the shopping list inaccurate.

Mitigation: Review the inputs, apply the skill's sanity checks, and adjust for local serving habits before buying supplies.

## Reference(s):

- [Party Provisioning Reference](references/provisioning-math.md)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/party-provisioner)
- [Publisher profile](https://clawhub.ai/user/voronindenis5)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON calculator output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces rounded shopping-list quantities for drinks, food, ice, supplies, and optional alcohol budget estimates.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
