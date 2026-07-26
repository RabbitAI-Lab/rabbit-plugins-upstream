## Description: <br>
Security scanner for Moltbot skills. Scan GitHub repositories for vulnerabilities before installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[moltcheck](https://clawhub.ai/user/moltcheck) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to submit GitHub repository URLs to MoltCheck for security scanning before installing external Moltbot skills. It returns trust scores, risk summaries, permission analysis, credit status, and setup guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Repository URLs submitted for scanning are sent to moltcheck.com for analysis. <br>
Mitigation: Install and use this skill only for repositories you are comfortable sharing with MoltCheck. <br>
Risk: Setup and paid-credit flows may expose a MoltCheck API key, wallet address, memo, or payment instructions in command output. <br>
Mitigation: Use a MoltCheck-specific API key, keep setup output private, and avoid pasting sensitive setup details into shared logs. <br>
Risk: Credit-purchase details are provided by a third-party service. <br>
Mitigation: Independently verify wallet and credit-purchase details on the official MoltCheck site before sending funds. <br>


## Reference(s): <br>
- [ClawHub Moltcheck Skill Page](https://clawhub.ai/moltcheck/skills/moltcheck) <br>
- [MoltCheck Website](https://moltcheck.com) <br>
- [MoltCheck API Documentation](https://moltcheck.com/api-docs.md) <br>
- [MoltCheck OpenAPI Specification](https://moltcheck.com/openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance, configuration] <br>
**Output Format:** [JSON responses with scan summaries, trust scores, risk lists, credit status, or setup instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include third-party report URLs, API-key setup output, and payment instructions returned by MoltCheck.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
