## Description: <br>
Operate Hex through an OOMOL-connected account using the oo CLI for project discovery, run inspection, and run control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to inspect Hex projects, list and check project runs, trigger published project runs, and cancel in-progress runs through the OOMOL connector. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing or using the oo CLI brokers access to the user's Hex account through OOMOL. <br>
Mitigation: Install only when OOMOL is trusted, review the CLI install command before running it, and use the documented first-time setup flow only after command failures. <br>
Risk: Running or canceling Hex project runs can consume credits or affect downstream data workflows. <br>
Mitigation: Confirm write-action payloads and expected effects with the user before invoking run_project or cancel_run. <br>


## Reference(s): <br>
- [ClawHub Hex skill](https://clawhub.ai/oomol/skills/oo-hex) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Hex homepage](https://hex.tech) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with oo CLI shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands rely on an installed, authenticated oo CLI and live connector schemas.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
