## Description: <br>
Monitor Minimax Coding Plan usage to stay within API limits. Fetches current usage stats and provides status alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesethrose](https://clawhub.ai/user/thesethrose) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to check MiniMax Coding Plan prompt usage, remaining quota, and reset timing so they can manage API consumption. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scanner reports that the script reads and executes a broader .env file than the setup instructions disclose. <br>
Mitigation: Review the script before running it, and use a skill-local .env file or export only MINIMAX_CODING_API_KEY and MINIMAX_GROUP_ID in the shell. <br>
Risk: Running the script with a shared parent .env may expose unrelated credentials or execute unintended shell content. <br>
Mitigation: Avoid shared parent .env files for this skill and limit the runtime environment to the two MiniMax variables it needs. <br>


## Reference(s): <br>
- [MiniMax Basic Information](https://platform.minimax.io/user-center/basic-information) <br>
- [MiniMax Coding Plan Remains API](https://platform.minimax.io/v1/api/openplatform/coding_plan/remains?GroupId={GROUP_ID}) <br>
- [Minimax Usage on ClawHub](https://clawhub.ai/thesethrose/skills/minimax-usage) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with shell commands and terminal text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MiniMax Coding Plan API credentials and jq/curl-compatible shell execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
