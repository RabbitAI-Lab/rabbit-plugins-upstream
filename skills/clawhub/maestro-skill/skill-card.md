## Description: <br>
Query Maestro APIs over HTTP using the SIWX + JWT + x402 credit purchase flow. Resolve the exact endpoint from docs.gomaestro.org before requesting or paying. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vardominator](https://clawhub.ai/user/vardominator) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to make direct HTTP calls to Maestro endpoints, resolve endpoint details from Maestro documentation, handle SIWX authentication, and purchase x402 API credits only when required by a live 402 response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may request wallet signing or raw private-key access. <br>
Mitigation: Use a dedicated low-balance wallet or constrained signer and do not expose a primary wallet or unrestricted private key. <br>
Risk: The skill can spend USDC to purchase Maestro API credits. <br>
Mitigation: Require approval for every paid request and manually verify the endpoint, network, payee, asset, and exact amount before signing. <br>
Risk: Payment terms can change between requests. <br>
Mitigation: Use only the latest live 402 response for supported chains, payment recipient, asset, and price limits. <br>


## Reference(s): <br>
- [SIWX + x402 Reference](references/siwx-x402.md) <br>
- [Maestro documentation index](https://docs.gomaestro.org/llms.txt) <br>
- [ClawHub skill page](https://clawhub.ai/vardominator/skills/maestro-skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, text] <br>
**Output Format:** [Markdown with HTTP request steps, header details, and command or code snippets as needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include returned API data, selected network, payment amount, signer address, remaining credits, and payment metadata when relevant.] <br>

## Skill Version(s): <br>
0.2.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
