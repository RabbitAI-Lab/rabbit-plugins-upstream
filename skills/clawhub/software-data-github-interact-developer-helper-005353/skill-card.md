## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams turn GitHub-style development requests into practical bug-fixing, setup-hardening, reliability, workflow, checklist, analysis, code, or adjacent-skill outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, AI-agent users, skill authors, maintainers, and teams use this skill to structure GitHub-style development work such as bug fixes, setup hardening, reliability improvements, issue workflows, and adjacent skill creation. It turns the user's goal and constraints into actionable local-friendly implementation steps, artifacts, checklists, analyses, code changes, and verification notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording may cause the skill to activate for general developer or GitHub-adjacent requests. <br>
Mitigation: Review when it activates and proceed with repository or GitHub actions only after the user explicitly asks for that task. <br>
Risk: Guidance or proposed changes for repositories can be incorrect, incomplete, or unsafe if applied without review. <br>
Mitigation: Review proposed steps and code, run the recommended verification commands, and scan changes before deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Release](https://clawhub.ai/kyro-ma/skills/software-data-github-interact-developer-helper-005353) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Popular ClawHub skill demand: Github](https://clawhub.ai/skills/github) <br>
- [Ask HN: How are you enabling your employees to do AI dev in the cloud?](https://news.ycombinator.com/item?id=48543969) <br>
- [Ask HN: Active GitHub accounts probably delivering malware, now what?](https://news.ycombinator.com/item?id=48548530) <br>
- [Add repo skill for standardized GitHub issue creation](https://github.com/repoprompt/repoprompt-ce/issues/232) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown responses with optional code blocks, shell commands, checklists, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should state assumptions, keep execution local-hardware friendly, and include verification notes when code or data is involved.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
