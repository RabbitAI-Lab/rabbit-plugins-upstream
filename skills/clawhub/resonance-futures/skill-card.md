## Description: <br>
Design and run an agent-native, evidence-settled prediction market covering the trust model, market lifecycle, machine-measurable settlement, anti-gaming rules, and the path from play credits to real money. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickflach](https://clawhub.ai/user/nickflach) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and product teams use this skill to design safer agent-native prediction markets with separated proposal, curation, trading, settlement, identity, and ledger responsibilities. It is most relevant before implementing real-money or play-credit markets that rely on machine-measurable evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prediction markets that handle identity, settlement, custody, or real money can create financial and legal exposure if launched without review. <br>
Mitigation: Obtain legal review before real-money use and keep settlement, custody, identity, and ledger permissions separated. <br>
Risk: Incorrect settlement or inconsistent ledger updates can mislead users or pay the wrong outcome. <br>
Mitigation: Use evidence-first settlement, append-only double-entry ledgers, durable outbox delivery, idempotent retries, and dispute windows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nickflach/skills/resonance-futures) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with architecture patterns, lifecycle rules, risk controls, and implementation constraints] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Non-executable design guidance; any implementation should receive legal review before real-money use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
