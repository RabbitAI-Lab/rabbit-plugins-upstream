## Description:

Build a restaurant meal that fits the user's calorie, protein, sodium and allergen goals. Totals calories, protein, carbs, fat and sodium from the restaurant's published nutrition figures, flags any item with a missing figure instead of guessing, checks listed allergens, and suggests swaps that close the gap. Uses the BJ's Restaurant & Brewhouse menu as the worked example. Use when someone asks what to order to stay under a calorie or sodium limit, how many calories or how much protein a restaurant meal has, or which menu items avoid an allergen.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nbkdevs](https://clawhub.ai/user/nbkdevs)

### License/Terms of Use:

MIT-0

## Use Case:

External users planning a restaurant meal can total published nutrition values, compare them with calorie, protein, sodium, and allergen goals, and review possible swaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Menu allergen listings may not account for cross-contact in shared kitchens or fryers.

Mitigation: For a serious allergy, confirm requirements directly with the restaurant before ordering.

Risk: Missing or variable restaurant nutrition figures can make meal totals incomplete or inaccurate.

Mitigation: Use current restaurant-published figures, identify missing values instead of treating them as zero, and confirm serving details when needed.

## Reference(s):

- [BJ's menu and nutrition information](https://bjsmenus.com/)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown tables with nutrition totals, goal comparisons, and suggested swaps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Flags totals as incomplete when published figures are missing; provides meal arithmetic, not medical or dietetic advice.]

## Skill Version(s):

1.0.1 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
