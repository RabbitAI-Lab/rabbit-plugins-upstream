## Description:

Debug Node.js with node inspect, --inspect, breakpoints, CDP, heap, and CPU profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to debug Node.js applications, tests, child processes, startup races, memory growth, and CPU hot paths with the Node inspector, Chrome DevTools Protocol, heap snapshots, and CPU profiles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional npm tooling can execute third-party package code.

Mitigation: Pin the package version or use an existing locked dependency when possible.

Risk: Exposed Node.js inspector ports can permit unsafe debugging access.

Mitigation: Keep inspector ports bound to localhost unless operating on an isolated network.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/node-inspect-debugger)
- [Publisher profile](https://clawhub.ai/user/azizbrownint)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell commands and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js; optional Chrome DevTools Protocol tooling should be installed cautiously and pinned when possible.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
