## Description:

Enables an agent to ask Amazon storefront Alexa shopping questions and return conversational shopping guidance, grouped product recommendations, ASINs, product links, and follow-up prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce agents use this skill for conversational Amazon product discovery when they need Alexa-style answers, curated product groups, ASINs, product URLs, and follow-up question ideas. It is suited to single-turn shopping prompts or page-anchored Amazon questions where the agent can summarize prior results before making another paid call.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopping prompts, Amazon URLs, session metadata, and optional feedback may be sent to LinkFox services.

Mitigation: Install only when that disclosure is acceptable, avoid including sensitive information in prompts or URLs, and review feedback before allowing it to be sent.

Risk: The skill includes onboarding, API-key handling, and billing/payment order flows.

Mitigation: Prefer self-service account setup, avoid sharing SMS codes unless intentionally onboarding through the agent, and confirm every plan, order, and payment step before execution.

Risk: The scripts persist full responses and session metadata under generated linkfox directories.

Mitigation: Review or clean generated linkfox directories when prompts, product results, screenshots, or session records may be sensitive.

Risk: Each answered call can consume LinkFox credits and repeated follow-up calls are independent paid requests.

Mitigation: Tell users before additional calls are made, use the built-in cache when appropriate, and avoid automatic retries or broad exploratory loops.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-alexa-search)
- [API Reference](references/api.md)
- [Onboarding and Billing Guide](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown report by default, or structured JSON when requested; scripts may also print shell-oriented setup guidance and write response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts one shopping prompt per call, optional Amazon page URL context, and optional output format selection; successful calls can consume LinkFox credits and store full responses locally.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
