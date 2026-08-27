## Description:

Yuandun (yotta-guardian) is a cross-agent guardrail that uses deterministic rules and optional intent verification to evaluate risky exec, write, edit, read, run, and shell tool calls before execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill as a pre-execution safety gate for high-risk commands, sensitive path writes, system configuration changes, and other tool calls that need deterministic allow, deny, or review decisions with audit traces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An external verifier can receive sensitive command text, paths, and content previews.

Mitigation: Keep the default local-only mode unless the configured verifier is trusted for the data it may receive.

Risk: A global install can copy the guardrail into multiple agent environments.

Mitigation: Use the global installer only when the same pre-check behavior is intended across those agents.

Risk: A guardrail verdict can be misunderstood as final authorization for a risky operation.

Mitigation: Treat deny and review outcomes as reasons to stop and report findings to the user; keep human authorization and compliance checks outside the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-guardian)
- [rules.md](references/rules.md)
- [policies.md](references/policies.md)
- [intent-verifier.md](references/intent-verifier.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-guardian)
- [Agent Skills standard](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [CLI text, JSON verdicts, Markdown reports, and JSONL audit logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verdicts include allow, deny, or review decisions with severity, matched rule IDs, reasons, exit codes, and optional verifier details.]

## Skill Version(s):

0.1.1 (source: release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
