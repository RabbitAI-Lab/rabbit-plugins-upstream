## Description:

Linggen gives agents a local, cross-host memory layer plus optional browser and X session control through bundled local tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linggen](https://clawhub.ai/user/linggen)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and external users can use this skill to let compatible agents recall, add, update, delete, scan, and maintain durable personal or cross-project memory. It also provides guidance for optional browser and X session operations when the Linggen engine and browser bridge are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store selected personal facts and inject recalled facts into future agent prompts.

Mitigation: Review memory records regularly, avoid saving secrets or sensitive facts, and use the delete or forget commands when a record should no longer be used.

Risk: Scan and backfill flows can read local agent session history and convert selected details into durable memory.

Mitigation: Run scan/backfill only when that behavior is intended, review generated candidates before relying on them, and keep secret filtering enabled.

Risk: The install and update path downloads executable components, and evidence says supply-chain controls are incomplete for some components.

Mitigation: Review the bundled installers before first use, prefer the bundled no-remote-script path where available, verify checksums for supported binaries, and reassess before enabling engine or browser features.

Risk: Browser and X session operations may expose logged-in user context to an agent.

Mitigation: Enable browser features only for trusted sessions, respect visible permission prompts, and disable or avoid the browser bridge when logged-in page access is not needed.

## Reference(s):

- [Linggen homepage](https://linggen.dev)
- [ClawHub skill page](https://clawhub.ai/linggen/skills/linggen)
- [ClawHub publisher profile](https://clawhub.ai/user/linggen)
- [Routing rules](references/routing-rules.md)
- [Dream flow](references/dream-flow.md)
- [Condense flow](references/condense-flow.md)
- [Extractor prompt](references/extractor-prompt.md)
- [Shared memory design](doc/shared-memory-design.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-producing CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can cause local CLI calls that read or write memory records and may return JSON from the ling-mem CLI or MCP tools.]

## Skill Version(s):

2.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
