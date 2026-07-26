## Description: <br>
A self-custody Kaspa blockchain CLI wallet for sending KAS, checking balances, generating payment URIs, estimating fees, and returning JSON output for automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manyfestation](https://clawhub.ai/user/manyfestation) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and automation agents use this skill to manage a self-custody Kaspa wallet from the command line, including balance checks, fee estimates, payment URIs, mnemonic generation, and KAS transfers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet credentials or generated mnemonics can be exposed if they are copied into transcripts, logs, or shared environments. <br>
Mitigation: Keep private keys and mnemonics out of transcripts and logs, and use a low-value or test wallet when evaluating the skill. <br>
Risk: The send command can transfer funds without clear built-in safeguards. <br>
Mitigation: Manually verify the recipient, amount, fee, and network before any send operation. <br>
Risk: The installer may use remote pip bootstrap behavior. <br>
Mitigation: Review the installer and dependencies first, or avoid the installer unless you accept that behavior. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/manyfestation/skills/kaspa) <br>
- [Kaspa Docs](https://docs.kaspa.org/) <br>
- [Kaspa Explorer](https://explorer.kaspa.org/) <br>
- [kaspa-py SDK](https://github.com/aspect-build/kaspa-py) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with bash examples and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses KASPA_PRIVATE_KEY or KASPA_MNEMONIC environment variables and supports mainnet, testnet-10, and custom RPC endpoints.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
