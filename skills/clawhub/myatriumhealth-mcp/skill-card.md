## Description:

Guides signed-in MyAtriumHealth users in reading their own patient-portal data through shell commands relayed via a Chrome tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Patients and their authorized agents use this skill to retrieve their own MyAtriumHealth records, including results, medications, allergies, visits, and messages, from an authenticated browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad, persistent browser-mediated access exposes sensitive patient records to shell commands.

Mitigation: Use only on a trusted machine for your own authorized account; review the persistent pairing and remove it when no longer needed.

Risk: Raw responses or shell output may expose health details, messages, insurance information, or access tokens.

Mitigation: Project only needed fields; avoid logging, saving, or sharing raw responses and shell history.

Risk: Expired sessions or missing browser tabs can produce misleadingly empty responses.

Mitigation: Check the signed-in session and keep a signed-in portal tab open before interpreting empty results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/myatriumhealth-mcp)
- [MyAtriumHealth endpoint recipes](references/endpoints.md)
- [MyAtriumHealth shell helpers](references/mah.sh)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Retrieved patient records can contain sensitive personal health and insurance information.]

## Skill Version(s):

1.3.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
