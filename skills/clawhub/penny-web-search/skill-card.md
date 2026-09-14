## Description:

Real-time web search and structured local-business/Places search using PennyAPI over x402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ayoubsalem-spec](https://clawhub.ai/user/ayoubsalem-spec)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agent users use this skill to route current web research, fact checking, verification, and structured local-business or Places searches through PennyAPI paid x402 endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route broad prompts into wallet-paid web or Places calls.

Mitigation: Use a low-balance x402 wallet with strict spend limits and require explicit approval before paid calls.

Risk: The examples recommend unpinned npx tooling.

Mitigation: Pin and verify the AgentCash and skills CLI versions before running commands from the skill.

Risk: Persistent AgentCash setup may make the paid service easier to invoke automatically.

Mitigation: Review any AgentCash configuration added by the skill and avoid broad automatic enablement.

## Reference(s):

- [PennyAPI homepage](https://pennyregwatch.com)
- [Penny Web Search endpoint](https://pennyregwatch.com/v1/search)
- [Penny Places endpoint](https://pennyregwatch.com/web/places)
- [ClawHub skill page](https://clawhub.ai/ayoubsalem-spec/skills/penny-web-search)
- [ClawHub publisher profile](https://clawhub.ai/user/ayoubsalem-spec)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with inline JSON request bodies and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to call paid x402 web search and Places endpoints with explicit query and result-count parameters.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
