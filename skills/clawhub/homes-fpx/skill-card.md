## Description:

Query homes.com from a shell with the fpx CLI to search listings, resolve street addresses, fetch property detail, photos, history, and saved homes through the user's own signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve homes.com real-estate data from shell workflows when they need fpx-backed access through an already paired browser session rather than the homes-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access saved homes and saved searches through the user's paired homes.com browser session, which may reveal private housing preferences.

Mitigation: Run saved-home and saved-search recipes only when that account data is intended, and avoid storing or sharing resulting files unnecessarily.

Risk: The skill depends on a live paired Transporter browser session and homes.com pages that may redirect to sign-in or WAF challenge flows.

Mitigation: Confirm the paired www.homes.com tab is open, signed in when needed, and has cleared the challenge before relying on returned data.

## Reference(s):

- [homes.com request recipes](references/homes-requests.md)
- [ClawHub homes-fpx skill page](https://clawhub.ai/chrischall/skills/homes-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, Node.js, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include homes.com page data and account-specific saved homes or searches when the paired browser tab is signed in.]

## Skill Version(s):

1.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
