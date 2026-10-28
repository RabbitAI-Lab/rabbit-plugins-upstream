## Description:

CallForMe places calls to U.S. businesses on the user's behalf and returns answers and a transcript.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jakemarsh](https://clawhub.ai/user/jakemarsh)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask the agent to call businesses for information, quotes, reservations, appointments, or cancellations, and receive a summary of the call.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Calls and bulk call campaigns can incur charges, and auto-reload may add funds.

Mitigation: Set spending and call-count limits, and review auto-reload before paying.

Risk: A call may lead to a booking or cancellation decision on the user's behalf.

Mitigation: Explicitly approve booking or cancellation decisions before the agent agrees.

Risk: Call details and transcripts may be emailed or shared publicly.

Mitigation: Store the API key in protected secret storage and review transcripts before creating public sharing links.

## Reference(s):

- [CallForMe](https://callforme.tel)
- [CallForMe connection](https://callforme.tel/mcp)
- [CallForMe guide](https://callforme.tel/llms.txt)
- [Pricing](https://callforme.tel/docs/pricing)
- [Free demo calls](https://callforme.tel/demo)
- [ClawHub release](https://clawhub.ai/jakemarsh/skills/callforme)

## Skill Output:

**Output Type(s):** [text, JSON]

**Output Format:** [Call summaries, answers, and transcripts; structured call results may be returned as JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may also be emailed to the account holder.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
