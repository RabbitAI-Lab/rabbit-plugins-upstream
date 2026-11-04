## Description:

Read and search your organization's Workvivo content through a browser session where you are signed in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees can use it to retrieve selected Workvivo posts, news, events, space content, colleague profiles, and search results when answering questions about their organization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The signed-in account may expose internal organization and employee information to the agent.

Mitigation: Pair only the intended Workvivo browser, use the organization's actual hostname, and select only fields relevant to the request.

Risk: Downloaded Workvivo documents may contain private information.

Mitigation: Keep downloaded documents private and share them only with authorized people.

Risk: Workvivo searches are recorded in the user's search history.

Mitigation: Avoid sensitive search queries when storing them in that history would be inappropriate.

## Reference(s):

- [Workvivo read endpoint recipes](references/endpoints.md)
- [Workvivo Fpx on ClawHub](https://clawhub.ai/chrischall/skills/workvivo-fpx)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Selected Workvivo data as JSON, with text or guidance when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only retrieval; searches add an entry to the user's Workvivo search history.]

## Skill Version(s):

0.2.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
