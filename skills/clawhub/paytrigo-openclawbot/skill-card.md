## Description: <br>
Use when an OpenClawBot needs to create or verify PayTrigo payments on Base/USDC without webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paytrigo](https://clawhub.ai/user/paytrigo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and OpenClawBot operators use this skill to create PayTrigo invoices, route browser-based payment approval, run direct bot payment flows, and poll payment status on Base/USDC without webhooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill ships live PayTrigo API keys. <br>
Mitigation: Replace embedded keys with reviewed deployment credentials and do not rely on bundled keys for production use. <br>
Risk: The direct bot payment flow can spend wallet funds. <br>
Mitigation: Run only with sandbox or limited-balance wallets and require external approval or spend limits before allowing agent-initiated payment. <br>
Risk: Private keys or passphrases can be exposed through command-line arguments. <br>
Mitigation: Prefer encrypted wallet files and passphrase files with restricted permissions instead of passing secrets directly on the command line. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paytrigo/skills/paytrigo-openclawbot) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript CLI commands and JSON API payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes payment flow guidance for invoice creation, payment intent submission, local wallet setup, and polling.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
