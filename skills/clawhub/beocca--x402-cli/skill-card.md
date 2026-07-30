## Description: <br>
A simple CLI that helps AI agents discover x402 services, make paywalled requests, and manage local EVM wallets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[beocca](https://clawhub.ai/user/beocca) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use x402-CLI to discover x402 services, manage local EVM wallets, and issue x402-paid HTTP requests from agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid x402 requests can spend real wallet funds to arbitrary endpoints without a confirmation gate or built-in spending limits. <br>
Mitigation: Review the destination URL, headers, and payload before each request, use a dedicated low-balance wallet, and treat command execution as explicit spend authorization. <br>
Risk: Wallet secrets can be exposed if plaintext wallet files or .env values are shared, committed, backed up, or reused across environments. <br>
Mitigation: Keep wallet files and .env values out of version control and shared storage, prefer encrypted local secret storage, and fund wallets only with the minimum needed balance. <br>
Risk: Request headers and payloads are transmitted to the third-party endpoint selected by the caller. <br>
Mitigation: Inspect outbound data before execution and avoid sending secrets or sensitive payloads unless the endpoint and payment are intentional. <br>


## Reference(s): <br>
- [x402-CLI ClawHub release](https://clawhub.ai/beocca/skills/x402-cli) <br>
- [AgNet OpenAPI](https://api.agnet.world/openapi.json) <br>
- [AgMsg OpenAPI](https://api.agmsg.world/openapi.json) <br>
- [KeePass CLI companion skill](https://clawhub.ai/beocca/skills/keepass-cli) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Single JSON object on stdout, with optional stderr security warnings and optional JSON files written by save commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Every command uses a stable ok/action or ok/error_code envelope; paid request warnings are informational stderr output.] <br>

## Skill Version(s): <br>
1.1.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
