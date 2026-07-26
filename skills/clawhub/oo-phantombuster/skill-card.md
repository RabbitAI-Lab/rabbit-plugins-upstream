## Description: <br>
PhantomBuster helps an agent read and operate PhantomBuster resources through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect PhantomBuster action schemas and run supported read, launch, and stop operations through an OOMOL-connected PhantomBuster account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked too broadly for PhantomBuster-adjacent requests. <br>
Mitigation: Use it only for PhantomBuster workflows and inspect the live action schema before constructing a payload. <br>
Risk: Launch, stop, or other account-changing operations can affect PhantomBuster resources. <br>
Mitigation: Ask for explicit user confirmation of the target, payload, and expected effect before running write actions, and keep connector permissions scoped to the intended account and work. <br>


## Reference(s): <br>
- [PhantomBuster homepage](https://phantombuster.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-phantombuster) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live schema inspection before execution and returns connector responses as JSON when actions are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact metadata and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
