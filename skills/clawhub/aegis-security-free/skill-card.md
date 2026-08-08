## Description: <br>
Aegis Security Free helps agents perform basic blockchain safety checks, including address reputation, token honeypot checks, free quota lookup, and risk-level summaries for Ethereum and Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent users can use this skill for basic pre-transaction blockchain safety checks on Ethereum and Base. It is intended for address reputation checks, token honeypot screening, quota lookup, and human review of medium or higher risk results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad shell execution and local read capability for a narrow blockchain lookup workflow. <br>
Mitigation: Review before installing and prefer a version that limits execution to specific HTTP requests needed for address, token, and usage checks. <br>
Risk: API key and client fingerprint handling are not fully explained in the release evidence. <br>
Mitigation: Use environment variables for secrets, avoid committing keys, and confirm how client fingerprints are generated, stored, and transmitted before use. <br>
Risk: Blockchain risk results may be incomplete or uncertain. <br>
Mitigation: Use results as decision support only, require human review for MEDIUM risk results, and block or explicitly confirm HIGH and CRITICAL risk activity. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON-shaped API response examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include safety guidance and API response fields; results are not a guarantee of blockchain transaction safety and should be reviewed for important decisions.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
