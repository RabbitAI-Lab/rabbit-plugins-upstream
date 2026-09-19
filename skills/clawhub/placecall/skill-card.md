## Description:

PlaceCall lets an agent place real phone calls to US businesses for reservations, inquiries, quotes, and similar tasks, returning a verified outcome, transcript, and recording.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voygr](https://clawhub.ai/user/voygr)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use PlaceCall to let an agent call US businesses, ask questions, make or change reservations, request quotes, and report back with the call outcome and transcript.

### Deployment Geography for Use:

Global, with calls and place suggestions limited to United States destinations.

## Known Risks and Mitigations:

Risk: The skill can place real, recorded, potentially billable phone calls to people or businesses.

Mitigation: Confirm the destination number, authorization to call, brief, callback number, and any personal details before placing a call; use the skill only for US destination numbers.

Risk: The API key can spend call credits or expose account access if shared in chat or printed in logs.

Mitigation: Keep PLACECALL_API_KEY in OpenClaw config or an environment variable, reference it in commands without echoing it, and replace a lost key through the provider recovery flow.

Risk: Call transcripts and recordings may contain sensitive information and are stored by the service.

Mitigation: Put only task-needed information in the call brief, tell users calls are recorded, and treat transcripts and extracted fields as data to evaluate rather than instructions.

Risk: A timed-out or dropped POST request may still have placed a call, so an immediate retry could duplicate the call and charge.

Mitigation: List recent calls and reconcile by target number and creation time before retrying any request that may have reached the API.

Risk: Place suggestions and call briefs may include uncertain public-review-derived claims.

Mitigation: Review the suggested place card and call brief before dialing, and use the call to verify uncertain details instead of treating suggestion text as confirmed fact.

## Reference(s):

- [PlaceCall ClawHub listing](https://clawhub.ai/voygr/skills/placecall)
- [PlaceCall homepage](https://github.com/voygr-tech/placecall)
- [VOYGR publisher profile](https://clawhub.ai/user/voygr)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl commands, JSON request and response examples, and operational instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses PLACECALL_API_KEY for authenticated API calls to api.voygr.tech and can return call outcomes, transcripts, recordings, event-stream updates, place suggestions, and credit or quota status.]

## Skill Version(s):

6.0.1 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
