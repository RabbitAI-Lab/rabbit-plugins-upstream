## Description: <br>
Analyzes KRX-listed Korean equities using financial fundamentals, news outlook, and technical chart conditions to produce an investment-attractiveness score and BUY/HOLD/AVOID-style verdict. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[saebyeok-im](https://clawhub.ai/user/saebyeok-im) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents use this skill when a user asks for structured analysis of a Korean stock by ticker or company name. It is intended to summarize public KRX equity data from Naver Finance into weighted financial, news, and technical scores while avoiding casual or unsupported investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Investment-style scores and BUY/HOLD/AVOID-style verdicts may be mistaken for financial advice. <br>
Mitigation: Treat outputs as analytical summaries only, review the underlying data independently, and do not use the skill as the sole basis for trading decisions. <br>
Risk: Full analysis details may be written to stderr where orchestration logs could capture them. <br>
Mitigation: Avoid providing sensitive portfolio context, and review logging behavior before using the skill in workflows with retained logs. <br>
Risk: The skill is scoped to Korean KRX-listed equities and Naver Finance-style inputs. <br>
Mitigation: Reject non-Korean stocks, cryptocurrency, or unsupported assets, and verify ticker data before applying the scoring framework. <br>


## Reference(s): <br>
- [Equity Analysis Framework](artifact/references/framework.md) <br>
- [ClawHub skill page](https://clawhub.ai/saebyeok-im/skills/equity-analyst-test) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Structured plain text or Markdown with score breakdowns, verdicts, reasoning summaries, and optional command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are constrained to Korean equities and should not be treated as financial advice or as the sole basis for trading decisions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
