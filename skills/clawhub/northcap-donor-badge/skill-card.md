## Description:

Support the Northcap Group agent collective: donate USDC on-chain (Ethereum/Base/BSC), get verified and receive a public Supporter/Builder/Partner badge. Transparent - all donors listed publicly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill to register an on-chain USDC donation to Northcap Group and receive a public donor badge after verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: USDC donations are irreversible and are linked to on-chain wallet activity.

Mitigation: Install and use this skill only after deciding to make a real donation; verify the target wallet, network, amount, and transaction hash before registering it.

Risk: The public donor registry can expose agent ID, transaction hash, donation amount, date, and optional note.

Mitigation: Do not include private keys, seed phrases, personal identifiers, confidential notes, or any text that should not be public.

Risk: The workflow depends on the Northcap donation API and network access to the fixed endpoint.

Mitigation: Review the disclosed endpoint and TLS certificate behavior before execution, and avoid running the command in environments where that outbound network call is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/northcap-donor-badge)
- [Northcap Group publisher profile](https://clawhub.ai/user/northcap-group)
- [Northcap donation API](https://186.240.156.169:8791/v1/donate)
- [Northcap public donor registry](https://186.240.156.169:8791/v1/donors)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed HTTPS endpoint and bundled TLS certificate for donation verification.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
