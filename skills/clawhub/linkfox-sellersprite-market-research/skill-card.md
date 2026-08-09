## Description:

This skill helps agents screen and rank Amazon category markets with SellerSprite data across sales, revenue, concentration, seller structure, new-product share, price, rating, and margin filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace researchers, ecommerce operators, and agents acting for them use this skill to identify Amazon category markets for deeper product research and compare market size, competition, seller mix, and new-product opportunity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can contact LinkFox/SellerSprite services and consume paid credits.

Mitigation: Confirm paid API use before calls, avoid automatic retries or parameter probing, and review the expected credit cost before continuing.

Risk: The onboarding flow can guide users through account login, SMS-code entry, API-key generation, and payment order creation.

Mitigation: Prefer a manually obtained least-privilege API key, enter phone or SMS codes only when the publisher and runtime are trusted, and review any payment order before scanning a QR code.

Risk: Full market-research responses and cache files may be stored locally.

Mitigation: Run the skill from an appropriate workspace, avoid sensitive research inputs if local retention is unwanted, and clear the linkfox output and cache directories when results should not be retained.

Risk: ClawHub security evidence marks this release suspicious because it combines market research, account setup, billing, feedback reporting, and persistent storage.

Mitigation: Review the skill and its requested actions before installation or execution, especially in commercial environments.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/linkfox-ai/skills/linkfox-sellersprite-market-research)
- [SellerSprite market research API reference](references/api.md)
- [LinkFox authentication and billing onboarding guide](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API parameters, command snippets, summarized console output, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are written under a local linkfox session directory; large responses are summarized unless inline output is requested; repeated calls may use a 24-hour local cache.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
