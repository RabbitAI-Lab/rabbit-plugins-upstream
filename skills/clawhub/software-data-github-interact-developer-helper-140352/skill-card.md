## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams plan and execute GitHub-style workflows for bug fixing, reliability hardening, and adjacent ClawHub skill work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, AI-agent users, skill authors, maintainers, and teams use this skill to turn GitHub-style maintenance needs into practical workflows, artifacts, checklists, analysis, code changes, and verification notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has broad triggers for GitHub, CLI, issue, API, and bug-fix requests, so it may be selected for requests that need more precise routing. <br>
Mitigation: Review activation behavior before installation and narrow triggers or disable implicit invocation when precise routing is required. <br>
Risk: Workflow or code-change guidance could be incorrect or incomplete for a specific repository or production context. <br>
Mitigation: Review proposed changes before execution, run the suggested verification commands, and confirm assumptions against the target repository. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/software-data-github-interact-developer-helper-140352) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Popular ClawHub skill demand: Github](https://clawhub.ai/skills/github) <br>
- [GitHub issue demand signal: PinePods issue 903](https://github.com/madeofpendletonwool/PinePods/issues/903) <br>
- [Hacker News demand signal: GitHub project maintainer has many issues](https://news.ycombinator.com/item?id=48829445) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional inline code, shell commands, configuration snippets, checklists, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance-only skill; no hidden execution, credential access, persistence, or destructive behavior reported by the authoritative security evidence.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
