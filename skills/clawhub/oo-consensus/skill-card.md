## Description:

Consensus (consensus.app). Use this skill for ANY Consensus request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Consensus for relevance-ranked academic papers through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may require installing the oo CLI and connecting a Consensus API key through OOMOL.

Mitigation: Review account, credential, and billing implications before setup; only run setup steps after a matching command failure.

Risk: Billing stops can prevent the connector from completing requests.

Mitigation: Check OOMOL account credit or billing status before retrying after HTTP 402 or OOMOL_INSUFFICIENT_CREDIT errors.

## Reference(s):

- [Consensus homepage](https://consensus.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-consensus)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
