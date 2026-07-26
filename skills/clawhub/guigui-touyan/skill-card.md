## Description: <br>
Epic Leek Daily generates structured daily A-share investment research notes from market data and IMA knowledge-base context, with emphasis on contrarian signals, extreme market events, and buy/sell-point review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlfan966-tech](https://clawhub.ai/user/jlfan966-tech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Investors and analysts use this skill to produce a daily Markdown research note for the A-share market, combining index and sector data with prior IMA knowledge-base notes when available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes investment notes to a configured local path and can sync them to a named IMA knowledge base. <br>
Mitigation: Confirm the local path, IMA connector, and target knowledge-base folder before first use. <br>
Risk: Broad trigger phrases could cause accidental note generation or sync. <br>
Mitigation: Invoke the skill by its explicit name when possible and review generated content before relying on it. <br>
Risk: Market analysis and suggested plans may be incomplete or misleading if source data or connectors are unavailable. <br>
Mitigation: Verify market data, assumptions, and any trading decisions independently before acting. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/jlfan966-tech/guigui-touyan) <br>
- [ClawHub skill page](https://clawhub.ai/jlfan966-tech/skills/guigui-touyan) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown investment research note] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes a dated local Markdown note and may sync it to the configured IMA knowledge base when connectors are available.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
