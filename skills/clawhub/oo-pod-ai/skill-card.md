## Description: <br>
Pod AI (callpod.ai) lets agents operate Pod AI through the OOMOL oo CLI for supported reading, creating, and updating workflows instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Pod AI through an OOMOL-connected account, including creating outbound phone calls with a Pod AI voice agent after confirming write payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a connected Pod AI account to place outbound calls. <br>
Mitigation: Review the generated call payload carefully and approve write actions only when the recipient, voice agent, and intended effect are clear. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-pod-ai) <br>
- [Pod AI Homepage](https://callpod.ai/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL Pod AI Connection](https://console.oomol.com/app-connections?provider=pod_ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return connector JSON responses that include data and a meta.executionId value.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
