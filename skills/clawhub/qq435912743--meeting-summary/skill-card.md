## Description:

Meeting Summary helps agents turn meeting transcripts, chat logs, or notes into structured summaries with conclusions, decisions, action items with owners and deadlines, open questions, risks, and follow-up topics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to convert meeting text into concise, actionable minutes. It is especially useful for extracting owner-deadline-action triples and separating confirmed decisions from unresolved questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The persistent learning helper can create or update a local learned_patterns.json file containing notes or preferences.

Mitigation: Use the learner commands only when the storage location is controlled, avoid confidential meeting material, and review or delete the learning file when needed.

Risk: Meeting records can be sensitive, and action extraction may miss or misidentify owners and deadlines.

Mitigation: Keep summaries in the user-designated location, do not externalize sensitive content, and mark missing owners or deadlines as pending confirmation.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown meeting summary with optional JSON action-item triples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action extraction is heuristic and should be reviewed by the agent before use.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
