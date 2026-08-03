## Description: <br>
Generate and manage Hierarchical Deterministic (HD) crypto wallets for 200+ cryptocurrencies using the Python `hdwallet` library through its CLI or Python API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[beocca](https://clawhub.ai/user/beocca) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users use this skill to generate wallet entropy, mnemonics, seeds, keys, and addresses for supported cryptocurrencies, either interactively through the `hdwallet` CLI or programmatically through Python. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated mnemonics, seeds, and private keys can grant full control of wallet funds if exposed. <br>
Mitigation: Keep wallet material out of shell history, logs, git, and chat transcripts, and store real wallet secrets only in an encrypted vault. <br>
Risk: Agentic or automated workflows can unintentionally expose high-value wallet material. <br>
Mitigation: Use a fresh virtual environment and dedicated wallets with minimal funds when automation must handle wallet secrets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/beocca/skills/create-crypto-wallets) <br>
- [python-hdwallet project](https://github.com/hdwallet-io/python-hdwallet) <br>
- [keepass-cli companion skill](https://clawhub.ai/beocca/skills/keepass-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and Python code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide generation of wallet mnemonics, private keys, public keys, addresses, CSV, and JSON output through hdwallet.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
