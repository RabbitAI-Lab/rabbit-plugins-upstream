## Description:

Analyzes Amazon keyword Share of Voice using Jungle Scout data, returning brand visibility, search volume, PPC bid estimates, and top ASIN click and conversion metrics across supported marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, marketplace analysts, and agents use this skill to assess brand share of voice and competitive visibility for a single Amazon keyword. It summarizes organic, sponsored, and combined brand presence, PPC bid context, and top ASIN click and conversion performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon keyword queries, session metadata, and API credentials are sent to LinkFox services.

Mitigation: Use the skill only for data you are comfortable sharing with LinkFox, obtain API keys from the official LinkFox site, and verify LINKFOX_* endpoint environment variables before running it.

Risk: Full API responses are retained locally in the workspace session data directory.

Mitigation: Run the skill from an appropriate workspace and remove stored LinkFox result files when they are no longer needed.

Risk: The included onboarding flow can generate tokens and create billing orders.

Mitigation: Use account setup and payment commands only when intentionally configuring or purchasing LinkFox credits, and review plan and payment details before proceeding.

Risk: Repeated calls consume LinkFox credits.

Mitigation: Confirm user intent before high-volume or repeated keyword lookups and rely on the built-in cache where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-keyword-share-of-voice)
- [API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables with JSON API results, local JSON data files, and occasional shell commands or environment-variable configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are written under a local linkfox session data directory; large responses are summarized unless inline output is requested, and duplicate requests may use a 24-hour cache.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
