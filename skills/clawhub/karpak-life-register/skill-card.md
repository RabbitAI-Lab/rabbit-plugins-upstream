## Description: <br>
Automate Karpak Life registration and SBT minting on the Karpak Living Map. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[karpak-developer](https://clawhub.ai/user/karpak-developer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to register a wallet on Karpak Life and mint a Soulbound Token on the Karpak Living Map. It guides the agent through parameter extraction, environment selection, wallet signing, profile setup, and mint status reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local browser bridge is unauthenticated and can expose wallet signing or transaction approval to tampering risk. <br>
Mitigation: Run only after review, keep untrusted websites closed during use, and prefer a version that adds a per-session bridge secret or stricter origin checks. <br>
Risk: The skill can submit a real BSC mainnet mint transaction that requires wallet approval and gas. <br>
Mitigation: Confirm the selected environment, contract, transaction details, and gas prompt in the wallet before approving. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/karpak-developer/skills/karpak-life-register) <br>
- [Karpak Life mainnet API](https://lifestyle-api.karpak.xyz) <br>
- [Karpak SBT mainnet](https://sbt.karpak.xyz) <br>
- [Karpak Life devnet API](https://devnet-lifestyle-api.karpak.xyz) <br>
- [Karpak SBT devnet](https://devnet.paratrix-sbt.pages.dev) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Text, API calls] <br>
**Output Format:** [Markdown with inline shell commands and terminal status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May open a local browser wallet bridge and report wallet address, account status, credential status, transaction hash, and explorer link.] <br>

## Skill Version(s): <br>
1.0.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
