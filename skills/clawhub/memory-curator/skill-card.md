## Description: <br>
Memory Curator distills verbose daily logs into compact, indexed digests for agent memory workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[77darius77](https://clawhub.ai/user/77darius77) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to compress Clawdbot memory logs into daily digest skeletons that preserve summaries, stats, key events, learnings, connections, open questions, and next-day priorities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local memory logs and generated digests may contain names, activity details, or other sensitive context. <br>
Mitigation: Review generated digests before committing or sharing them, and keep access limited to the intended workspace. <br>
Risk: An automated end-of-day cron job can repeatedly read memory logs and create digest files without manual initiation. <br>
Mitigation: Enable the cron schedule only deliberately and review the generated output as part of the memory workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/77darius77/skills/memory-curator) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown digest skeletons with shell command usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [When the helper script is run, it reads a dated memory log and writes a digest file under the local Clawdbot memory digests directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
