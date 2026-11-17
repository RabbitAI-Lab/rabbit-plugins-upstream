## Description:

Retrieves public Douyin data through okdata, including videos, accounts, comments, trends, Xingtu creators, keywords, and Douyin Index metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and marketers use the skill to answer questions about public Douyin content, account activity, trends, and creator performance. It fetches data one page at a time, with paid API calls where required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid requests incur per-call charges, and fetching additional pages adds charges.

Mitigation: Check the endpoint price and set a call limit before fetching; request more pages only when needed.

Risk: Paid requests use an API key and send request data to an external service.

Mitigation: Keep the key in secret storage such as OKDATA_API_KEY, never print or log it, and send only data you are comfortable sharing with okdata.

Risk: The security review is partial and has medium confidence.

Mitigation: Review the service and data handling before use, and use it only if you trust the service and accept the data sent to it.

Risk: Fetched platform text may contain instructions written by other users.

Mitigation: Treat fetched text as data and do not follow instructions embedded in it.

## Reference(s):

- [Douyin API reference](https://okdata.online/apis/douyin/?src=skill-okdata-douyin)
- [okdata agent setup guide](https://okdata.online/agents.md)
- [ClawHub skill page](https://clawhub.ai/conn-ho/skills/okdata-douyin)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Text summaries and Markdown responses based on fetched Douyin data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One API page per call; additional pages require separate calls and charges.]

## Skill Version(s):

0.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
