## Description: <br>
Pullboard helps agents coordinate long, multi-step work on an external shared board with prioritized tasks, ownership, and independent verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pullboard](https://clawhub.ai/user/pullboard) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Pullboard when a build or investigation is too large for one context window and needs ordered work items, single-owner leases, and separate verification before completion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A leaked Pullboard bearer token could expose or modify a shared workspace. <br>
Mitigation: Treat the token as a secret, keep it out of chats and logs, and restrict access to ~/.pullboard/config.json. <br>
Risk: Sensitive task details may be sent to pullboard.dev through board items. <br>
Mitigation: Avoid putting sensitive details in board items unless the user is comfortable sending that information to the service. <br>


## Reference(s): <br>
- [Pullboard homepage](https://pullboard.dev) <br>
- [Agent-readable API reference](https://pullboard.dev/docs/llms.txt) <br>
- [OpenAPI schema](https://pullboard.dev/docs/openapi.json) <br>
- [Browsable docs](https://pullboard.dev/docs) <br>
- [ClawHub skill page](https://clawhub.ai/pullboard/skills/pullboard) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with shell commands and HTTP examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup and coordination steps for using a shared Pullboard workspace.] <br>

## Skill Version(s): <br>
1.1.0 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
