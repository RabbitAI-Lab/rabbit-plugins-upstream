## Description: <br>
Searches Tenor and Giphy for GIF reactions, converts selected GIFs to WhatsApp-compatible MP4 files, and helps send them to a specified WhatsApp contact. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External personal users use this skill to find GIF reactions for WhatsApp chats, convert them to MP4, and send one selected media file to a chosen contact. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send media through WhatsApp and has weak confirmation guidance, creating a risk of accidental message sending. <br>
Mitigation: Confirm the recipient, selected media file, and message text before any send action. <br>
Risk: The artifact includes unrelated SEO trigger language that could cause use outside the intended WhatsApp GIF workflow. <br>
Mitigation: Use the skill only for explicit WhatsApp GIF search-and-send requests, and narrow trigger language before deployment. <br>
Risk: The workflow depends on third-party media and messaging services. <br>
Mitigation: Add clear notices for Tenor, Giphy, WhatsApp, and network access before publication or installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/gif-whatsapp-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown with inline shell commands and structured status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May download GIF media, create temporary MP4 files, and invoke a WhatsApp message tool when the user confirms the recipient and selected media.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
