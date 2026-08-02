## Description: <br>
Helps agent users and skill maintainers plan, fix, harden, and validate Tavily-style web search workflows on ClawHub. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agent users, skill authors, and maintainers use this skill to turn demand for Tavily-style web workflows into practical plans, checklists, templates, code changes, and validation notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad implicit invocation could route unrelated web or search requests through this workflow helper. <br>
Mitigation: Narrow the trigger keywords or require explicit invocation when precise routing is more important than convenience. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-tavily-web-workflow-helper-080414) <br>
- [Requirement plan](references/requirement-plan.md) <br>
- [Tavily Search demand signal](https://clawhub.ai/skills/openclaw-tavily-search) <br>
- [Web research demand signal](https://github.com/hugimuni-labs/brnrd/issues/411) <br>
- [Web access constraint signal](https://news.ycombinator.com/item?id=48985198) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, configuration snippets, and concise validation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are tailored to the user's immediate workflow and may include reusable checklists or implementation artifacts.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
