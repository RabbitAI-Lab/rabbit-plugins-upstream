## Description: <br>
Command-line tool to browse and query Polymarket prediction markets, view prices, orderbooks, and track positions without needing an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, analysts, traders, and agents use this skill to query public Polymarket market data from a terminal workflow, including search, trending markets, prices, orderbooks, categories, events, and volume views. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local verification can execute Python code from the product folder. <br>
Mitigation: Run verification in a disposable workspace or sandbox, especially for untrusted submissions. <br>
Risk: Live market data may be incomplete, delayed, or unavailable when the public API cannot be reached. <br>
Mitigation: Treat CLI output as informational and verify important market decisions against authoritative sources before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/polymarket-cli) <br>
- [Polymarket Gamma API](https://gamma-api.polymarket.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Terminal text output and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Queries live public API data; no API key or wallet is required by the artifact.] <br>

## Skill Version(s): <br>
2.0.1 (source: ClawHub release metadata; artifact frontmatter lists 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
