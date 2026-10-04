## Description:

Helps agents review SignUpGenius sign-ups, available slots, reports, and groups, and make requested group or sign-up changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to check volunteer slots, RSVPs, and group membership, and to request changes to their sign-ups or groups through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated access to a SignUpGenius account can expose account information and sign-up details.

Mitigation: Use project-scoped configuration, protect API keys, and avoid placing passwords in shared files.

Risk: The skill can change sign-ups and group membership; its summary understates the available write actions.

Mitigation: Review the intended recipient, slot, and confirmation preview before approving any change.

## Reference(s):

- [SignUpGenius skill release](https://clawhub.ai/chrischall/skills/signupgenius)
- [signupgenius-mcp package](https://www.npmjs.com/package/signupgenius-mcp)
- [SignUpGenius](https://www.signupgenius.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include slot availability, group details, and previews for sign-up changes.]

## Skill Version(s):

2.1.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
