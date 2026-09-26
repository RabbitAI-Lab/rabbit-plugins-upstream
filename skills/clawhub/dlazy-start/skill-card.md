## Description:

Quickstart guidance for AI orchestrators driving @dlazy/cli, covering install, authentication, capability discovery, cloud and local tool invocation, async polling, and common failure recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this skill to operate @dlazy/cli from an orchestrator such as Claude Code, Cursor, Codex, or Copilot. It helps agents install and authenticate the CLI, discover available tools, invoke cloud and local commands, poll long-running tasks, and recover from common CLI failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on @dlazy/cli, which can call paid cloud tools and save generated outputs.

Mitigation: Install only from trusted package sources, use dry-run or tool description commands before paid calls, and announce provider, model, and cost before invoking generation tools.

Risk: API keys may be supplied through command-line flags, config files, or environment variables.

Mitigation: Prefer device-code login or protected environment injection, avoid inline API keys when possible, and protect ~/.dlazy/config.json.

Risk: Browser-cookie based downloads may use local browser session data.

Mitigation: Use cookies_from_browser only when the user explicitly accepts that local browser session data may be accessed for the download workflow.

Risk: Optional local runtimes such as Remotion or yt-dlp may be installed by CLI doctor commands.

Mitigation: Run doctor install commands only in environments where npm-installed local runtimes are allowed and review proxy or runtime requirements first.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell command examples and CLI usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes install, authentication, discovery, invocation, polling, dry-run, and troubleshooting guidance for @dlazy/cli.]

## Skill Version(s):

2.0.21 (source: server release metadata; artifact frontmatter says 2.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
