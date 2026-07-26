## Description: <br>
Akshare Stock helps agents query A-share market quotes, historical candles, financial data, sector data, fund flows, IPO data, and margin data through an AkShare-based CLI workflow. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[terryso](https://clawhub.ai/user/terryso) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, developers, and analysts can use this skill to guide an agent through A-share stock data lookups and market-analysis workflows. Outputs should be treated as informational market data support, not investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The artifact describes commands for scripts/akshare_cli.py, but the security evidence says that CLI script is absent. <br>
Mitigation: Confirm the CLI script is included or provide an equivalent implementation before relying on the documented commands. <br>
Risk: The workflow may install and use external finance-data packages and fetch market data from the network. <br>
Mitigation: Review package sources, run the skill in a controlled environment, and treat returned market data as informational. <br>
Risk: Market data output can be mistaken for investment advice. <br>
Mitigation: Present results as data support only, avoid trading recommendations, and add source or retrieval context when available. <br>
Risk: AkShare-style data retrieval may fail when upstream websites or network conditions change. <br>
Mitigation: Handle failed or stale responses explicitly and cross-check important results before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/terryso/skills/akshare-stock) <br>
- [Server-resolved source repository path](https://github.com/terryso/claw-skills/tree/master/skills/akshare-stock) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and expected JSON or table command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The documented CLI defaults to JSON output and can request table output for human reading.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
