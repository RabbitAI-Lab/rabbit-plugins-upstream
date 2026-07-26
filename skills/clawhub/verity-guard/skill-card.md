## Description: <br>
Independent fail-closed second opinion before acting: allow/review/block a risky action, fact-check a claim, screen text for prompt injection, or flag PII/secrets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[meloliva14](https://clawhub.ai/user/meloliva14) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use verity-guard to request an independent advisory verdict before irreversible actions, risky communications, fact claims, prompt-injection exposure, or outbound data sharing. It returns a second opinion and receipt data; it does not provide non-skippable enforcement by itself. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted action details, claims, untrusted text, logs, configs, or files are sent to a third-party verification service. <br>
Mitigation: Avoid sending secrets, private documents, or regulated data unless the service's handling of that content has been reviewed and accepted. <br>
Risk: VERITY_WALLET_KEY can authorize spending from the configured Base wallet. <br>
Mitigation: Use a dedicated low-balance wallet, do not reuse a main wallet, and keep the private key in the environment rather than command arguments. <br>
Risk: The skill is advisory and cannot force the agent to ask for a verdict before acting. <br>
Mitigation: Use a tool-call-path plugin or hook when non-skippable enforcement is required. <br>
Risk: Payment, timeout, network, or malformed-response failures mean no verdict exists. <br>
Mitigation: Treat these cases as fail-closed: stop, disclose that the check did not happen, and do not proceed as though it returned allow. <br>


## Reference(s): <br>
- [VerityLayer homepage](https://veritylayer.dev) <br>
- [Full check catalog](references/catalog.md) <br>
- [Enforcement boundary](references/enforcement.md) <br>
- [VerityLayer suite API](https://suite.veritylayer.dev) <br>
- [ClawHub skill page](https://clawhub.ai/meloliva14/skills/verity-guard) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands; the runtime script prints JSON verdicts, errors, wallet addresses, and receipt verification results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid checks may return signed verdict receipts; nonzero exits indicate payment, availability, verification, or usage failures.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
