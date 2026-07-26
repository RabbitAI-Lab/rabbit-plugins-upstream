## Description: <br>
Helps agent users, skill authors, maintainers, and teams create practical Gog-style productivity workflows for bug fixing, setup hardening, reliability improvement, and adjacent skill design. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to turn Google Workspace, CLI, bug-fix, and workflow-productivity requests into concise plans, checklists, scripts, templates, decision aids, or implementation support. It emphasizes local-hardware-friendly outputs and asks only for missing information that materially changes the result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may route unrelated Google, CLI, Gmail, Calendar, Drive, Contacts, or bug-fix requests to this skill. <br>
Mitigation: Narrow invocation rules or invoke the skill manually when the request is clearly about Gog-style workflow planning or productivity support. <br>
Risk: Generated scripts, configuration snippets, or workflow changes may not match the user's environment. <br>
Mitigation: Review outputs before use and validate them against the stated success criteria, assumptions, limits, and required inputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-gog-google-workflow-helper-080317) <br>
- [Requirement plan](artifact/references/requirement-plan.md) <br>
- [Popular ClawHub skill demand: Gog](https://clawhub.ai/skills/gog) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with optional code blocks, shell commands, checklists, templates, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, validation notes, remaining risks, and follow-up work when helpful.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
