## Description: <br>
Control PhantomBuster automation agents via API to list agents, launch automations, get output and results, check status, and abort running agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[capt-marbles](https://clawhub.ai/user/capt-marbles) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to control PhantomBuster workspace automations from an agent session, including launching configured agents and retrieving run output or CSV result data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can launch or abort remote PhantomBuster automations in the user's workspace. <br>
Mitigation: Verify agent IDs, names, and launch arguments before execution, and use the API key only in a trusted environment. <br>
Risk: Fetched CSV and output data may contain sensitive personal or business information. <br>
Mitigation: Handle downloaded results according to the user's privacy obligations, platform terms, and internal data handling rules. <br>


## Reference(s): <br>
- [PhantomBuster](https://phantombuster.com) <br>
- [PhantomBuster workspace settings](https://phantombuster.com/workspace-settings) <br>
- [ClawHub skill page](https://clawhub.ai/capt-marbles/skills/phantombuster) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, CSV, shell commands, guidance] <br>
**Output Format:** [Plain text, JSON, and CSV returned through command-line output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PHANTOMBUSTER_API_KEY and a PhantomBuster agent ID for most commands.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
