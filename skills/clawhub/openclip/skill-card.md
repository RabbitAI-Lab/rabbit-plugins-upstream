## Description: <br>
OpenClip lets an agent use the OpenClip MCP server to clip long videos into captioned short-form moments, transcribe and convert media, edit images or video, remove backgrounds, and generate short UGC-style ad clips. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yordilorenzo](https://clawhub.ai/user/yordilorenzo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, creators, marketers, and developers use this skill to ask an agent to process media through OpenClip: identify viral video moments, render captioned clips, transcribe recordings, convert or edit media, remove image backgrounds, and generate short UGC-style ads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects an agent to a remote media-processing service and may send selected videos, images, URLs, or briefs to OpenClip. <br>
Mitigation: Use it only with media and prompts the user intends to process through OpenClip, and avoid private or sensitive media unless the user accepts that service boundary. <br>
Risk: Completed media outputs may be stored or shared as service/CDN URLs. <br>
Mitigation: Treat returned output URLs as persistent external artifacts and avoid sharing them more broadly than the user intends. <br>
Risk: Some OpenClip workflows are asynchronous and can fail because of authentication, subscription, credits, download, or validation issues. <br>
Mitigation: Poll the documented status tools, read terminal status and error text before acting, and report subscription, credit, or authentication remediation clearly to the user. <br>


## Reference(s): <br>
- [OpenClip MCP server](https://openclip.app/mcp) <br>
- [OpenClip manual token endpoint](https://openclip.app/mcp/key) <br>
- [OpenClip reference](reference.md) <br>
- [ClawHub skill page](https://clawhub.ai/yordilorenzo/skills/openclip) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, markdown, API calls] <br>
**Output Format:** [Markdown guidance with inline commands, MCP tool names, status values, and returned media URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include OpenClip job identifiers, status guidance, transcripts, clip metadata, caption preset choices, and permanent service/CDN URLs returned by OpenClip.] <br>

## Skill Version(s): <br>
1.1.1 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
