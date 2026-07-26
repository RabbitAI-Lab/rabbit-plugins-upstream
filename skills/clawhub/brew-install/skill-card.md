## Description: <br>
Install missing binaries via dnf (Fedora/Bazzite package manager). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xejrax](https://clawhub.ai/user/xejrax) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users on Fedora or Bazzite use this skill to search for packages and install missing command-line binaries with dnf. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Package installation can change system state and may require administrator privileges. <br>
Mitigation: Review each proposed install command before approval and run it only on the intended Fedora/Bazzite system. <br>
Risk: The skill name may suggest Homebrew, but the artifact states that it wraps dnf rather than Homebrew. <br>
Mitigation: Use it only when dnf package searches or installs are desired. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires dnf on a Fedora/Bazzite system.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
