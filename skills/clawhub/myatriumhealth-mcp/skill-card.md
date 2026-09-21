## Description:

Read MyAtriumHealth (Atrium Health's Epic MyChart patient portal) — test results, medications, allergies, immunizations, health issues, visits, goals — from a shell with the fpx CLI (@fetchproxy/cli), by relaying requests through your signed-in Chrome tab. Use when you want your MyChart data in a script or one-shot without running the myatriumhealth-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable users use this skill to read their own MyAtriumHealth patient portal data from shell scripts or one-shot commands without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads personal health information through an authenticated MyAtriumHealth browser session.

Mitigation: Use it only for the signed-in user's own account, avoid shared terminals and logs, and unset MAH_TOKEN after use.

Risk: Broad authenticated request helpers may reach sensitive or state-changing portal actions beyond the intended read-only recipes.

Mitigation: Prefer documented read-only endpoints, review commands before execution, and add endpoint allowlists before broader deployment.

Risk: Expired, missing, or partially relayed sessions can appear successful while returning login pages, empty bodies, or empty JSON.

Mitigation: Check mah_signed_in and helper exit codes before trusting results, and require an active signed-in my.atriumhealth.org Chrome tab.

## Reference(s):

- [Skill page](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)
- [MyAtriumHealth portal](https://my.atriumhealth.org/myatriumhealth)
- [MyAtriumHealth endpoints](references/endpoints.md)
- [MyAtriumHealth shell helpers](references/mah.sh)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown with shell snippets and helper script references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-oriented fpx and jq recipes that operate through a signed-in browser session and print data to stdout.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
