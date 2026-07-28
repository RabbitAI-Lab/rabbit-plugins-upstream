## Description: <br>
KLYC-PMM is a memory-management skill for agents that records, syncs, distills, searches, encrypts, backs up, and recovers agent memory through the publisher's Yaochi service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sylncn](https://clawhub.ai/user/sylncn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use this skill to give OpenClaw, LightClaw, or Claude Code agents a persistent private memory workflow: write local journal and memory entries, sync selected files to the publisher service, search or recover memories, and run memory distillation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist agent memories to the publisher service and upload identity or instruction files for disaster recovery. <br>
Mitigation: Install only when that persistence model is intended; review watched file lists before enabling sync and avoid placing secrets in AGENTS.md, SOUL.md, IDENTITY.md, USER.md, or TOOLS.md. <br>
Risk: The skill includes long-running watch behavior, a daemon installer path, and an updater that downloads replacement shell code. <br>
Mitigation: Avoid curl-pipe-bash installation and unsigned updates; pin the reviewed release and inspect downloaded scripts before execution. <br>
Risk: Distillation can mutate backend memory data when not run in preview mode. <br>
Mitigation: Run distillation with --dry-run unless the operator is authorized to change the backend memory database. <br>


## Reference(s): <br>
- [PMM full architecture](artifact/references/pmm-full-architecture.md) <br>
- [ClawHub skill page](https://clawhub.ai/sylncn/skills/klyc-pmm) <br>
- [Publisher documentation](https://ai.syln.cn/?route=klyc-pmm) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands, local file updates, and JSON or status output from scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires jq and curl; normal operation may call the publisher API, persist local tokens, sync watched files, and write recovery or memory files.] <br>

## Skill Version(s): <br>
8.2.4 (source: server release, SKILL.md frontmatter, skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
