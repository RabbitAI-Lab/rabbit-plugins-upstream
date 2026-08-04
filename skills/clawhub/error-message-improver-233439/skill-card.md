## Description: <br>
Helps agents produce practical local workflows, checklists, and decision support for diagnosing home-network issues such as bufferbloat, router problems, modem problems, and latency. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Remote workers, gamers, home-office users, and small teams use this skill to turn symptoms and constraints into local diagnostic workflows for bufferbloat, router, modem, and latency issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill name and broad triggers may cause an agent to invoke it for unrelated error-message or general-help requests. <br>
Mitigation: Install only when a home-network diagnostics skill is intended, and tighten the name, description, and triggers before broad deployment. <br>
Risk: Network troubleshooting guidance can be misleading if the user provides incomplete device, ISP, topology, or measurement details. <br>
Mitigation: Ask only for missing details that materially change the diagnostic path, state assumptions, and include verification steps for each recommendation. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/error-message-improver-233439) <br>
- [Publisher Profile](https://clawhub.ai/user/kyro-ma) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or plain text with optional code, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should state assumptions, limits, validation steps, and follow-up work when useful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
