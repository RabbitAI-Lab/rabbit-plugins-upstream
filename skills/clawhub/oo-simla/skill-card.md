## Description: <br>
Simla.com is an agent skill for reading, creating, and updating Simla.com customer and order data through an OOMOL-connected Simla account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operators use this skill to let an agent inspect live Simla.com action schemas and run customer and order read, create, and edit actions through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Create and edit actions can change Simla.com customer or order data. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running any write-tagged action. <br>
Risk: The oo CLI setup, OOMOL sign-in, and Simla.com connection are part of the trust boundary. <br>
Mitigation: Only perform setup when a command fails for the documented reason, and verify that the user expects the OOMOL account and Simla.com connection being used. <br>
Risk: Customer and order records may contain sensitive business or personal data. <br>
Mitigation: Request and return only the data needed for the user's task, and avoid exposing unnecessary fields in prompts or summaries. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-simla) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>
- [Simla.com Homepage](https://www.simla.com/en) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload or response handling.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [State-changing Simla.com actions require user confirmation, and action schemas are inspected before payload construction.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
