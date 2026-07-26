## Description: <br>
Operate Statamic through an OOMOL-connected account to read, create, update, and delete Statamic site license data using the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and site operators use this skill to list and manage Statamic site licenses through an OOMOL-connected Statamic account, including create, update, and delete actions after inspecting the live action schema. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, and delete Statamic site licenses through OOMOL. <br>
Mitigation: Review proposed create, update, or delete payloads carefully and confirm state-changing actions before execution. <br>
Risk: First-time setup may install or authenticate the oo CLI. <br>
Mitigation: Run the installer or login flow only when the CLI or authentication is missing and only if OOMOL is trusted for the environment. <br>


## Reference(s): <br>
- [Statamic homepage](https://statamic.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
