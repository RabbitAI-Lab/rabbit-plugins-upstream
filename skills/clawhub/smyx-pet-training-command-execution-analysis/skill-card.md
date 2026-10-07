## Description:

Analyzes pet-training videos to assess whether a pet performs sit, down, and stay commands and reports posture matching and response timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet trainers and developers use this skill to assess command execution in training videos and review analysis results or past reports. It does not provide medical diagnosis or behavioral therapy advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos or video URLs are sent to Life Emergence services for analysis.

Mitigation: Confirm permission to share the footage and review the service's data handling before use.

Risk: The skill can silently create or reuse an identity, log in remotely, and store tokens in a workspace SQLite database.

Mitigation: Review the account flow before installation and restrict access to the workspace and stored tokens.

Risk: Matching prompts can automatically retrieve cloud report history without clear user confirmation.

Mitigation: Require explicit user consent before querying history and confirm the account and report scope.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-training-command-execution-analysis)
- [Pet training analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table, with optional saved output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include command matching, response timing, and report links.]

## Skill Version(s):

1.0.13 (source: ClawHub server release; bundled frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
