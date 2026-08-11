## Description:

Conducts open-ended Q&A on image content based on computer vision and large language models, supporting natural language responses to user questions about images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to ask open-ended questions about image content, receive natural-language visual analysis, and retrieve prior visual question-answering reports from the publisher service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, URLs, user questions, and account-linked metadata may be sent to the publisher's cloud services for analysis and report retrieval.

Mitigation: Use non-sensitive media unless the publisher has documented retention, deletion, and authorization controls that meet the deployment requirements.

Risk: The skill creates persistent local identity state and may store tokens in a workspace SQLite database.

Mitigation: Review workspace data handling before installation, restrict filesystem access to trusted users, and clear the local data store when the skill is no longer needed.

Risk: The skill can query report history beyond a single visual question-answering request.

Mitigation: Confirm that report-history access is expected for the deployment and that account boundaries are understood before enabling the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-visual-qa-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](artifact/references/api_doc.md)
- [smyx_analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown or plain text containing visual question-answering results, report links, or structured JSON; results can optionally be written to a file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include cloud-generated analysis results, report history, and links to exported reports.]

## Skill Version(s):

1.0.13 (source: server release evidence; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
