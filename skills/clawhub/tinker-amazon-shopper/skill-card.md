## Description:

Helps an agent search Amazon.es, decode product specs, ask narrowing questions, and rank buyable products by normalized value metrics such as EUR/GB, EUR/kg, or EUR/kg active ingredient.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill for iterative Amazon.es shopping decisions where the agent should compare available products, normalize value metrics, and recommend the best deal rather than return raw links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may capture and reuse Amazon session cookies for delivery or account-specific pricing.

Mitigation: Use anonymous mode by default, capture a session only when necessary, store it in a real OS keychain, and clear it with --logout when finished.

Risk: Shopping queries or product data can be sent to configured third-party services.

Mitigation: Review AMAZON_SHOPPER_* environment variables before use and leave optional third-party integrations disabled unless needed.

Risk: The security verdict flags fetch, relay, third-party, and external-instruction paths for review.

Mitigation: Review and scan the skill before installation, then run it with only the documented network, file, shell, and credential access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/tinker-amazon-shopper)
- [Publisher profile](https://clawhub.ai/user/globalcaos)
- [Amazon account session management](https://www.amazon.es/gp/css/account/info/view.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance, files]

**Output Format:** [JSON CLI results and concise Markdown recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stateful task IDs; optional page dumps, datasets, and charts when the user provides output paths.]

## Skill Version(s):

1.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
