## Description: <br>
Helps Mac users free disk space by providing Terminal guidance to remove user cache files without targeting personal files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[olegmayami45-boop](https://clawhub.ai/user/olegmayami45-boop) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Mac users use this skill to recover local disk space when storage is low. The skill gives concise Terminal steps for removing files under the current user's cache directory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The cleanup command permanently deletes user cache files. <br>
Mitigation: Verify the command is exactly `rm -rf ~/Library/Caches/*` and understand it targets cache files before running it. <br>
Risk: A user may grant elevated access without understanding why macOS is asking. <br>
Mitigation: Avoid entering a password unless macOS clearly explains why permission is needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/olegmayami45-boop/skills/reclaim-disk-space-on-your-mac) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a macOS Terminal command that permanently deletes user cache files.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
