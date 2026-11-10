## Description:

Deploy OpenClaw subagents on paid, confidential Agentgates virtual machines and manage them from the command line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentgates](https://clawhub.ai/user/agentgates)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to provision, manage, and message separate OpenClaw agents on Agentgates confidential virtual machines for research, data work, or other delegated tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Compute purchases and model calls spend from separate prepaid balances; the purchase cap is checked by the script and is not enforced as a server-side ceiling.

Mitigation: Start or renew machines only with owner authorization, set a conservative --max-usd, and keep both balances limited.

Risk: The x402 request body and local machine state can contain gateway or inference credentials.

Mitigation: Keep secret-bearing body output out of logs, protect the local state file, and do not share gateway tokens.

Risk: The provider's confidential-computing and data-retention guarantees were not independently validated in the release evidence.

Mitigation: Verify the machine's attestation and review the provider's data-retention terms before sending sensitive work.

## Reference(s):

- [Agentgates Compute API docs](https://api.agentgates.ai/api/compute/docs)
- [Agentgates Inference API docs](https://api.agentgates.ai/api/inference/docs)
- [Agentgates project repository](https://github.com/agentgates-ai/agentgates)
- [OpenClaw project repository](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Text]

**Output Format:** [Command-line instructions and API requests; agent responses as text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deployment request bodies can contain credentials; keep them out of logs and share only with the intended service.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
