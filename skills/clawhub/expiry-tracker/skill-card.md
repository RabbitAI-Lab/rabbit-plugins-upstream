## Description:

Track food expiry dates from grocery receipts, get daily alerts before food goes bad, receive use-this-today suggestions, and reduce food waste.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and household-focused agents use this skill to maintain a local inventory of perishable groceries, identify items expiring soon, and produce waste reports that support meal planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores grocery inventory and waste history locally in ~/.expiry_tracker.json.

Mitigation: Review, protect, or delete that local file on shared or managed computers when the data should not persist.

Risk: Expiry and recipe guidance may be too general for a specific item or storage condition.

Mitigation: Use the tracker as a reminder aid and apply normal food-safety checks before consuming or discarding food.

## Reference(s):

- [Server-resolved GitHub repository](https://github.com/voronindenis5/expiry-tracker)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/expiry-tracker)
- [Default Shelf Life & Category Detection](references/shelf-life.md)
- [Recipe Hints by Category](references/recipe-hints.md)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance, configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create or update a local JSON inventory at ~/.expiry_tracker.json.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
