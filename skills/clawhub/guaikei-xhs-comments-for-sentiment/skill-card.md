## Description:

Retrieves public Xiaohongshu data for note search, note details, comment collection, and creator post monitoring, and leaves sentiment analysis or reporting to the calling agent workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketing analysts, content operators, and agent workflows use this skill to retrieve public Xiaohongshu search results, note details, comments, and creator posts for downstream trend, competitor, KOL, or sentiment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords or links and the GUAIKEI_API_TOKEN to the guaikei.com API.

Mitigation: Use only approved research topics and links, and configure the token only in trusted environments.

Risk: Successful results are saved locally under the package logs directory and may contain sensitive research topics or URLs.

Mitigation: Review and delete log files after use when they contain sensitive or non-public business research.

Risk: The tool retrieves public platform data but does not judge accuracy, sentiment, or business meaning on its own.

Mitigation: Have the calling agent or reviewer validate downstream summaries, sentiment labels, and business conclusions against the returned JSON.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-comments-for-sentiment)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [GUAIKEI API access and support](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Configuration, Guidance]

**Output Format:** [Structured JSON results with concise text guidance and command-line examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful task results are saved locally under the package logs directory; API access requires GUAIKEI_API_TOKEN.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
