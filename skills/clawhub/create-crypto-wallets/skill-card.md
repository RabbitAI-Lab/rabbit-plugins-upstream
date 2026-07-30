## Description: <br>
Generate and manage Hierarchical Deterministic (HD) crypto wallets for 200+ cryptocurrencies, including Bitcoin and Ethereum, using the Python hdwallet library through either its CLI or Python API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[beocca](https://clawhub.ai/user/beocca) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to set up hdwallet, generate or derive HD crypto wallets, and produce compatible keys and addresses for supported cryptocurrencies. It is intended for controlled workflows where wallet secrets are handled as sensitive financial credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated mnemonics, seeds, and private keys can grant full control over associated funds if exposed. <br>
Mitigation: Use the skill offline or in a controlled environment, avoid shared logs and shell history, and store wallet secrets in an encrypted vault. <br>
Risk: Writing wallet material to plaintext files or tracked directories can leak financial credentials. <br>
Mitigation: Restrict file permissions, keep secret files out of version control, and prefer encrypted storage such as a local KeePass database. <br>
Risk: Using newly generated wallets with significant funds before validation can increase financial loss if derivation, storage, or handling is incorrect. <br>
Mitigation: Test with minimal funds and use dedicated wallets for automated or agentic workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/beocca/skills/create-crypto-wallets) <br>
- [python-hdwallet project](https://github.com/hdwallet-io/python-hdwallet) <br>
- [keepass-cli companion skill](https://clawhub.ai/beocca/skills/keepass-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code] <br>
**Output Format:** [Markdown with bash and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include mnemonics, seeds, private keys, extended keys, WIF values, public keys, addresses, JSON, or CSV; treat generated wallet material as secrets.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
