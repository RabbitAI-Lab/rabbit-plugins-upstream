## Description: <br>
Opens PC368, extracts recent result rows, filters by composite-number tail matches while excluding triples and consecutive triples, and reports match rate and profit or loss. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[powerzzjohn](https://clawhub.ai/user/powerzzjohn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users can use this skill to analyze recent PC368 result data for selected composite-number tail targets and a chosen reporting window. It calculates matched periods, excluded periods, percentages, and a profit/loss formula from scraped page data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Opening pc368.net exposes normal visit metadata such as IP address and user agent. <br>
Mitigation: Use the skill only when browser access to pc368.net is acceptable for the user and environment. <br>
Risk: The profit/loss output is a calculation from scraped page data and may be mistaken for financial or gambling advice. <br>
Mitigation: Treat the result as a local calculation only, and review the underlying page data before relying on it. <br>
Risk: Page layout changes, popups, or network issues may affect scraped result accuracy. <br>
Mitigation: Verify the page state and visible result rows when the skill reports data shortages or extraction problems. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/powerzzjohn/skills/pc368-filter-analyzer) <br>
- [PC368 website](https://pc368.net/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown report with calculated counts, percentages, and profit/loss.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-supplied composite-number targets and period count; uses visible PC368 page data.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
