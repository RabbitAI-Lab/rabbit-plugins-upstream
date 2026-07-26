## Description: <br>
here.now lets agents publish websites and files to live URLs in seconds. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[adamludwin](https://clawhub.ai/user/adamludwin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and teams use here.now to publish selected files or folders as websites, raw file viewers, workspace-owned sites, or private Drive storage. It helps create live URLs, manage access controls, update existing publishes, and share persistent private files through shell workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload selected local files and create public links. <br>
Mitigation: Confirm the intended files and access mode before publishing; use password, restricted access, workspace access, or private Drive storage when content should not be public. <br>
Risk: Account credentials and claim tokens may persist across sessions. <br>
Mitigation: Treat ~/.herenow/credentials and .herenow/state.json as sensitive, avoid passing API keys as command-line flags in interactive use, and do not commit credential or state files. <br>
Risk: Anonymous published sites expire unless claimed or updated with an authenticated account. <br>
Mitigation: Share the current site URL and claim URL only from the latest script output, and tell users when an anonymous site expires in 24 hours. <br>


## Reference(s): <br>
- [here.now Documentation](https://here.now/docs) <br>
- [here.now Access Control Documentation](https://here.now/docs#access-control) <br>
- [here.now Workspace Documentation](https://here.now/docs#workspaces) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands, URLs, and JSON/API output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Publishing workflows return live site URLs and publish result details; Drive workflows return JSON metadata or file content.] <br>

## Skill Version(s): <br>
1.18.0 (source: evidence release version and artifact SKILL.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
