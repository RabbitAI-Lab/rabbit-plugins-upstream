## Description: <br>
Manage LNbits Lightning Wallet (Balance, Pay, Invoice). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[talvasconcelos](https://clawhub.ai/user/talvasconcelos) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to manage an LNbits Lightning wallet from an agent, including balance checks, invoice creation, invoice decoding, and payments after explicit confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles full LNbits wallet credentials. <br>
Mitigation: Use a dedicated low-balance wallet, keep LNBITS_API_KEY out of chat, and rotate any key that may have been exposed. <br>
Risk: The skill can trigger real Lightning payments. <br>
Mitigation: Decode the invoice, review amount and destination details, check balance, and require explicit yes/no confirmation before every payment. <br>
Risk: Using an untrusted LNbits endpoint can expose wallet activity or credentials. <br>
Mitigation: Set LNBITS_BASE_URL explicitly to a trusted HTTPS LNbits instance. <br>


## Reference(s): <br>
- [LNbits](https://lnbits.com) <br>
- [ClawHub skill page](https://clawhub.ai/talvasconcelos/skills/lnbits) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/talvasconcelos) <br>
- [LNbits demo server](https://demo.lnbits.com) <br>
- [LNbits default server used by CLI](https://legend.lnbits.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON CLI results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 plus LNBITS_API_KEY and LNBITS_BASE_URL environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
