## Description: <br>
Monitor Minimax Coding Plan usage to stay within API limits, fetch current usage stats, and provide status alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[franky0617](https://clawhub.ai/user/franky0617) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and MiniMax Coding Plan users can run this skill to check current prompt usage, remaining quota, reset timing, and threshold-based status before continuing API-backed coding work. <br>

### Deployment Geography for Use: <br>
Global, for users with access to the MiniMax Coding Plan service. <br>

## Known Risks and Mitigations: <br>
Risk: The security review found that the skill loads and executes a broader parent .env file instead of the documented same-directory .env file. <br>
Mitigation: Review which .env file will be sourced before installing or running the skill, and prefer limiting it to MINIMAX_CODING_API_KEY and MINIMAX_GROUP_ID from a same-directory file or already-set environment variables. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/franky0617/skills/minimax-coding-plan-usage) <br>
- [MiniMax user center basic information](https://platform.minimax.com/user-center/basic-information) <br>
- [MiniMax coding plan remains endpoint](https://platform.minimax.com/v1/api/openplatform/coding_plan/remains?GroupId={GROUP_ID}) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal text with a usage summary, reset countdown, and status alerts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MINIMAX_CODING_API_KEY and MINIMAX_GROUP_ID, and depends on curl and jq.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
