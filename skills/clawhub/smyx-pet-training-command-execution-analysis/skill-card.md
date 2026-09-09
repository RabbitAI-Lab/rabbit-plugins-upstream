## Description:

Analyzes pet training videos or video URLs through remote APIs to judge whether a pet follows Sit, Down, or Stay commands, including posture match, command timing, response latency, and report output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit pet training videos for command-execution recognition and to retrieve structured training analysis reports. It is intended for training-effect review and device handoff signals, not medical diagnosis or behavior therapy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos, video URLs, identity values, and report history are sent to remote APIs.

Mitigation: Review the provider before use, avoid sensitive media, and run the skill only in workspaces where this data sharing is acceptable.

Risk: Configured API endpoints may include HTTP development services or otherwise untrusted hosts.

Mitigation: Verify the active configuration uses trusted HTTPS endpoints before running analysis or history queries.

Risk: The skill can create or reuse a local identity and store account linkage or tokens in workspace data files.

Mitigation: Use an isolated workspace and protect or remove data/smyx-api-key.txt and data/smyx-common-claw.db when persistent account linkage is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-training-command-execution-analysis)
- [Pet training command API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown report text or JSON-like structured analysis returned from remote APIs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include posture match results, command timing, response latency, execution status, recommendations, historical report records, and report export links.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
