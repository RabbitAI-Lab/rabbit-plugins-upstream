## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create practical Skill Vetter-style workflows, checklists, analyses, and implementation support for bug fixing, safety hardening, reliability improvement, and adjacent skill creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, skill authors, maintainers, and teams use this skill to turn Skill Vetter-style needs into concrete local workflows, checklists, analyses, code changes, shell commands, or configuration guidance. It is intended for practical review, bug fixing, setup hardening, reliability improvement, and related skill-creation tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has broad trigger wording that may activate for ordinary security, GitHub, or bug-fix requests. <br>
Mitigation: Prefer explicit invocation or narrower trigger wording when predictable activation matters. <br>
Risk: Workflow, code, command, or configuration suggestions may be incomplete or unsuitable for a user's specific environment. <br>
Mitigation: Review generated outputs before execution and validate them against the stated success criteria and remaining risks. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter) <br>
- [ClawHub Github skill demand signal](https://clawhub.ai/skills/github) <br>
- [Ask HN: Active GitHub accounts delivering malware](https://news.ycombinator.com/item?id=48548530) <br>
- [GitHub issue: no-secret-in-config guarantee](https://github.com/Elevarq/Arq-Signals/issues/101) <br>
- [GitHub issue: credential-provider abstraction](https://github.com/Elevarq/Arq-Signals/issues/93) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with optional code blocks, command snippets, checklists, and validation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are tailored to the user's immediate context and should include assumptions, limits, and verification notes when useful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
