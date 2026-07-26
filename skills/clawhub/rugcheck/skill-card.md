## Description: <br>
Analyze Solana tokens for rug pull risks using the RugCheck API, including safety scores, liquidity, holder distribution, metadata mutability, insider patterns, and token discovery lists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psychotechv4](https://clawhub.ai/user/psychotechv4) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and token reviewers use this skill to check Solana mint addresses for RugCheck risk signals and to inspect trending, new, recent, or verified Solana token lists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Solana token mint addresses submitted for analysis are sent to RugCheck. <br>
Mitigation: Invoke the skill for explicit token-checking requests and avoid submitting sensitive or embargoed token research. <br>
Risk: RugCheck responses are third-party risk signals and may be incomplete, stale, or interpreted as investment advice. <br>
Mitigation: Present results as informational risk analysis, avoid financial advice, and corroborate material decisions with additional sources. <br>
Risk: The skill uses a local shell helper to call an external API. <br>
Mitigation: Review commands before execution and confirm the RugCheck API destination is acceptable for the environment. <br>


## Reference(s): <br>
- [RugCheck API](https://api.rugcheck.xyz) <br>
- [RugCheck token page](https://rugcheck.xyz/tokens/<mint>) <br>
- [ClawHub skill page](https://clawhub.ai/psychotechv4/skills/rugcheck) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only RugCheck API queries; token-specific commands validate Solana-style mint addresses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
