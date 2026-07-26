## Description: <br>
Send real physical postcards anywhere in the world, paid with x402 USDC on Base, Stripe, or manual USDC transfer, without signup or an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cktc](https://clawhub.ai/user/cktc) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use Moltpost to create, pay for, and track real-world postcard mailings through API calls. Agents can generate postcard content, collect recipient details, request approval, and present payment or wallet-signature steps to the owner. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill supports paid real-world postcard mailing, which can create irreversible physical mail and payment actions. <br>
Mitigation: Require explicit owner approval before each postcard API call and before each wallet signature, USDC transfer, or Stripe payment step. <br>
Risk: Recipient addresses and postcard content are sent to Moltpost, and postcards are physically visible in transit. <br>
Mitigation: Send only owner-provided addresses, avoid sensitive content, and set postcards private when appropriate. <br>
Risk: The heartbeat routine fetches mutable remote instructions. <br>
Mitigation: Disable or tightly constrain heartbeat use unless the fetched instructions can be inspected and trusted before use. <br>


## Reference(s): <br>
- [Moltpost ClawHub Skill Page](https://clawhub.ai/cktc/skills/moltpost) <br>
- [Moltpost Homepage](https://moltpost.io) <br>
- [Moltpost API Base](https://api.moltpost.io/v1) <br>
- [Moltpost Skill File](https://moltpost.io/skill.md) <br>
- [Moltpost Heartbeat Instructions](https://moltpost.io/heartbeat.md) <br>
- [6x4 Front Design Guideline](https://moltpost.io/guidelines/6x4-front.svg) <br>
- [6x4 Back Design Guideline](https://moltpost.io/guidelines/6x4-back.svg) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON payloads, curl examples, HTML snippets, and API workflow instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May lead an agent to prepare API requests, postcard HTML, payment links, wallet-signature prompts, status checks, and owner-facing confirmation text.] <br>

## Skill Version(s): <br>
1.3.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
