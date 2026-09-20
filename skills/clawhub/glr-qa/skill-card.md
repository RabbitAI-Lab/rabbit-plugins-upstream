## Description:

Run goal-driven GameLearningRuntime QA against an authorized game, training adapter, replay, or live probe and produce a dated JSON plus self-contained HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and project owners use this skill to run bounded GameLearningRuntime checks on authorized games, adapters, replays, or live probes and summarize the resulting evidence. It helps distinguish deterministic checks, replay results, training metrics, and missing live evidence without claiming release quality from a single smoke test.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose training or live-probe checks that execute commands against a local project.

Mitigation: Review proposed commands before execution and run them only against projects and environments the user is authorized to test.

Risk: Generated QA reports could include proprietary traces, secrets, or unapproved live-game data.

Mitigation: Keep proprietary traces, secrets, local overrides, and unapproved live-game data out of published artifacts.

Risk: A passing smoke command or synthetic check could be mistaken for full release quality.

Mitigation: Report evidence scope explicitly and separate deterministic checks, replay results, training metrics, synthetic installer tests, and authorized live acceptance.

## Reference(s):

- [ClawHub glr-qa skill page](https://clawhub.ai/loonghao/skills/glr-qa)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and references to generated JSON and HTML QA reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces human-facing QA summaries from bounded checks; generated project artifacts include result.json and index.html when the underlying GLR QA command is run.]

## Skill Version(s):

0.22.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
