## Description: <br>
Select and send local reaction GIFs by tag — pat-on-back, celebration, salute, facepalm, etc. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mirza42](https://clawhub.ai/user/mirza42) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use Gif Picker to let OpenClaw agents choose local reaction GIFs by emotional tag and emit a MEDIA line for replies without relying on third-party GIF APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup can make outbound requests to public media hosts and save downloaded GIF files in the OpenClaw workspace. <br>
Mitigation: Review or replace the sample GIF URLs before running populate.sh when media provenance matters. <br>
Risk: The skill emits MEDIA paths intended to attach reaction GIFs to agent replies. <br>
Mitigation: Use the picker only in contexts where attaching a reaction GIF is appropriate for the conversation and destination channel. <br>


## Reference(s): <br>
- [Gif Picker ClawHub listing](https://clawhub.ai/mirza42/skills/gif-picker) <br>
- [mirza42 publisher profile](https://clawhub.ai/user/mirza42) <br>
- [Declared project homepage](https://github.com/mirza-alam/openclaw-gif-picker) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text MEDIA line with optional status listings and markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local GIF index and filesystem paths; sample GIFs are downloaded during setup when populate.sh is run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
