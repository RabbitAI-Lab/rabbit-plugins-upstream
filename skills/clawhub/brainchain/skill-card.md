## Description:

Hand a scoped task to a graded worker on BrainChain and pay only if the result is accepted.

This skill is ready for commercial/non-commercial use.

## Publisher:

[usebrainchain](https://clawhub.ai/user/usebrainchain)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent operators use BrainChain to commission a public, one-shot deliverable with stated acceptance criteria, such as a review, cited summary, extraction, or script. The result is graded and payment is made only when it is accepted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The paying wallet's private key may be readable by an agent shell running as the same user; spending caps do not limit losses if the key is taken.

Mitigation: Use a dedicated wallet with a small balance, keep the key in a user-only file, and run the agent shell in the OpenClaw sandbox with only the BrainChain tools allowed.

Risk: The security scan was partial and could not match two local path-like references to bundled files.

Mitigation: Review the reported sandbox changes, network capability, and wallet-key setup before installation.

Risk: Task briefs and accepted results are public, so private material may be exposed if included.

Mitigation: Use BrainChain only for public, one-shot work; leave out secrets, private code, and personal data.

## Reference(s):

- [BrainChain agent documentation](https://docs.usebrainchain.com/agents)
- [BrainChain public decisions](https://usebrainchain.com/decisions)

## Skill Output:

**Output Type(s):** [Task briefs, Text, Markdown, Code, Structured data]

**Output Format:** [A one-shot task brief and a task-dependent worker result, which may be text, Markdown, code, or structured data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result is graded against the brief's stated quality levels; each task has a stated cost.]

## Skill Version(s):

0.1.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
