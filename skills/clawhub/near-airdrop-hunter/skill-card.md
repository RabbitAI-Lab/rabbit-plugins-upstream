## Description: <br>
Discover NEAR airdrops, check eligibility, claim rewards, and track claimed airdrops across multiple platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaiss](https://clawhub.ai/user/shaiss) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to list known NEAR ecosystem airdrop opportunities, check where eligibility can be verified, open claim destinations, and keep local tracking notes by account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The claim flow can be mistaken for an on-chain or protocol-level claim. <br>
Mitigation: Treat claim output as a pointer to a third-party URL and verify completion independently in the wallet or protocol interface. <br>
Risk: Airdrop links can expose users to phishing or unsafe wallet prompts. <br>
Mitigation: Verify each URL and review every wallet signature or approval before connecting a wallet or signing. <br>
Risk: Local tracking data can be confused with authoritative reward status. <br>
Mitigation: Use ~/.near-airdrop/tracking.json only as a local note and confirm eligibility or rewards with the relevant protocol. <br>


## Reference(s): <br>
- [NEAR Ecosystem](https://near.org/ecosystem/) <br>
- [NEAR Airdrops](https://near.org/airdrops/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance, configuration] <br>
**Output Format:** [Terminal text and command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local tracking data to ~/.near-airdrop/tracking.json when claim tracking is used.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
