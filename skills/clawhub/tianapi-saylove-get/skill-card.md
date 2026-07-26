## Description: <br>
随机获取一句土味情话。当用户需要情话、撩人语录或幽默表白时使用此技能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to fetch a random TianAPI cheesy love line for flirtatious quotes, humorous confessions, or similar short-form text prompts. It is useful when an agent should call TianAPI with a user-provided API key and present the returned quote. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The helper script sends a user-provided TianAPI key to TianAPI to retrieve a quote. <br>
Mitigation: Use the skill only when TianAPI use is acceptable, and store the key in TIANAPI_SAYLOVE_KEY or another secret mechanism instead of passing it on the command line. <br>
Risk: A local scripts/.env file may contain the TianAPI key if users choose that setup path. <br>
Mitigation: Do not commit scripts/.env or any file containing the API key, and rotate the key if it is exposed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/workxin/skills/tianapi-saylove-get) <br>
- [TianAPI Saylove API](https://www.tianapi.com/apiview/80) <br>
- [TianAPI Saylove Endpoint](https://apis.tianapi.com/saylove/index) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance and JSON command output from the helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a TianAPI key supplied through TIANAPI_SAYLOVE_KEY, a local scripts/.env file, or the --key command-line option.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
