## Description: <br>
Get the current macOS Focus mode. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickchristensen](https://clawhub.ai/user/nickchristensen) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent check the currently active macOS Focus mode before tailoring responses or automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes the current macOS Focus mode name to the agent. <br>
Mitigation: Install only when the user is comfortable sharing that local Focus status with the agent. <br>
Risk: The helper is macOS-specific and depends on jq. <br>
Mitigation: Use it only on macOS systems with jq installed, and expect no useful output in unsupported environments. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text emitted to stdout, with Markdown usage guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports a single Focus mode name, such as No Focus, Office, Sleep, or Do Not Disturb.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
