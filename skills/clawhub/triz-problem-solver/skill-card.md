## Description: <br>
Generate reviewable TRIZ innovation or TRIZ/DFMA cost-reduction concepts and expand a selected concept into a detailed solution by calling the PatSnap Solution Engine MCP endpoint over HTTP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwt1995](https://clawhub.ai/user/wwt1995) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and product teams use this skill to generate TRIZ-based product innovation, design improvement, DFMA, manufacturing simplification, assembly optimization, and cost-reduction concepts through PatSnap's Solution Engine endpoint. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Engineering problem descriptions and product details are sent to PatSnap's ai-fabric.patsnap.com service. <br>
Mitigation: Redact trade secrets, NDA material, personal information, proprietary technology, and export-controlled content before using the skill. <br>
Risk: Service-generated TRIZ or DFMA concepts may be incomplete, unsuitable, or misaligned with real-world constraints. <br>
Mitigation: Review returned candidates and details against engineering requirements, constraints, implementation difficulty, and safety considerations before acting. <br>
Risk: Long-running task failures or timeouts may still leave work processing on the remote service. <br>
Mitigation: Report the error to the user and ask before retrying to avoid duplicate tasks. <br>


## Reference(s): <br>
- [PatSnap Solution Engine MCP endpoint](https://ai-fabric.patsnap.com/mcp/patsnap-solution-engine?APP_ID=Patsnap) <br>
- [Eureka RD](https://eureka.patsnap.com/rd/#/agentic?type=triz&start_from=hub) <br>
- [ClawHub skill page](https://clawhub.ai/wwt1995/skills/triz-problem-solver) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown presentation with JSON-RPC results and inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns candidate idea summaries, job IDs, optional analysis fields, and selected solution details when returned by the PatSnap service.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
