## Description: <br>
Mixmax (mixmax.com) requests for reading, creating, and updating data through the OOMOL-connected Mixmax connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to operate Mixmax from an OOMOL-connected account, including listing sequences, searching sequence recipients, and adding recipients after confirming state-changing payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a connected Mixmax account through OOMOL. <br>
Mitigation: Install and use it only with an intended OOMOL account and connected Mixmax workspace. <br>
Risk: The add_sequence_recipients action can change Mixmax sequence state. <br>
Mitigation: Confirm the exact payload, target sequence, recipients, and intended scheduling effect before running the write action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mixmax) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Mixmax homepage](https://www.mixmax.com/) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The agent fetches the live connector schema before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
