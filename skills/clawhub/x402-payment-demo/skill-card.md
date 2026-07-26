## Description: <br>
Demo of x402 payment protocol by fetching a protected image. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[hades-ye](https://clawhub.ai/user/hades-ye) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to demonstrate an x402 payment flow on TRON by requesting a protected image, handling the payment challenge, signing the required permit, retrieving the image, and deleting the temporary file after display. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs the agent to automatically perform blockchain payment and signing steps without explicit spending limits. <br>
Mitigation: Use Nile or Shasta testnets by default, and require the agent to show the exact network, recipient, asset, amount, and signature request before any payment or permit signing. <br>
Risk: Mainnet execution can involve real-funds behavior. <br>
Mitigation: Use mainnet only when the user deliberately requests it and confirms the payment details before signing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hades-ye/skills/x402-payment-demo) <br>
- [TRON Nile protected demo endpoint](https://x402-tron-demo.aibank.io/protected-nile) <br>
- [TRON Shasta protected demo endpoint](https://x402-tron-demo.aibank.io/protected-shasta) <br>
- [TRON Mainnet protected demo endpoint](https://x402-tron-demo.aibank.io/protected-mainnet) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Files] <br>
**Output Format:** [Markdown guidance with URLs, payment-flow steps, and temporary image-file handling] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill fetches and displays a protected image, then deletes the local temporary file after display.] <br>

## Skill Version(s): <br>
1.0.2 (source: release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
