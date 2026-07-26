## Description: <br>
Enables agents to inspect schemas and run OOMOL connector actions for listing, retrieving, and updating BlazeMeter Service Virtualization service mock templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and QA engineers use this skill to work with BlazeMeter service mock templates through an OOMOL-connected account, including inspecting live schemas before list, get, or update operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can update BlazeMeter service mock template configuration in the connected workspace. <br>
Mitigation: Confirm the exact payload and intended effect with the user before execution, and make sure the OOMOL BlazeMeter connection is scoped to the intended workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-blaze-meter-service-virtualization) <br>
- [BlazeMeter Service Virtualization homepage](https://www.blazemeter.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects returned by the oo CLI when actions are executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
