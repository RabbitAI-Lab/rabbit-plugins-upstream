## Description: <br>
Guides agents through adding SettleMesh end-user billing to a deployed app so paid platform calls can be charged to the logged-in user's wallet with developer markup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[structureintelligence](https://clawhub.ai/user/structureintelligence) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and product engineers use this skill to add end-user-pays billing to deployed apps that make paid platform calls on behalf of logged-in users. It covers quoting charges, forwarding payer sessions, reading billed amounts, testing before real users, and handling billing errors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides payment-sensitive login and billing behavior that can affect SettleMesh accounts and wallets. <br>
Mitigation: Use it only for intended SettleMesh end-user billing, confirm the intended account before first use, and review charge or allowance prompts before execution. <br>
Risk: Misusing payer credentials can charge the wrong party or expose a test payer token. <br>
Mitigation: Treat API keys as runtime or developer credentials, not payer tokens; use logged-in user sessions for X-Settle-Payer and never ship self-test payer tokens as user credentials. <br>
Risk: Running the end-user-pays path outside the deployed backend can fail or fall back to developer-funded billing behavior. <br>
Mitigation: Exercise the money path from the deployed app server with the injected app runtime key, quote charges before capture, and read billed amounts from SettleMesh charge headers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/structureintelligence/skills/charge-my-users) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with inline shell commands and HTTP request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Payment-sensitive workflow requiring SettleMesh CLI access and SETTLE_API_KEY.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
