## Description: <br>
Enables agents to inspect and manage Oracle Cloud Infrastructure resources through the OOMOL-connected oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to inspect OCI action schemas and run read, write, and destructive operations for connected tenancy, compute, monitoring, and networking resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change OCI resources and run Oracle Cloud Agent commands on target hosts. <br>
Mitigation: Require manual confirmation for all resource changes and for run_instance_agent_command, including the exact target instance and script content. <br>
Risk: State-changing actions may be proposed with incomplete or stale assumptions about required OCI inputs. <br>
Mitigation: Fetch the live action schema before building a payload and confirm the exact payload and expected effect before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-oracle-cloud) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Oracle Cloud Infrastructure homepage](https://www.oracle.com/cloud/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
