## Description:

Read MyAtriumHealth (Atrium Health's Epic MyChart patient portal) — test results, medications, allergies, immunizations, health issues, visits, goals — from a shell with the fpx CLI (@fetchproxy/cli), by relaying requests through your signed-in Chrome tab. Use when you want your MyChart data in a script or one-shot without running the myatriumhealth-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users access their own MyAtriumHealth portal information from shell workflows or scripts, including test results, medications, allergies, immunizations, health issues, visits, goals, and messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests access to login cookies despite claiming they stay inside the browser.

Mitigation: Before approving pairing, remove unnecessary cookie-reading and Cookie-header capture permissions and resolve the cookie assurance; keep health-record output private and revoke the bridge grant when finished.

## Reference(s):

- [MyAtriumHealth](https://my.atriumhealth.org/)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON data and shell output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contain sensitive personal health information; project responses to only the fields needed.]

## Skill Version(s):

1.3.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
