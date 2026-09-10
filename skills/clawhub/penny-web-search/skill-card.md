## Description:

Real-time web search for current information using PennyAPI over x402, including fresh web results, recent facts, current events, research, verification, fact checking, and up-to-date information when the answer may have changed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ayoubsalem-spec](https://clawhub.ai/user/ayoubsalem-spec)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agent users use this skill to route current-information questions to PennyAPI for paid public-web search, source discovery, and verification when model knowledge may be stale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause paid external web-search calls through a wallet-capable x402 client.

Mitigation: Use a low-balance wallet with spending limits and require confirmation before paid calls.

Risk: Broad trigger language may route more tasks to paid live web lookup than intended.

Mitigation: Enable the skill only for explicit live-web requests and tighten agent routing rules.

Risk: Command examples use unpinned AgentCash package versions.

Mitigation: Prefer pinned AgentCash and skill versions in production environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ayoubsalem-spec/skills/penny-web-search)
- [PennyAPI homepage](https://pennyregwatch.com)
- [PennyAPI paid search endpoint](https://pennyregwatch.com/v1/search)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and source URLs when returned by PennyAPI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid x402 web-search calls should preserve returned source URLs and distinguish PennyAPI results from agent inference.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
