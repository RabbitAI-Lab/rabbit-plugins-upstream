## Description:

聊天 supports Doubao large-model chat workflows with model-call, API-integration, and search-oriented response guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to run chat, model-call, and search-assisted workflows that return conversational text, usage summaries, and troubleshooting guidance. It is not suited for decisions that require deterministic or human creative judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests read, write, and command execution authority beyond a narrow chat workflow.

Mitigation: Run it only in a constrained environment and review any file or command action before approval.

Risk: The artifact describes API key setup and ambiguous backend behavior.

Mitigation: Avoid providing credentials or sensitive files unless the publisher clarifies API key handling and command or file behavior.

Risk: The skill's broad documentation may produce outputs that are inaccurate or inappropriate for high-impact tasks.

Mitigation: Require human review for business-critical, security-sensitive, or deterministic decisions.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include chat replies, token or usage summaries, error messages, and setup guidance.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
