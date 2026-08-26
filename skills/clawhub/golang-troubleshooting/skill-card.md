## Description:

Troubleshoots Go programs systematically by guiding agents through root cause investigation for bugs, crashes, deadlocks, performance symptoms, tests, pprof, Delve, race detection, GODEBUG tracing, and production debugging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to troubleshoot Go services and libraries by reproducing failures, gathering diagnostic evidence, isolating root causes, and verifying fixes. It is suited for single-issue debugging and broader Go codebase bug hunts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production debugging examples may expose credentials, cookies, tokens, request bodies, or PII if copied without redaction.

Mitigation: Redact sensitive data before logging, sharing, or storing diagnostics, and review any HTTP dump or environment-variable command before use.

Risk: pprof endpoints can expose sensitive runtime information or create service load if made publicly reachable.

Mitigation: Keep pprof authenticated, isolated to trusted networks, and enabled only when needed.

Risk: The skill can guide an agent to inspect and modify Go code or run diagnostic tools.

Mitigation: Review proposed code changes and shell commands before applying them in production repositories.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/samber/skills/golang-troubleshooting)
- [Homepage](https://github.com/samber/cc-skills-golang)
- [General Debugging Methodology](references/methodology.md)
- [Common Go Bugs](references/common-go-bugs.md)
- [Test-Driven Debugging](references/testing-debug.md)
- [Concurrency Debugging](references/concurrency-debug.md)
- [Performance Troubleshooting](references/performance-debug.md)
- [pprof Reference](references/pprof.md)
- [Diagnostic Tools](references/diagnostic-tools.md)
- [Production Debugging](references/production-debug.md)
- [Compilation Issues](references/compilation.md)
- [Code Review Red Flags](references/code-review-flags.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include troubleshooting plans, diagnostic commands, test cases, code edits, and review findings.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
