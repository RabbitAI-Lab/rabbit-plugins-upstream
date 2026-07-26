## Description: <br>
ClawDaddy helps agents check domain availability, brainstorm available names, purchase domains with USDC or cards, and manage DNS, nameservers, transfers, and domain settings through an AI-friendly registrar API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gregm711](https://clawhub.ai/user/gregm711) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and AI agents use this skill to search for available domain names, compare prices, register domains, and administer DNS and registrar settings for purchased domains. Because it can spend money and change live domain infrastructure, use it where purchase and infrastructure changes can be explicitly reviewed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can let an agent spend money to register domains. <br>
Mitigation: Require explicit user approval after presenting the domain, quote, payment method, total cost, and payment flow before any purchase request is made. <br>
Risk: The skill can change live DNS records, nameservers, transfer state, locks, and autorenew settings, which can disrupt domain infrastructure. <br>
Mitigation: Require explicit approval before DNS deletion or overwrite, nameserver changes, transfer preparation, lock changes, or autorenew changes, and show the expected impact before applying the change. <br>
Risk: Management tokens can control purchased domains if exposed in ordinary chat or long-term memory. <br>
Mitigation: Keep management tokens in a dedicated secret store and avoid storing or repeating them in normal conversation history. <br>


## Reference(s): <br>
- [ClawDaddy ClawHub listing](https://clawhub.ai/gregm711/skills/clawdaddy) <br>
- [ClawDaddy application](https://clawdaddy.app) <br>
- [ClawDaddy agent documentation](https://clawdaddy.app/llms.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Configuration, Text] <br>
**Output Format:** [Markdown guidance with HTTP examples and JSON or TXT API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May initiate paid domain registration and live DNS, nameserver, transfer, lock, or autorenew changes through ClawDaddy endpoints.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
