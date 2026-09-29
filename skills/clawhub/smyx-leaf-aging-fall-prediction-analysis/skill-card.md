## Description:

Analyzes fixed-angle houseplant leaf images or videos to detect aging indicators and forecast likely leaf-fall windows over the next 3-7 days.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, plant-care operators, and developers use this skill to analyze plant leaf media, identify aging or stress signals, and receive structured care guidance with report links. It also supports querying prior leaf-aging and fall-risk analysis reports associated with the user's account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, URLs, and report history are processed by the publisher's remote service.

Mitigation: Use only media suitable for third-party remote processing, and avoid media containing people, private interiors, sensitive locations, or account data unless retention and deletion terms are clarified.

Risk: Analysis and history requests may be linked to a persistent local or remote identity.

Mitigation: Review identity handling before installation and avoid use where persistent association of plant media or report history is unacceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-leaf-aging-fall-prediction-analysis)
- [Leaf aging API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the returned analysis text to a user-specified output file.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
