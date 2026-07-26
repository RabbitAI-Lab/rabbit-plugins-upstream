## Description: <br>
Provides expert OAuth 2.0 implementation, troubleshooting, and token management guidance for Twenty CRM with Google and Microsoft OAuth plus email and calendar sync integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[avirweb](https://clawhub.ai/user/avirweb) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill as a troubleshooting and implementation reference for Twenty CRM OAuth flows, including login issues, token refresh, domain restrictions, and email/calendar sync. Review recommendations before applying them to production authentication systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes OAuth troubleshooting guidance that could weaken session protection if applied without review, including recommendations around readable auth cookies. <br>
Mitigation: Review authentication changes with a security engineer, prefer HttpOnly or server-managed sessions where possible, and never paste live OAuth secrets, token values, or raw environment output into chats, tickets, logs, or documentation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/avirweb/skills/twenty-oauth-mastery) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code, shell command, and SQL snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only OAuth troubleshooting reference; review generated guidance before using it in production.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
