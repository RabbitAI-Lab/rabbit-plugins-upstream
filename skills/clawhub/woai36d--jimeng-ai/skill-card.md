## Description: <br>
Jimeng Ai helps agents generate and save images from text or image prompts through a local Jimeng API wrapper using a user-provided Jimeng session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users with a Jimeng membership use this skill to request generated images, manage the local service, update the session ID, and save generated files into a workspace output directory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Jimeng session cookies and account-related actions. <br>
Mitigation: Use only a Jimeng account/session you control, replace or remove the bundled sessionid, protect config.json and logs, and avoid shared machines. <br>
Risk: The local API wrapper can expose account-backed image generation if it is bound or configured too broadly. <br>
Mitigation: Review before installing, bind the service to localhost, restrict CORS, and update dependencies. <br>


## Reference(s): <br>
- [Jimeng website](https://jimeng.jianying.com/) <br>
- [ClawHub skill page](https://clawhub.ai/woai36d/skills/jimeng-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files] <br>
**Output Format:** [Markdown status text, JSON API responses, shell commands, configuration updates, and downloaded image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated images are saved to the configured output directory; generation count is documented as 1 to 4 images per request.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
