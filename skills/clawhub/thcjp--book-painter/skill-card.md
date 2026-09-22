## Description: <br>
Book Painter helps agents find and book local painter services through the Lokuli protocol. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to request local painter service search and booking assistance through an agent. Human review is appropriate before any order is placed because confirmation behavior, provider endpoints, and credential handling are not clearly specified. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad local read, write, and command authority without clear limits. <br>
Mitigation: Run it in a constrained agent environment and approve file or command actions explicitly before execution. <br>
Risk: Booking confirmation, provider endpoints, credential handling, and transmitted order information are unclear. <br>
Mitigation: Require human confirmation before sending service requests, credentials, or personal booking details. <br>
Risk: Inconsistent instructions may produce incorrect booking guidance or misleading status summaries. <br>
Mitigation: Review generated responses and verify provider details outside the skill before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/book-painter) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and occasional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API request guidance and booking-status summaries; confirmation and endpoint details are not well specified.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
