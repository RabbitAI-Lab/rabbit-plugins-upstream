## Description:

Install and use the public beta jd-drama CLI to operate JianDan short-drama projects, scripts, uploaded imports, assets, storyboards, videos, brands, and task diagnostics from Codex, Code, OpenClaw, or other agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyengine-ai](https://clawhub.ai/user/flyengine-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent install and run the jd-drama CLI for JianDan short-drama project discovery, script import, asset, storyboard, video, brand, and task diagnostics workflows while preserving dry-run and confirmation boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates against JianDan production short-drama data and real quotas.

Mitigation: Install and use it only when that access is intended, and review every dry-run output before approving confirmed commands.

Risk: Installing the beta npm package can pull a newer beta CLI than this skill release was authored against.

Mitigation: Check jd-drama --version, run release-check before live work, and reassess behavior when the beta package changes.

Risk: Confirmed write operations can modify projects, scripts, imports, storyboard segments, video generation, or brand associations.

Mitigation: Use named CLI commands, preview writes with --dry-run, and run the exact approved command with --confirm only after user approval.

Risk: Credentials or local configuration could be exposed if inspected directly.

Mitigation: Use browser authorization and avoid requesting passwords, tokens, or configuration file contents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyengine-ai/skills/jd-drama)
- [JianDan production API endpoint](https://jiandan.flyengine.cn/api)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON-oriented CLI usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses dry-run previews for writes and requires explicit user approval before confirmed production actions.]

## Skill Version(s):

1.0.0-beta.3 (source: server release evidence and artifact install instructions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
