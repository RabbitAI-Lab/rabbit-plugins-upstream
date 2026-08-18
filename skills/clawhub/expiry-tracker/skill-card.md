## Description:

Expiry Tracker helps track perishable grocery items, expiry dates, use-this-today suggestions, and waste reports through a local command-line workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers can use this skill to maintain a local food inventory, identify items expiring soon, and generate simple waste reports. It is best suited for manual grocery and fridge tracking rather than automated food-safety decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates and updates a local ~/.expiry_tracker.json file containing food inventory and waste-history data.

Mitigation: Install and run it only when local storage of this household inventory data is acceptable.

Risk: Receipt-scanning and daily-alert wording may imply automation that the script does not provide.

Mitigation: Treat receipt entry as manual comma-separated input and use external reminders if daily checks are needed.

Risk: Shelf-life estimates and expiry suggestions are not food-safety determinations.

Mitigation: Check packaging, storage history, and signs of spoilage before eating anything near or past its date.

## Reference(s):

- [Expiry Tracker README](README.md)
- [Recipe Hints by Category](references/recipe-hints.md)
- [Default Shelf Life & Category Detection](references/shelf-life.md)
- [Server-resolved GitHub provenance](https://github.com/voronindenis5/expiry-tracker)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and local JSON file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local ~/.expiry_tracker.json file for inventory and waste-history data.]

## Skill Version(s):

0.1.1 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
