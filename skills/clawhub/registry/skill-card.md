## Description: <br>
Search Sharebench, an open registry of reusable AI artifacts (skills, agent personas, prompts, playbooks in SKILL.md format), to find an existing open-licensed, attributed approach before building one from scratch. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sharebench](https://clawhub.ai/user/sharebench) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to search the public Sharebench registry before creating a reusable skill, prompt, agent persona, playbook, or knowledge artifact from scratch. It helps them find open-licensed, attributed examples and adapt relevant results to the user's context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Sharebench. <br>
Mitigation: Use generalized queries and avoid secrets, private customer data, internal project names, regulated information, or other confidential details. <br>
Risk: Returned registry artifacts may not fit the user's situation as-is. <br>
Mitigation: Read each returned artifact fully before reuse and adapt it to the user's actual context. <br>


## Reference(s): <br>
- [ClawHub Sharebench skill page](https://clawhub.ai/sharebench/skills/registry) <br>
- [Sharebench public search API](https://sharebench.ai/api/public/search?q=YOUR+QUERY) <br>
- [Sharebench artifact page pattern](https://sharebench.ai/p/<slug>) <br>
- [Sharebench public MCP server](https://mcp-public.sharebench.ai) <br>
- [Sharebench](https://sharebench.ai) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash commands and URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search queries are sent to Sharebench and results are returned as JSON by the public API.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
