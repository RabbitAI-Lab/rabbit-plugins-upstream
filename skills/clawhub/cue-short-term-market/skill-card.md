## Description:

Uses Cue to run short-term market research that tracks 24-hour catalysts, analyzes Dragon-Tiger List activity, maps overnight global events to A-share themes, and produces sourced analysis drafts for market observation and short-term trading research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market researchers use this skill to run Cue-powered public-data research workflows for short-term market themes, catalysts, trading calendars, sector flows, and intraday observations. The skill guides users through selecting a live Cue research buddy, confirming credit use, running the Cue runner, and returning sourced reports without fabricating missing results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may download or update Cue runner code before use.

Mitigation: Review and scan the runner source before deployment, and use a trusted pinned copy where change control is required.

Risk: The workflow uses a Cue account API key and calls Cue network services.

Mitigation: Use least-privilege credential handling, keep the API key out of prompts and logs, and confirm network use is acceptable for the environment.

Risk: Running deep research can consume Cue credits.

Mitigation: Require explicit user confirmation before each credit-consuming run and report empty results without retry loops that spend additional credits.

Risk: Market research outputs may be incomplete, stale, or unsuitable as financial advice.

Mitigation: Preserve source links, treat the report as research support only, and require user due diligence before trading or investment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-short-term-market)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and sourced research report text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve source links and should not invent reports when the Cue runner returns no content.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
