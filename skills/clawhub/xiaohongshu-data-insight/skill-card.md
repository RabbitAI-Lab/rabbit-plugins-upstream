## Description:

This read-only skill searches public Xiaohongshu notes, retrieves note details and comments, and gathers creator posts and engagement data as JSON without logging in or publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, brand teams, and analysts use this skill to research topics, monitor competitors, assess creators, and summarize public comment sentiment on Xiaohongshu.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords and Xiaohongshu links are sent to the third-party Guaikei API, and the security review asks users to clarify what request data may be transmitted.

Mitigation: Before use, explain the data sent to Guaikei and avoid submitting sensitive keywords or links unless the user understands and accepts that data flow.

Risk: The security review says the artifact was only partially inspected and recommends against installation pending review.

Mitigation: Review the remaining skill components and resolve the security concerns before installing or using the skill.

## Reference(s):

- [Guaikei service](https://www.guaikei.com)
- [Output contract](references/contract.md)
- [Command options](references/options.md)
- [Request routing](references/routing.md)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [Structured JSON results with concise natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results cover public notes, note details, comments, creator posts, and engagement metrics; the command output uses a status envelope.]

## Skill Version(s):

1.2.3 (source: frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
