## Description: <br>
Develop, test, or integrate the OpenClaw Tally Node.js library for task-level cost, complexity, and efficiency analytics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jonathanjing](https://clawhub.ai/user/jonathanjing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to work on or explicitly integrate OpenClaw Tally, a local Node.js library for detecting task boundaries, recording task cost metadata in SQLite, and computing task efficiency analytics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A runtime hook integration can observe message streams before the library can classify task boundaries. <br>
Mitigation: Enable the library only through an explicit plugin or operator-owned hook and disclose the observed event scope before activation. <br>
Risk: The local ledger may store task summaries, costs, model names, session IDs, tool metadata, and cron or task history. <br>
Mitigation: Confirm the SQLite database path before use and treat the ledger as local usage telemetry. <br>
Risk: Installing native dependencies may download a signed prebuild or compile a local Node.js addon. <br>
Mitigation: Review the Node.js 22 and better-sqlite3 installation path in the target environment before enabling the library. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/jonathanjing/skills/openclaw-tally) <br>
- [Publisher profile](https://clawhub.ai/user/jonathanjing) <br>
- [Project homepage](https://github.com/JonathanJing/openclaw-tally) <br>
- [Product requirements document](PRD.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline code and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local integration guidance for a library-only release; runtime integrations must be explicitly enabled outside the skill bundle.] <br>

## Skill Version(s): <br>
0.3.2 (source: server release metadata, SKILL.md metadata, skill.json, package.json, src/index.js) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
