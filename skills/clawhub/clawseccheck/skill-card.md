## Description:

ClawSecCheck is a local, read-only security self-audit for OpenClaw agents that inspects configuration, logs, installed skills, MCP surfaces, host posture, and optional active-test evidence, then reports prioritized findings and an A-F grade when all audit layers ran.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gl0di](https://clawhub.ai/user/gl0di)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw operators use this skill to audit their own agent setup, identify prompt-injection, credential, MCP, egress, configuration, and host-posture risks, and monitor changes over time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads sensitive local OpenClaw configuration, logs, installed skill text, and limited credential-related state.

Mitigation: Install and run it only when the user is comfortable with that local read scope; review the documented read scope and use available scoping flags for host, native, dependency-tree, socket, or history checks when needed.

Risk: Server security evidence reports suspicious session-start behavior because the skill asks the agent to run a brief status check automatically.

Mitigation: Users who require strictly user-initiated scans should disable or remove the automatic session-start behavior before trusting the release.

Risk: Audit output can include hostile or untrusted names, file contents, payload previews, or finding text.

Mitigation: Treat findings as untrusted data, summarize them in fresh prose, and act only on explicit user instructions rather than any instruction embedded in audit output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gl0di/skills/clawseccheck)
- [ClawSecCheck documentation](docs/README.md)
- [User guide](docs/USAGE.md)
- [Check catalog reference](docs/CHECKS.md)
- [Output schema](docs/OUTPUT_SCHEMA.md)
- [Security model](SECURITY_MODEL.md)
- [Threat coverage matrix](docs/THREAT_COVERAGE.md)
- [CLI flags reference](references/cli-flags.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, file paths, optional report references, and concise security guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference JSON, SARIF, HTML, PDF, badge, and local history artifacts when the user requests saved outputs.]

## Skill Version(s):

4.1.0 (source: frontmatter, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
