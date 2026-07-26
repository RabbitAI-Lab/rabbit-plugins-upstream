## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams handle AdMapix-style software and data workflows by clarifying requirements, producing practical artifacts, and validating outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, agent users, skill authors, and maintainers use this skill to turn broad AdMapix-style software and data requests into concrete workflows, checklists, analyses, code changes, or decision support. It is aimed at local-hardware-friendly implementation and verification rather than cloud-only or large-training workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad auto-invocation wording may cause the skill to be selected for generic data or bug-fix requests. <br>
Mitigation: Narrow trigger wording or disable implicit invocation when precise routing is required. <br>
Risk: Workflow guidance can produce incorrect or incomplete implementation advice if the user's constraints are underspecified. <br>
Mitigation: Restate assumptions, ask only for materially missing inputs, and include verification commands or review criteria before acting on outputs. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/software-data-admapix-raw-developer-helper-035207) <br>
- [AdMapix ClawHub demand signal](https://clawhub.ai/skills/admapix) <br>
- [Ontology ClawHub demand signal](https://clawhub.ai/skills/ontology) <br>
- [Agent Browser ClawHub demand signal](https://clawhub.ai/skills/agent-browser-clawdbot) <br>
- [Hacker News data language discussion](https://news.ycombinator.com/item?id=48742811) <br>
- [Hacker News context layer discussion](https://news.ycombinator.com/item?id=48745664) <br>
- [SegmentFault DevLake plugin article](https://segmentfault.com/a/1190000042069896) <br>
- [SegmentFault mysql raw data question](https://segmentfault.com/q/1010000012550302) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should state assumptions, validation steps, and remaining risks when relevant.] <br>

## Skill Version(s): <br>
0.20260702.35207 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
