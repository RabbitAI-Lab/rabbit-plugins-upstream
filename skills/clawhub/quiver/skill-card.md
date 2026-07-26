## Description: <br>
Query alternative financial data from Quiver Quantitative, including Congress trading, lobbying, government contracts, and insider transactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stuhorsman](https://clawhub.ai/user/stuhorsman) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and market researchers use this skill to query Quiver Quantitative alternative financial datasets and inspect non-traditional market signals as JSON records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Quiver Quantitative API key. <br>
Mitigation: Provide QUIVER_API_KEY through a secure environment variable or secret store and avoid committing credentials to project files. <br>
Risk: The skill depends on the quiverquant Python package. <br>
Mitigation: Install the dependency from a trusted package source before use. <br>


## Reference(s): <br>
- [Quiver Quantitative Skill Page](https://clawhub.ai/stuhorsman/skills/quiver) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [JSON arrays returned by command-line calls, with Markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires QUIVER_API_KEY and the quiverquant Python dependency.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
