## Description: <br>
Queries Chinese website ICP registration information, including registration number, subject name, registration type, status, and update time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, site operators, and agents use this skill to look up ICP filing details for a supplied domain through TianAPI and present the returned record fields clearly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys may be exposed if passed on the command line or committed in scripts/.env. <br>
Mitigation: Set TIANAPI_ICP_KEY through the shell or a managed secret store, avoid command-line key arguments, and do not commit local .env files. <br>
Risk: Each lookup sends the queried domain and the TianAPI API key to TianAPI. <br>
Mitigation: Use the skill only for domains that are appropriate to share with TianAPI and disclose this external API dependency to users. <br>


## Reference(s): <br>
- [TianAPI ICP Query API](https://www.tianapi.com/apiview/118) <br>
- [TianAPI ICP API endpoint](https://apis.tianapi.com/icp/index) <br>
- [ClawHub skill page](https://clawhub.ai/workxin/skills/tianapi-icp-query) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON from the helper script with human-readable explanatory text or command guidance from the agent] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and TIANAPI_ICP_KEY; each lookup sends the queried domain and API key to TianAPI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
