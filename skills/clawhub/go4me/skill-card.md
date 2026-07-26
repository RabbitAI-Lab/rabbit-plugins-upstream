## Description: <br>
Send XCH to Twitter users via Go4Me address lookup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[koba42corp](https://clawhub.ai/user/koba42corp) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to look up Go4Me profiles for Twitter-style handles, resolve Chia XCH addresses, and prepare confirmed XCH sends or 1-mojo tips through sage-wallet. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit real Chia payments through a local wallet. <br>
Mitigation: Require explicit user confirmation before sending and make clear that submitted XCH transactions can move real funds. <br>
Risk: Recipient identity checks are too loose for payment-level risk. <br>
Mitigation: Use only normal Twitter-style handles and independently verify the resolved XCH address and Go4Me profile before confirming a transaction. <br>
Risk: The skill depends on sage-wallet for transaction execution. <br>
Mitigation: Install sage-wallet only from a trusted source and review the dependency before use. <br>


## Reference(s): <br>
- [Go4Me](https://go4.me/) <br>
- [Chia Network](https://www.chia.net/) <br>
- [Sage Wallet](https://github.com/xch-dev/sage) <br>
- [Go4Me Skill on ClawHub](https://clawhub.ai/koba42corp/skills/go4me) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown responses with JSON lookup data and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include transaction confirmation text, resolved profile fields, XCH address details, and error messages.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
