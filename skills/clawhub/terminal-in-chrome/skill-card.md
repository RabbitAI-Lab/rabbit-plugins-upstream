## Description: <br>
Manages the Web Terminal Chrome Extension local backend server. Use this skill to start, stop, or check the status of the local terminal server running on port 8989. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yayayahei](https://clawhub.ai/user/yayayahei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and users of the Web Terminal Chrome Extension use this skill to start, stop, check, and explain the local backend server that connects browser pages to a local shell. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to start and manage a local terminal backend that gives a Chrome extension access to a local shell. <br>
Mitigation: Install and use it only when that local browser-terminal behavior is intended, and use trusted source code. <br>
Risk: Stopping the backend with a process ID can terminate the wrong process if the port owner is misidentified. <br>
Mitigation: Verify that the PID shown by lsof belongs to this terminal backend, and prefer normal shutdown or plain kill before kill -9. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/yayayahei/skills/tree/main/terminal-in-chrome) <br>
- [ClawHub skill page](https://clawhub.ai/yayayahei/skills/terminal-in-chrome) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local process and port checks for the terminal backend.] <br>

## Skill Version(s): <br>
1.1.31 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
