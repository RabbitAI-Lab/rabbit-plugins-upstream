## Description:

Boka tvättid via bokatvattid.se: free slots, book, cancel, view bookings. Triggers: tvättid, tvättstuga, tvättbokning, gästlägenhet, laundry booking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[patello](https://clawhub.ai/user/patello)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find available laundry or guest-apartment slots, book or cancel reservations, and review current bookings for Boka tvättid/Visir v1-mode buildings. The skill requires the user's building, apartment number, and PIN credentials before it can act on the user's account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Debug mode can expose login or session details in logs.

Mitigation: Avoid running with BOKA_DEBUG enabled until debug output is redacted, and keep PINs out of chat, shell history, and logs.

Risk: The skill uses building, apartment, and PIN credentials to act on a real booking account.

Mitigation: Use only when the user is comfortable providing those credentials through config or environment variables, and do not include the PIN in final responses.

Risk: Booking and cancellation commands can make real changes to the user's reservations.

Mitigation: Confirm the exact room, date, and time before booking or cancelling, and do not use --yes without explicit user confirmation.

## Reference(s):

- [Boka tvättid legacy API reference](references/bokatvattid-api.md)
- [Boka tvättid web app](https://prod.bokatvattid.se)
- [ClawHub skill page](https://clawhub.ai/patello/skills/boka-tvattid)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text or Markdown with shell commands and summarized CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform real booking or cancellation actions after explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
