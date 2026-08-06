## Description:

Turns supplied support, product, or training materials into a grounded interactive digital-human customer education course where learners can ask voice questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

External customer education and support teams use this skill to convert help center articles, product documentation, support playbooks, supplied text, or selected documents into an interactive course that teaches customers how to resolve a high-frequency question cluster. The skill is intended for education and support deflection, not account-specific troubleshooting or guaranteed issue resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update the PersonWise CLI executable before creating courses.

Mitigation: Proceed only after explicit user approval for install or update actions, and use the bundled bootstrap and market-bound PersonWise service declared by the release.

Risk: Selected source documents or images may be uploaded to PersonWise for course generation.

Mitigation: Use only files named, attached, or explicitly selected by the user; get approval before uploading any local file discovered by the agent.

Risk: Generated education content could be mistaken for account-specific troubleshooting or a support guarantee.

Mitigation: Keep the course evidence-locked to supplied materials, avoid unsupported claims, and route diagnosis or unsupported questions to the user's support channel.

## Reference(s):

- [Customer Education on ClawHub](https://clawhub.ai/personwiseai/skills/personwise-customer-education)
- [PersonWise Agent API Resource](https://personwise.ai/api/agent)
- [PersonWise OAuth Protected Resource Metadata](https://personwise.ai/.well-known/oauth-protected-resource/api/agent)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON course blueprints, bounded patch files, shell command invocations, status summaries, and final course links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report PersonWise run IDs, project IDs, source statuses, review results, terminal state, and access-specific course URLs. Selected source documents or images may be uploaded to PersonWise for course generation.]

## Skill Version(s):

2.1.9 (source: server release evidence and skill attribution block)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
