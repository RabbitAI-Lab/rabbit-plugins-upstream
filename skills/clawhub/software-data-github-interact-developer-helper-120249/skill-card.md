## Description: <br>
Helps agent users and maintainers plan, implement, and verify GitHub-style ClawHub workflows for bug fixes, setup hardening, reliability improvements, and adjacent skill creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, AI-agent users, skill authors, and maintainers use this skill to turn GitHub-style workflow needs into concrete plans, code or configuration guidance, checklists, and validation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad developer and GitHub-adjacent activation wording may select the skill for requests where proposed commands or code changes could affect repositories or local systems. <br>
Mitigation: Review suggested commands, code changes, and configuration edits before execution or approval. <br>
Risk: The skill provides workflow and implementation guidance but does not independently validate the user's repository state or credentials. <br>
Mitigation: Run the verification commands, scans, or tests recommended in the output and avoid sharing secrets in prompts or artifacts. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/software-data-github-interact-developer-helper-120249) <br>
- [Popular ClawHub skill demand: Github](https://clawhub.ai/skills/github) <br>
- [Popular ClawHub skill demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks, command examples, checklists, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are tailored to the user's stated constraints and should include assumptions, limits, and remaining risks when relevant.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
