## Description:

Run deep, multi-source research queries via the kenkyu API and get back a cited answer with sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[george3d6](https://clawhub.ai/user/george3d6)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for thorough, sourced research using the kenkyu.dev API when a quick answer is not enough.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents send research queries and token-authenticated requests to an external paid service.

Mitigation: Use only with an intended kenkyu.dev account token and avoid sensitive, regulated, or confidential material unless external processing is acceptable.

Risk: Research calls can consume paid balance and require sufficient account funds.

Mitigation: Check account balance before long research runs and choose time limits deliberately.

## Reference(s):

- [kenkyu API base URL](https://kenkyu.dev)
- [ClawHub skill page](https://clawhub.ai/george3d6/skills/kenkyu-research)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown answer with cited source metadata returned from JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a short answer, a detailed markdown answer up to 500 words, cost and elapsed-time metadata, and source records with links, summaries, extracts, content, and weights.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
