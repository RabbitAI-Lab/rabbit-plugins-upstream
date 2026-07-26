## Description: <br>
随机返回一条幽默励志的打工人语录，涵盖加班、老板画饼等职场真实写照。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to fetch a random TianAPI workplace quote for lighthearted, motivational, or relatable workplace copy. The agent can call the helper script or API, parse the response, and present the quote clearly to the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys can be exposed if passed on the command line or committed in scripts/.env. <br>
Mitigation: Prefer TIANAPI_DGRYL_KEY from the shell or a managed secret store, avoid command-line keys, and keep any .env file out of version control with restricted file access. <br>


## Reference(s): <br>
- [TianAPI 打工人语录 API](https://www.tianapi.com/apiview/262) <br>
- [TianAPI DGRYL endpoint](https://apis.tianapi.com/dgryl/index) <br>
- [ClawHub skill page](https://clawhub.ai/workxin/skills/tianapi-dgryl) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [JSON from the helper script and concise text or Markdown when presenting quotes to users] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and TIANAPI_DGRYL_KEY; use a shell environment variable or managed secret store for the API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
