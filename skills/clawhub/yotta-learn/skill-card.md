## Description:

元习 yotta-learn helps agents capture mistakes, corrections, missing capability requests, and useful insights as reusable project-local learning entries for later review and skill improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to turn command failures, user corrections, stale knowledge, and better practices into reusable .learnings entries. They can review, aggregate, promote, or extract those entries into longer-lived agent guidance and skill skeletons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hooks and promoted learning entries can make captured content persist into future agent instructions.

Mitigation: Review and narrow hook matchers before enabling them, and manually inspect each entry before promotion into AGENTS.md or CLAUDE.md.

Risk: Learning entries could capture secrets, credentials, private context, or overly broad source excerpts.

Mitigation: Keep .learnings entries free of secrets and use summaries or redacted snippets for sensitive incidents.

Risk: Optional memory sync depends on a yotta-memory executable found on PATH.

Mitigation: Use --remember only when the yotta-memory executable is trusted; otherwise rely on local .learnings records.

Risk: Installing into directories with attacker-controlled symlinks can redirect written skill files.

Mitigation: Install only into directories you control and inspect target paths before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-learn)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-learn)
- [Examples and field reference](references/examples.md)
- [FAQ](references/faq.md)
- [Hooks setup](references/hooks-setup.md)
- [Walkthroughs](references/walkthroughs.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown notes, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes project-local learning files; optional hooks and memory sync require explicit setup or flags.]

## Skill Version(s):

0.2.0 (source: frontmatter, package.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
