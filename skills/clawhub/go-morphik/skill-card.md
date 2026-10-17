## Description:

Guides Go developers in using the unofficial go-morphik client for Morphik API document ingestion, retrieval, and management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Morphik document ingestion, search, retrieval, and queries into their projects with the unofficial Go client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Morphik API credentials or document contents could be exposed through logs or an unintended endpoint.

Mitigation: Keep MORPHIK_API_KEY out of code and logs; send credentials and selected documents only to Morphik or a deployment chosen by the user.

Risk: Document and connector operations can alter remote resources or send unintended data.

Mitigation: Limit ingestion, updates, deletion, and connector changes to user-requested, task-owned resources; review data before sending it.

## Reference(s):

- [go-morphik setup and reference](references/setup.md)
- [go-morphik source repository](https://github.com/psyb0t/go-morphik)
- [go-morphik on ClawHub](https://clawhub.ai/psyb0t/skills/go-morphik)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
