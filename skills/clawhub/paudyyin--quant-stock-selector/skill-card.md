## Description: <br>
Selects top A-share stock candidates using multi-factor quantitative models across technical, fundamental, capital, chip distribution, concentration, and volume signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Investors and analysts with stock-market experience use this skill to generate informational daily A-share stock recommendations, win-rate reports, and market/news summaries. It is not a trading system and its outputs require independent investment judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stock recommendations can influence investment decisions and may be wrong, incomplete, delayed, or unsuitable for the user. <br>
Mitigation: Treat outputs as informational only, verify recommendations with independent analysis, and apply the artifact's stated position sizing and stop-loss discipline before acting. <br>
Risk: The skill supports email reports and requires a 163 email authorization code when that feature is enabled. <br>
Mitigation: Provide email credentials only when email reports are needed, store authorization codes outside public files, and rotate the code if it is exposed. <br>
Risk: Unpinned Python dependencies may change behavior over time. <br>
Mitigation: Review and pin dependency versions in a controlled environment before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/quant-stock-selector) <br>
- [Publisher profile](https://clawhub.ai/user/paudyyin) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, Python configuration snippets, shell commands, and structured stock-analysis summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces informational stock recommendations, score explanations, win-rate summaries, and optional email report setup guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
