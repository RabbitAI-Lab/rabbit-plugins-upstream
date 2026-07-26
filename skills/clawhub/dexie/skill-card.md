## Description: <br>
Dexie lets agents and users query Dexie.space for Chia DEX offers, token prices, liquidity, trading pairs, and platform statistics through CLI or chat commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[koba42corp](https://clawhub.ai/user/koba42corp) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and Clawdbot operators use this skill to retrieve public Chia DEX market information from Dexie.space, including offers, token details, prices, pairs, and platform statistics. It is suitable for informational CLI and chat workflows, not for financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill returns market data that users could mistake for financial advice. <br>
Mitigation: Present results as informational Dexie.space data only and require users to make independent trading decisions. <br>
Risk: The skill depends on resolved npm packages and a public API client dependency. <br>
Mitigation: Install from the included package-lock.json or review resolved npm dependencies before deployment. <br>
Risk: Results depend on the availability and freshness of the public Dexie.space API. <br>
Mitigation: Handle API errors visibly and avoid treating returned prices, volumes, or liquidity as guaranteed real-time values. <br>


## Reference(s): <br>
- [Dexie.space](https://dexie.space) <br>
- [Dexie.space API](https://api.dexie.space/v1) <br>
- [ClawHub Dexie Skill](https://clawhub.ai/koba42corp/skills/dexie) <br>
- [Clawdbot](https://clawd.bot) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, guidance] <br>
**Output Format:** [Plain text formatted for CLI and chat messages, with JavaScript examples in documentation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses are generated from public Dexie.space API data and may include prices, volumes, liquidity, offer IDs, pair summaries, and error messages.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence, package.json, README, and CHANGELOG dated 2026-01-29) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
