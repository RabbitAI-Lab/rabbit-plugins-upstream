## Description: <br>
AI agent toolkit for OK Computers, Ring Gates, and Net Protocol onchain storage on Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[potdealer](https://clawhub.ai/user/potdealer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to read OK Computer NFT state, build transaction payloads for onchain posts, DMs, pages, usernames, Ring Gates transmissions, and Net Protocol storage, and submit those transactions through a wallet or Bankr. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write operations can submit irreversible Base blockchain transactions. <br>
Mitigation: Use a limited wallet and API key, keep gas exposure small, and inspect every transaction and signing request before submission. <br>
Risk: The JSONP loader deliberately executes relay-delivered code outside the normal iframe sandbox boundary. <br>
Mitigation: Use the loader only with trusted relay content and avoid JSONP loading for untrusted pages or data. <br>
Risk: Onchain messages, pages, and stored data are public and permanent. <br>
Mitigation: Do not store private data onchain and review content before writing it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/potdealer/skills/ok-computers) <br>
- [Publisher profile](https://clawhub.ai/user/potdealer) <br>
- [OK Computers official site](https://okcomputers.xyz) <br>
- [Net Protocol](https://netprotocol.app) <br>
- [Ring Gates protocol specification](RING-GATES.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, json] <br>
**Output Format:** [Markdown guidance with JavaScript examples, shell commands, and Bankr-compatible transaction JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read operations use public RPC calls; write operations produce transaction payloads that require wallet ownership, signing, gas, and optional Bankr API credentials.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
