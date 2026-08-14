## Description:

A Chinese A-share quantitative data analysis skill that uses AkShare to retrieve A-share market quotes, historical K-line data, financial data, board and industry information, fund flow, IPO, and margin financing information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to answer questions about Chinese A-share stock lookup, market data, financial analysis, sector analysis, screening workflows, and related data retrieval tasks. Outputs are informational and should not be treated as investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outputs may be mistaken for investment advice or relied on without checking the underlying market data.

Mitigation: Treat all retrieved data and analysis as informational, verify important results against authoritative sources, and do not use the skill as a sole basis for investment decisions.

Risk: AkShare data retrieval depends on network access and upstream public data sources that may change or fail.

Mitigation: Add local error handling and retry logic before operational use, and expect some interfaces to require maintenance when source websites change.

Risk: The fund-flow CLI action may fail because the security guidance notes that it may need a code fix.

Mitigation: Test the CLI locally before relying on the fund-flow action and patch the action if it fails in the target environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zuoyunlai/skills/akshare-stock)
- [Publisher profile](https://clawhub.ai/user/zuoyunlai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python examples, shell commands, and JSON CLI output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AkShare-backed data retrieval workflows that depend on network availability and upstream data-source stability.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
