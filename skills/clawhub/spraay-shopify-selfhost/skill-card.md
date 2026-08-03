## Description: <br>
Deploy and self-host the open-source Spraay Shopify app for batch USDC payouts on Base from a merchant's Shopify admin. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plagtech](https://clawhub.ai/user/plagtech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Shopify merchants, developers, and operators use this skill to deploy, configure, self-host, and troubleshoot a batch USDC payout app with Railway, Supabase, and a merchant-controlled wallet. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides deployment of a wallet-connected payout app and references a specific contract address. <br>
Mitigation: Confirm the repository and contract address are trusted before installation, as recommended by the server security guidance. <br>
Risk: Shopify, database, and app secrets are required during deployment. <br>
Mitigation: Keep secrets out of chats and commits, and store them only in the deployment platform's protected environment variables. <br>
Risk: A payout transaction moves real USDC and includes a disclosed 0.3% protocol fee. <br>
Mitigation: Run an initial test with a very small payout and review the fee before approving the wallet transaction. <br>


## Reference(s): <br>
- [Spraay Shopify source repository](https://github.com/plagtech/spraay-shopify) <br>
- [Spraay protocol docs](https://docs.spraay.app) <br>
- [ClawHub skill page](https://clawhub.ai/plagtech/skills/spraay-shopify-selfhost) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with step-by-step instructions, tables, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes deployment, environment variable, OAuth, database, wallet, custom domain, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
