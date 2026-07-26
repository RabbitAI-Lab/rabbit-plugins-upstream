## Description: <br>
Fetch reusable cryptocurrency realtime spot prices and historical price/K-line data for a symbol or coin id. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cryptoworldb1](https://clawhub.ai/user/cryptoworldb1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to fetch cryptocurrency spot prices, historical candles, and reusable JSON market data from supported market-data sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The published artifact appears incomplete because it documents scripts and references that are not included. <br>
Mitigation: Verify that the referenced Node script and data-source documentation are present before relying on the skill. <br>
Risk: The skill is intended to call external market-data services, so source availability and coverage may vary. <br>
Mitigation: Handle missing fields and source errors explicitly, and avoid inferring market cap, supply, or history when a source does not provide it. <br>
Risk: Using an output path can overwrite an existing file. <br>
Mitigation: Choose a non-sensitive output path and review the destination before running commands with an output file. <br>


## Reference(s): <br>
- [Server-resolved source](https://github.com/cryptoworldB1/skills/tree/main/crypto-market-data) <br>
- [Source repository](https://github.com/cryptoworldB1/skills) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Code, Guidance] <br>
**Output Format:** [JSON returned by a Node script, with shell command and import examples in Markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes query details, realtime ticker data, historical price or candle series, source metadata, and non-fatal source errors.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata; artifact metadata lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
