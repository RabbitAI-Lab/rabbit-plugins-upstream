## Description:

Searches locally synchronized Temu category data by keyword to return matching Chinese names, English names, category IDs, and hierarchy metadata for product or store filtering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, developers, and agents use this skill to find Temu category IDs after category data has been synchronized into the LinkFox local category store. The returned IDs can support downstream product, shop, or category filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs remote authenticated API calls and depends on LinkFox API keys.

Mitigation: Install only when LinkFox is trusted for the task, keep API keys scoped to the intended environment, and avoid exposing session metadata or credentials in shared workspaces.

Risk: The included onboarding flow can request phone/SMS registration, generate API keys, and handle billing or payment orders.

Mitigation: Run onboarding and payment commands only with explicit user intent, verify plan and payment details before ordering, and avoid using the skill where billing actions must be tightly restricted.

Risk: Server evidence marks the release security verdict as suspicious because its behavior extends beyond category lookup.

Mitigation: Review the skill before installation and limit use to environments where remote authenticated requests, onboarding, and billing workflows are acceptable.

## Reference(s):

- [Temu category search API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [json, files, shell commands, configuration, guidance]

**Output Format:** [JSON responses and concise Markdown guidance; large responses may be saved as JSON files with summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a keyword and optional pagination parameters; authenticated calls use LINKFOX_AGENT_API_KEY or LINKFOXAGENT_API_KEY.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
