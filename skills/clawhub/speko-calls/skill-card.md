## Description:

Place and monitor outbound AI phone calls through Speko.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speko](https://clawhub.ai/user/speko)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to place approved outbound AI phone calls through Speko, monitor call status, and retrieve call reports, recordings, and transcripts. It is intended only for cases where dialing is explicitly requested and each recipient, number, and call purpose has been confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can place real paid outbound phone calls to physical telephone numbers.

Mitigation: Install only where outbound calling is approved and audited, require the platform API key from the environment, and confirm the full E.164 number and call purpose before every call.

Risk: Call reports, transcripts, recordings, and structured data can contain phone numbers and call content.

Mitigation: Treat call artifacts as sensitive, account for phone numbers echoed in structured data, and avoid pasting credentials or sensitive details into logged shell commands.

Risk: Misuse could include emergency calls, premium-rate calls, unwanted outreach, volume dialing, or impersonation.

Mitigation: Refuse emergency lines, premium-rate numbers, recipients without an apparent relationship, volume dialing, and impersonation; stop at one confirmed call unless the user explicitly authorizes more one number at a time.

## Reference(s):

- [Speko Calls Skill Page](https://clawhub.ai/speko/skills/speko-calls)
- [Speko API Base URL](https://api.speko.dev/v1)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON response fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl, jq, and SPEKO_PLATFORM_API_KEY; call reports may include phone numbers, summaries, outcomes, transcripts, recordings, structured data, and cost fields.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
