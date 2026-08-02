## Description: <br>
Helps agent users, skill authors, maintainers, and teams apply GitHub-style development workflows for bug fixing, setup hardening, reliability improvements, and adjacent skill creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to turn GitHub-style workflow requests into practical implementation plans, checklists, artifacts, code changes, and verification notes. It is intended for local-hardware-friendly software and data workflows rather than cloud-only or large-training processes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked for broad GitHub or developer-help prompts because implicit invocation is enabled and trigger terms are generic. <br>
Mitigation: Review routing behavior before deployment and narrow trigger terms if precise invocation matters. <br>
Risk: Workflow guidance could be applied without checking project-specific constraints or success criteria. <br>
Mitigation: Require the agent to restate the outcome, constraints, available inputs, and verification approach before producing implementation guidance. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/software-data-github-interact-developer-helper-010622) <br>
- [Popular ClawHub Skill Demand: Github](https://clawhub.ai/skills/github) <br>
- [Ask HN: Active GitHub accounts delivering malware](https://news.ycombinator.com/item?id=48548530) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with optional code blocks, shell commands, checklists, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, success criteria, verification notes, and follow-up risks when helpful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
