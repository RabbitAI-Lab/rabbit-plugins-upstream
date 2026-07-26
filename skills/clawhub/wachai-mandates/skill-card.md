## Description: <br>
Create, sign, and verify WachAI Mandates, which are verifiable agent-to-agent agreements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[akshat-mishra101](https://clawhub.ai/user/akshat-mishra101) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External agents and developers use this skill to install and operate the WachAI CLI for creating, signing, verifying, storing, and exchanging mandate agreements between server and client roles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI uses wallet material for signing mandates, and the release security guidance treats wallet.json like a private key. <br>
Mitigation: Review the npm package or source before installing, avoid valuable production wallets unless the tool and environment are trusted, and protect wallet.json from shared or synced storage. <br>
Risk: Mandates and XMTP exchange can expose sensitive agreement terms through transport or local retention. <br>
Mitigation: Avoid secrets, regulated data, and confidential terms in mandates unless XMTP transport and local storage retention are acceptable for the use case. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/akshat-mishra101/skills/wachai-mandates) <br>
- [WachAI Terminal homepage](https://github.com/quillai-network/WachAI-Terminal) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides agents through CLI commands that may create local wallet and mandate files.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
