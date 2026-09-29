## Description:

Helps agents search the web, retrieve page content, find similar pages, answer questions with citations, and run research tasks through Exa using Maton authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to search and analyze web content with Exa, request cited answers, or run asynchronous research through an authorized Maton connection. Optional hosted functions and triggers can automate approved tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private queries or internal URLs may be sent through the connected search service.

Mitigation: Review sensitive queries and URLs with the user before submitting them through Exa.

Risk: Hosted functions and triggers can run persistently or forward workspace, mailbox, or payment events to destinations.

Mitigation: Obtain explicit approval for each function, event source, trigger, and destination; review what data they access and where it goes.

Risk: Creating a connection or running a research task can authorize access or start ongoing work.

Mitigation: Confirm the intended account, connection, and research task with the user before approval.

## Reference(s):

- [Exa skill release](https://clawhub.ai/byungkyu/skills/exa-api)
- [Exa API documentation](https://exa.ai/docs)
- [Exa API reference](https://exa.ai/docs/reference/search)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with cited answers, API results, and command or code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research tasks may run asynchronously; results depend on the authorized connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
