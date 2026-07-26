## Description: <br>
Browser-based song creation with Suno, including gathering a song brief, generating lyrics, setting Persona and Custom mode, and producing new tracks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[machinesbefree](https://clawhub.ai/user/machinesbefree) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and creators use this skill to guide an agent through creating songs in Suno via a browser session, from gathering the song brief through generating and sharing track links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may use an active Suno browser session to create tracks under the user's Suno account. <br>
Mitigation: The user should log in directly, keep credentials private, and review song inputs before generation. <br>
Risk: The included Anchor Protocol runbook is an example and could be used unintentionally for an unrelated song request. <br>
Mitigation: Confirm the requested title, persona, lyrics, and style tags before creating tracks. <br>


## Reference(s): <br>
- [Suno Browser Workflow](references/suno-workflow.md) <br>
- [Suno](https://suno.ai) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown] <br>
**Output Format:** [Markdown with song brief details, lyrics or style tags when requested, Suno track links, and optional file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include browser-session actions and links to generated Suno tracks.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
