## Description: <br>
Guides agents through calling the Runware API correctly by inspecting model schemas, sending valid fields, choosing synchronous or asynchronous execution by modality, and reading the returned results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runware](https://clawhub.ai/user/runware) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill before making Runware generation calls to select the correct task type, validate model-specific request fields, choose synchronous or asynchronous execution, and read returned assets while managing cost. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may upload selected local input files to Runware services when executing generation tasks. <br>
Mitigation: Review inputs before execution and upload only files intended for Runware processing. <br>
Risk: Live Runware generation tasks can incur usage costs. <br>
Mitigation: Use dry-run validation or request cost reporting before committing to live or batch runs. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/runware/skills/runware-run) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Code] <br>
**Output Format:** [Markdown guidance with inline code identifiers and API request conventions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes dry-run and cost-reporting guidance for Runware tasks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
