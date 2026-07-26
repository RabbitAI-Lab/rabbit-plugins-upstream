## Description: <br>
Analyzes Korean KRX stocks using Naver Finance data to produce an Investment Attractiveness Score and BUY, BUY_LEAN, HOLD, or AVOID verdict. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[saebyeok-im](https://clawhub.ai/user/saebyeok-im) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to evaluate Korean listed equities with a structured framework that prioritizes financial fundamentals, then news outlook, then technical chart timing. It is intended for systematic analysis reports, not casual market opinions or non-Korean assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may rely on optional Python scripts that scrape Naver Finance and interact with an OpenClaw browser profile. <br>
Mitigation: Review scripts before running them and use a clean browser profile when possible. <br>
Risk: Generated stock scores and verdicts may be incorrect, stale, or unsuitable for financial decisions. <br>
Mitigation: Treat outputs as analysis drafts, verify source data independently, and avoid relying on them as investment advice. <br>
Risk: Batch reporting or LINE delivery workflows could send reports unexpectedly if configured by the user. <br>
Mitigation: Do not enable scheduled delivery workflows until their configuration and destinations have been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/saebyeok-im/skills/equity-analyst) <br>
- [Equity Analysis Framework](artifact/references/framework.md) <br>
- [Naver Finance stock pages](https://finance.naver.com/item/main.naver) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Structured Markdown report with numeric scoring fields and optional local text report files from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include financial, news, chart, final score, verdict, and reasoning sections.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
