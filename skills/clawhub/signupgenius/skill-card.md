## Description:

Automates SignUpGenius workflows for reading profiles, groups, sign-up sheets, slots, and reports, with limited write actions for group membership, RSVPs, slot claims, and slot releases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External organizers, volunteers, and agents acting for a SignUpGenius account holder use this skill to check commitments, inspect public or owned sign-up availability, manage owned group members, RSVP, and claim or release the signed-in user's slots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a SignUpGenius account through credentials, an API key, or a browser-session bridge.

Mitigation: Install only for trusted personal use, keep credentials and API keys private, and treat browser-session access as sensitive.

Risk: The skill can perform real write actions such as RSVPs, slot claims or releases, and group-member additions.

Mitigation: Require explicit user confirmation before write actions and review any dry-run or preview details before execution.

Risk: Public participant listing could expose or aggregate information from organizers' sign-ups.

Mitigation: Use participant data only for authorized, personal-scale workflows and avoid scraping or aggregating other organizers' sign-ups.

Risk: Pro reports may include participant and custom-question details for owned sign-ups.

Mitigation: Use report tools only for sign-ups owned by the authenticated account and handle returned participant details as sensitive.

## Reference(s):

- [SignUpGenius](https://www.signupgenius.com)
- [signupgenius-mcp npm package](https://www.npmjs.com/package/signupgenius-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SignUpGenius account, group, slot, RSVP, and report details returned through configured MCP tools.]

## Skill Version(s):

1.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
