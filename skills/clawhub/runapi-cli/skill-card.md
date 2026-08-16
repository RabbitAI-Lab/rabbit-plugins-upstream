## Description:

Install and use the RunAPI CLI for one-off artifacts and results from registered CLI-backed services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to install, inspect, authenticate, and run supported RunAPI CLI services for one-off tasks, JSON requests, task polling, pricing checks, callback listener workflows, and artifact handling. It directs production application integrations toward the RunAPI SDK instead of guessed CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented headless installer uses a pipe-to-shell pattern that can create supply-chain exposure if run without review.

Mitigation: Prefer the Homebrew install path when available, or download and inspect or verify the installer in a controlled environment before execution.

Risk: API keys, saved login credentials, listener secrets, uploaded files, and webhook listener operations can expose sensitive account or local-service access if handled casually.

Mitigation: Provide credentials only intentionally, avoid logging tokens and listener secrets, use stdin or environment auth for API keys, keep listener secrets out of project config, and verify uploads or listener operations before proceeding.

Risk: Installing this skill into other agent runtimes expands where its operational guidance can be invoked.

Mitigation: Review the skill and its security guidance before installing it into additional runtimes.

## Reference(s):

- [RunAPI model and CLI catalog](https://runapi.ai/models.md)
- [RunAPI models homepage](https://runapi.ai/models)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-cli)
- [RunAPI publisher profile](https://clawhub.ai/user/runapi-ai)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, text]

**Output Format:** [Markdown with shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to inspect installed CLI help before composing requests and to verify generated deliverables before completion.]

## Skill Version(s):

0.2.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
