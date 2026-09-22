## Description:

One-install associative memory graph for any OpenClaw workspace: migrate markdown memory into a graph, recall it by question, keep a task ledger, verify with a seeded battery, and revert cleanly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wstienstra](https://clawhub.ai/user/wstienstra)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use Engram to add local-first memory retrieval, task tracking, markdown migration, and workspace recall workflows to OpenClaw agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package can start a local daemon and add persistent scheduled jobs when optional rewire behavior is used.

Mitigation: Review the package before installing, run optional rewire only when persistent workspace changes are intended, and use the uninstall path to remove managed cron entries and stop the daemon.

Risk: The package can query local Ollama with memory content and expose credential metadata from Engram and workspace .env files.

Mitigation: Disable or remove credential and email heartbeat paths when agents should not handle secrets or mail credentials, and review local model routing before use.

Risk: The security scan verdict is suspicious because credential, email, and persistence behaviors are under-disclosed.

Mitigation: Treat installation as a review-gated action and scan the package before deployment.

## Reference(s):

- [Engram README](README.md)
- [Engram Skill Guide](SKILL.md)
- [How the numbers were measured](docs/measurement.md)
- [ClawHub skill page](https://clawhub.ai/wstienstra/skills/engram)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples, local configuration files, SQLite-backed memory data, and CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-first runtime; optional local embedding and reranking dependencies degrade to keyword-only behavior.]

## Skill Version(s):

1.2.0 (source: frontmatter and changelog, released 2026-09-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
