## Description: <br>
Manage a local CARP interface for ADILOS trust setup, queue polling, encrypted agent-to-agent requests, menus, results, answers, and secure commerce/escrow workflows through local or LAN CARP endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bitsanity](https://clawhub.ai/user/bitsanity) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to interact with a trusted local or LAN CARP interface for ADILOS setup, peer request handling, encrypted messaging, and commerce or escrow workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide calls to a CARP endpoint that may affect external agents, ACLs, payments, blockchain state, or escrow workflows. <br>
Mitigation: Keep IF_URL pointed only at a trusted local or LAN endpoint and require explicit user approval before ACL, payment, blockchain, escrow, or external counterparty actions. <br>
Risk: Generated CARP, ADILOS, or Ethereum key material and queue payloads can expose sensitive agent identity or transaction data. <br>
Mitigation: Protect generated key files, avoid printing or logging private keys, and treat IF_URL, cookies, request bodies, encrypted payloads, queue items, and payment references as sensitive. <br>
Risk: Queue polling and retries can consume inbound items or duplicate side effects if processing fails halfway through. <br>
Mitigation: Poll only when ready to process or record items, save raw responses and identifiers, and use idempotent retry handling with enough local state to prevent duplicate external actions. <br>
Risk: Trusting a discovered DID or peer key without verification can authorize the wrong counterparty. <br>
Mitigation: Require verified DID provenance and successful challenge/response before adding a DID to ACL or treating a peer as trusted. <br>


## Reference(s): <br>
- [CARP Skill Page](https://clawhub.ai/bitsanity/skills/carp) <br>
- [Publisher Profile](https://clawhub.ai/user/bitsanity) <br>
- [Reference Implementation](https://github.com/bitsanity/agent-crvp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline shell, Node.js, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and an IF_URL environment variable for the target CARP interface.] <br>

## Skill Version(s): <br>
1.0.3 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
