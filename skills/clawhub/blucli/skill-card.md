## Description: <br>
BluOS CLI (blu) for discovery, playback, grouping, and volume. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and users of Bluesound/NAD BluOS players use this skill to install and invoke the blu CLI for device discovery, playback control, grouping, TuneIn search/play, volume changes, and JSON output for scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the blu CLI with @latest may pull changing upstream code. <br>
Mitigation: Review or pin the upstream Go module before installation in environments with strict supply-chain requirements. <br>
Risk: Playback, grouping, or volume commands can affect the wrong BluOS player if the target is ambiguous. <br>
Mitigation: Confirm the selected device before changing playback, or set an explicit target with --device, BLU_DEVICE, or a config default. <br>


## Reference(s): <br>
- [Blucli homepage](https://blucli.sh) <br>
- [ClawHub skill page](https://clawhub.ai/steipete/skills/blucli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the blu CLI and a selected BluOS target device; scripts can request JSON output with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
