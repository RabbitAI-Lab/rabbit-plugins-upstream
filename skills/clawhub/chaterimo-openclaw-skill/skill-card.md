## Description: <br>
AI Customer Service for Shopify & E-commerce - Query conversations, analyze chatbot performance, and manage your Chaterimo AI assistant. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[caebixus](https://clawhub.ai/user/caebixus) <br>

### License/Terms of Use: <br>


## Use Case: <br>
E-commerce operators and support teams use this skill to connect an agent to Chaterimo, list chatbots, browse customer service conversations, read redacted transcripts, and review chatbot performance signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can read Chaterimo chatbot and support conversation data available to the configured API key. <br>
Mitigation: Use a least-privilege read-only key where possible, revoke it when no longer needed, and install only where that data access is acceptable. <br>
Risk: Conversation text may still be sensitive even when the service advertises PII redaction. <br>
Mitigation: Avoid exposing returned conversation text in prompts, logs, or shared workspaces unless those locations are approved for sensitive support data. <br>
Risk: A leaked CHATERIMO_API_KEY could allow unauthorized access within the key's permissions. <br>
Mitigation: Store the key only in the CHATERIMO_API_KEY environment variable, avoid pasting it into prompts, and revoke or rotate it immediately if exposed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/caebixus/skills/chaterimo-openclaw-skill) <br>
- [Chaterimo Website](https://www.chaterimo.com) <br>
- [Chaterimo API Keys](https://www.chaterimo.com/account/api-keys/) <br>
- [How to connect Chaterimo with Shopify](https://www.chaterimo.com/en/blog/shopify-ai-customer-service/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown responses with chatbot lists, redacted conversation summaries, transcripts, and operational guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CHATERIMO_API_KEY. Conversation data is described as PII-redacted but should still be treated as sensitive.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
