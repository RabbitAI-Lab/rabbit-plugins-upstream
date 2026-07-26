## Description: <br>
Creates user-facing App Store release notes by collecting and summarizing user-impacting changes since the last git tag or a specified ref. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dimillian](https://clawhub.ai/user/dimillian) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and release managers use this skill to turn local git history into concise App Store "What's New" notes that emphasize user-visible changes and omit internal work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads commit subjects and touched file names from the selected repository range, which may expose private project details to the agent. <br>
Mitigation: Run it only on repositories and ranges the agent may inspect, and pass a specific starting tag or ref for private repositories. <br>
Risk: If no tag or starting ref is supplied, the helper may summarize full repository history. <br>
Mitigation: Provide an explicit starting ref when the intended release range is narrower than full history. <br>


## Reference(s): <br>
- [App Store Release Notes Guidelines](references/release-notes-guidelines.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown bullet list with an optional title] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Release notes should map to real changes in the selected git range and avoid internal jargon.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
