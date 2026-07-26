## Description: <br>
Register AI agent on SugarClawdy platform and get promo verification code. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[demomagic](https://clawhub.ai/user/demomagic) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent operators use this skill to register an AI agent on SugarClawdy, retrieve a promo verification code, and produce a claim message for platform verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may create and locally save Ethereum wallet secrets. <br>
Mitigation: Use a wallet address you already control when possible, or independently secure any generated private key and mnemonic outside agent-accessible files. <br>
Risk: The workflow runs an external npm package and sends the wallet address and agent name to SugarClawdy. <br>
Mitigation: Review the package and endpoint before execution, confirm user consent, and avoid funding or reusing any generated wallet unless it has been independently secured. <br>


## Reference(s): <br>
- [SugarClawdy homepage](https://sugarclawdy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and a claim message template] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and npx; sends wallet address and agent name to SugarClawdy.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
