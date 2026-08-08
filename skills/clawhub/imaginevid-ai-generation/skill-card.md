## Description:

Use ImagineVid's authenticated agent generation tools to create image, video, or music outputs across the current capability catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[imaginevid-ai](https://clawhub.ai/user/imaginevid-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to discover ImagineVid media-generation capabilities, quote credit costs, submit approved image, video, or music generation requests, and check generation status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend credits from the connected ImagineVid account.

Mitigation: Show the exact server-returned quote and require explicit user approval before creating a generation.

Risk: Ambiguous submission outcomes can lead to duplicate generation attempts.

Mitigation: Do not retry after submission_unknown or unclear provider outcomes; continue polling the returned generation when available.

Risk: Credentials or private account details could be mishandled if collected in chat.

Mitigation: Use the host OAuth flow and avoid asking users to paste tokens, cookies, or private account identifiers.

## Reference(s):

- [ImagineVid](https://imaginevid.io)
- [ImagineVid Agent Tool Contract](references/tool-contract.md)
- [ClawHub Skill Page](https://clawhub.ai/imaginevid-ai/skills/imaginevid-ai-generation)

## Skill Output:

**Output Type(s):** [API Calls, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with tool calls, status updates, and returned result URLs or metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live capability catalog and server-returned quotes; requires explicit user approval before spending credits.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
