## Description:

zola-api helps agents query and update Zola wedding-planning data from a shell using curl against the Zola mobile API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Zola account operators use this skill to produce shell-based workflows for reading and changing vendors, budget, guests, seating, RSVPs, registry, invitations, gift tracker, and wedding website data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A long-lived Zola refresh token can expose the account if it is printed, logged, pasted into public text, or stored insecurely.

Mitigation: Treat the refresh token like a password, keep it out of logs and public output, and rotate it immediately if exposed.

Risk: The skill can guide broad live changes to wedding-planning data, including add, update, delete, registry, guest, RSVP, budget, invitation, and public website operations.

Mitigation: Require explicit confirmation before any write or delete action and review the exact target IDs and request body before execution.

Risk: Several Zola write endpoints replace whole records, so partial request bodies can wipe unrelated fields.

Mitigation: Use the documented read-modify-write workflow: fetch the current record first, preserve unchanged fields, and patch only the intended values.

## Reference(s):

- [Zola mobile-api endpoints](references/mobile-api-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zola-api)
- [Zola mobile API base URL](https://mobile-api.zola.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands often return JSON data envelopes and may require jq for filtering.]

## Skill Version(s):

1.12.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
