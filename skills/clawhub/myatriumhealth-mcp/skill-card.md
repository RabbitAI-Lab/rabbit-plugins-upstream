## Description:

Read MyAtriumHealth data, including test results, medications, allergies, immunizations, health issues, visits, goals, and messages, from shell workflows through a signed-in Chrome session using the fpx CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable MyAtriumHealth users use this skill to script read-only access to their own Epic MyChart patient-portal data through an already signed-in browser session. It is useful for one-shot data checks, jq-based projections, and shell workflows that do not require running the myatriumhealth-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can relay requests through a signed-in MyAtriumHealth browser session and expose sensitive health information.

Mitigation: Install only when comfortable granting fpx and its Chrome extension this access, treat command outputs and MAH_TOKEN as sensitive health information, and keep use scoped to the signed-in user's own account.

Risk: Broad or write-capable endpoint use could increase impact beyond the documented read-oriented workflows.

Mitigation: Prefer the documented read-oriented endpoint recipes, avoid broad or write-capable endpoints, and review commands before execution.

Risk: Browser-extension or fpx profile trust may persist after the immediate workflow is complete.

Mitigation: Understand how to revoke the fpx profile or browser-extension trust after use.

## Reference(s):

- [Skill source](artifact/SKILL.md)
- [MyAtriumHealth endpoint recipes](artifact/references/endpoints.md)
- [MyAtriumHealth shell helpers](artifact/references/mah.sh)
- [MyAtriumHealth portal](https://my.atriumhealth.org/myatriumhealth)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands and jq recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-oriented helper usage and command recipes; health data returned by those commands should be treated as sensitive.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
