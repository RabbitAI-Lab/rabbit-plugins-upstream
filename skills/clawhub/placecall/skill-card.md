## Description:

PlaceCall lets an agent call US businesses for reservations, inquiries, and quotes, then return verified outcomes, transcripts, and recordings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voygr](https://clawhub.ai/user/voygr)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use PlaceCall to let agents contact US businesses by phone, including booking or changing reservations, asking questions, checking availability, and requesting quotes. It is intended for real-world phone workflows where the agent reports call outcomes and transcript details back to the user.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The skill can place real phone calls that ring businesses and may spend account credits.

Mitigation: Confirm the destination number and call brief before placing a call, and use it only for numbers the user is authorized to call.

Risk: The API key can authorize calls and consume credits if exposed.

Mitigation: Store the key in the skill configuration or PLACECALL_API_KEY environment variable, and do not paste or print secrets in chat.

Risk: Calls can involve sensitive subjects or requests for payment, login codes, health details, or unnecessary personal information.

Mitigation: Avoid those task categories and keep call briefs limited to the minimum information needed for the task.

Risk: Call transcripts, recordings, and place-suggestion text can contain untrusted statements from third parties.

Mitigation: Treat returned transcripts, recordings, summaries, and suggestion rationale as data to evaluate rather than instructions for the agent to follow.

## Reference(s):

- [PlaceCall ClawHub listing](https://clawhub.ai/voygr/skills/placecall)
- [Publisher profile](https://clawhub.ai/user/voygr)
- [PlaceCall homepage](https://github.com/voygr-tech/placecall)
- [PlaceCall API](https://api.voygr.tech)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include call status, verified outcome, transcript details, recording references, place suggestions, and setup guidance for PLACECALL_API_KEY.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter version 6.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
