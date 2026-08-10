## Description:

Uses Amazon's storefront Alexa shopping assistant to answer a single natural-language shopping prompt, return a conversational recommendation, product groups with ASINs, and suggested follow-up questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and shopping assistants use this skill to ask Amazon Alexa conversational shopping questions, return product recommendations with ASINs and links, and continue with follow-up prompts by summarizing prior context into a new single-turn request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key and sends shopping prompts to a LinkFox gateway.

Mitigation: Install only when comfortable sharing those prompts with LinkFox, keep API keys in environment variables, and avoid including sensitive personal details in prompts.

Risk: Endpoint environment variables can redirect requests carrying credentials or prompts.

Mitigation: Verify LINKFOX_* endpoint variables point to legitimate LinkFox HTTPS domains before running the scripts.

Risk: Onboarding and billing helpers can create accounts, generate API keys, and create payment orders.

Mitigation: Require explicit user approval before login, API-key generation, plan selection, order creation, or payment-related commands.

Risk: The skill stores full API responses locally under LinkFox session data directories.

Mitigation: Review local saved response files for sensitive content and manage retention according to the user's workspace policy.

Risk: Alexa answers are live, single-turn, and not deterministic.

Mitigation: Treat recommendations as time-sensitive guidance, verify product details before purchasing, and summarize prior answers explicitly when asking follow-up questions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-alexa-search)
- [API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [LinkFox skills](https://skill.linkfox.com/)
- [LinkFox agent portal](https://agent.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report by default, or structured JSON when requested; scripts may also print shell guidance for authentication and billing setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each Alexa request accepts one prompt, can optionally anchor to a specific Amazon page URL, writes the full response to a local LinkFox session data file, and may use a 24-hour cache for repeated parameters.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
