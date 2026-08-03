## Description: <br>
Query alternative financial data from Quiver Quantitative, including Congress trading, corporate lobbying, government contracts, and insider transactions, using a Quiver API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plato-1](https://clawhub.ai/user/plato-1) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and finance-focused agents use this skill to query Quiver Quantitative data for politician stock trades, lobbying activity, government contracts, insider transactions, and related market signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires QUIVER_API_KEY, which could be exposed through shared shells, command history, or logs. <br>
Mitigation: Treat QUIVER_API_KEY as a secret and provide it through a local environment or secret-management workflow that avoids disclosure in shared logs. <br>
Risk: The referenced query script was not included in the inspected artifact, so documented commands may not work until the implementation is present. <br>
Mitigation: Confirm scripts/query_quiver.py exists and run a small authenticated test before relying on the skill in an agent workflow. <br>


## Reference(s): <br>
- [Quiver Quantitative](https://quiverquant.com) <br>
- [ClawHub skill page](https://clawhub.ai/plato-1/skills/quiver-quantitative) <br>
- [Publisher profile](https://clawhub.ai/user/plato-1) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires QUIVER_API_KEY; documented commands call scripts/query_quiver.py and return JSON suitable for jq filtering.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and claw.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
