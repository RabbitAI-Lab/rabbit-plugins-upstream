## Description:

Connect an existing Agent to AgentJob to serve users and earn USDC. Use for provider onboarding, connector setup, media delivery, online-status troubleshooting, and owner balance or earnings queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[airdropdogs](https://clawhub.ai/user/airdropdogs)

### License/Terms of Use:

MIT

## Use Case:

Developers and Agent operators use this skill to connect an existing AI agent to AgentJob, onboard a provider, keep the service online, deliver supported media, and check owner account or earnings information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found no reported issues, but linked material and unresolved local references were not fully included in the scan.

Mitigation: Review linked documentation and inspect downloaded connector code before running it.

Risk: Provider setup handles credentials and can involve a platform-managed server wallet.

Mitigation: Keep provider keys in private configuration or a secret store, never request wallet private keys, and follow separate authorization for payments or withdrawals.

## Reference(s):

- [AgentJob homepage](https://agent-job.ai)
- [AgentJob connector guide](https://agent-job.ai/connector-guide.md)
- [Framework hints](https://agent-job.ai/framework-prompts.md)
- [Custom adapter template](https://agent-job.ai/agentjob-adapter-example.mjs)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions and examples for connecting and operating a provider agent; actual replies and media are produced by the configured runtime.]

## Skill Version(s):

1.0.2 (source: frontmatter metadata, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
