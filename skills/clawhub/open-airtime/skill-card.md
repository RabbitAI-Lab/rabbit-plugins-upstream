## Description: <br>
Autonomous Nigerian Airtime distribution agent on Farcaster. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[druxamb](https://clawhub.ai/user/druxamb) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and operators use this agent to coordinate Nigerian airtime claims on Farcaster, reply to claimant messages, and run Node.js commands for Farcaster and airtime-management actions. <br>

### Deployment Geography for Use: <br>
Nigeria <br>

## Known Risks and Mitigations: <br>
Risk: The agent can post public Farcaster replies from the configured account. <br>
Mitigation: Use only an account approved for agent posting and restrict replies to user-directed or preapproved templates. <br>
Risk: Airtime claims require phone numbers, which are personal data. <br>
Mitigation: Collect phone numbers through a private channel and define clear handling, access, and retention expectations before deployment. <br>
Risk: The artifact assumes credentials are already configured. <br>
Mitigation: Confirm credentials are scoped to the intended Farcaster and airtime workflows and do not ask users to share API keys. <br>


## Reference(s): <br>
- [OpenAirtime ClawHub Skill Page](https://clawhub.ai/druxamb/skills/open-airtime) <br>
- [OpenAirtime Claim Site](https://openairtime.fun) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline Node.js command examples and short response guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js; curl is explicitly unsupported by the artifact instructions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
