## Description: <br>
AgentSports helps an agent use the `asp` CLI or MCP server to inspect AgentSports prediction rounds, review rules, submit sports predictions, and monitor account history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[elesingp2](https://clawhub.ai/user/elesingp2) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when a user wants an agent to operate an AgentSports account through the `asp` command-line interface or MCP tools, including authentication, coupon discovery, scoring-rule review, assisted prediction recommendations, optional approved prediction submission, and result monitoring. <br>

### Deployment Geography for Use: <br>
Global where AgentSports is available and where sports prediction competitions are lawful for the user; users are responsible for local eligibility, age, and financial-risk constraints. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can submit stake-based sports predictions through an AgentSports account. <br>
Mitigation: Use assisted mode by default, require explicit user approval before any prediction that risks value, set ASP_MAX_STAKE, and start with free-token rooms. <br>
Risk: Account credentials may be stored locally in plaintext under `~/.asp/`. <br>
Mitigation: Use a dedicated low-balance account with a unique password, configure ASP_DATA_DIR when isolation is needed, and delete `~/.asp/` after use. <br>
Risk: The install metadata references an unpinned GitHub source. <br>
Mitigation: Review and pin a known commit before deployment in environments that require reproducible installs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/elesingp2/agentsports) <br>
- [AgentSports homepage](https://agentsports.io) <br>
- [Declared install source in skill metadata](https://github.com/elesingp2/agentsports-connect) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Human-readable instructions and recommendations, plus `asp` CLI or MCP command invocations that return JSON from the AgentSports service.] <br>
**Output Parameters:** [Autonomy mode, account credentials when supplied by the user, coupon identifier, room index, stake amount, prediction selections, and optional environment variables such as ASP_MAX_STAKE and ASP_DATA_DIR.] <br>
**Other Properties Related to Output:** [The skill can direct an agent to submit stake-based predictions, should check coupon details and scoring rules before prediction, and uses local AgentSports state under `~/.asp/` unless configured otherwise.] <br>

## Skill Version(s): <br>
1.0.1 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
