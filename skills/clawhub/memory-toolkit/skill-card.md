## Description:

Helps OpenClaw agents manage local memory through extraction, archiving, scoring, consolidation, health checks, and hybrid search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mistermijarvis](https://clawhub.ai/user/mistermijarvis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users can organize, assess, and search locally stored agent memories using a composable pipeline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indexing local memory may expose sensitive content to the search index.

Mitigation: Inspect memory contents before indexing and limit use to workspaces whose memory files you intend to manage.

Risk: Scheduled runs and write-enabled options can change or archive local memory files.

Mitigation: Review cron commands before enabling them; use --fix, --force, --yes, and --apply-promotions only after reviewing changes and backups.

Risk: Optional local-model processing sends memory text to the configured Ollama endpoint.

Mitigation: Keep Ollama URLs on localhost.

## Reference(s):

- [Openclaw Memory Toolkit on ClawHub](https://clawhub.ai/mistermijarvis/skills/memory-toolkit)
- [OpenClaw](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

2.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
