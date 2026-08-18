## Description:

Run deep, multi-source research queries via the kenkyu API and get back a cited answer with sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[george3d6](https://clawhub.ai/user/george3d6)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run thorough, sourced research through the kenkyu API when a quick answer is not enough.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and the API token are sent to kenkyu.dev.

Mitigation: Do not use the skill with secrets, credentials, private documents, regulated data, or confidential internal material unless that disclosure and cost have been approved.

Risk: External research runs may incur cost and require an account balance.

Mitigation: Check the token's account balance before starting research and set an appropriate time limit for the value of the question.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/george3d6/skills/kenkyu-research)
- [kenkyu API](https://kenkyu.dev)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [JSON API responses with plain-text and Markdown research answers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research results can include cited sources, source extracts, cost, elapsed time, and non-fatal parsing or query errors.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
