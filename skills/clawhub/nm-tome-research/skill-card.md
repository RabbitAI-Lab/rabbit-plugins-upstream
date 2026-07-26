## Description: <br>
Runs multi-source research across GitHub, HN, Reddit, arXiv, and Semantic Scholar. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical researchers use this skill to run an agent-assisted research session, dispatch channel-specific research agents, synthesize findings, and save a formatted report in the workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generic research prompts may invoke an agent-assisted workflow that dispatches multiple research agents. <br>
Mitigation: Confirm the research scope and expected sources before dispatching agents. <br>
Risk: The skill can save research reports and session state into the workspace under docs/research/. <br>
Mitigation: Review generated files before committing, sharing, or relying on the saved report. <br>
Risk: Synthesized multi-source findings may include incomplete, stale, or misleading information. <br>
Mitigation: Review source evidence and top findings before using the report for decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-tome-research) <br>
- [Tome Plugin Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/tome) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown report with summaries, findings, saved workspace path, and optional code or command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save research output and session state under docs/research/.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
