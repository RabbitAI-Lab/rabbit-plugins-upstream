## Description: <br>
Operate Honeycomb through an OOMOL-connected account using the oo CLI connector for reading, creating, and updating Honeycomb data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to inspect Honeycomb schemas and run connector actions for datasets, boards, markers, and authentication status through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Marker creation changes Honeycomb state. <br>
Mitigation: Confirm the exact marker payload and intended effect with the user before running write actions. <br>
Risk: First-time setup can install the oo CLI or connect an OOMOL account. <br>
Mitigation: Run setup commands only after an authentication, connection, or missing-command failure and only when the user trusts OOMOL for this integration. <br>


## Reference(s): <br>
- [Honeycomb homepage](https://www.honeycomb.io/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub Honeycomb skill page](https://clawhub.ai/oomol/skills/oo-honeycomb) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses schema-first connector calls and returns oo CLI JSON responses when actions are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
