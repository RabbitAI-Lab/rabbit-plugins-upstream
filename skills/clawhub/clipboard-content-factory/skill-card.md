## Description: <br>
Clipboard Content Factory monitors copied clipboard content and turns articles or links into local draft posts for Douyin, Xiaohongshu, and Bilibili. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nh5gntnf78-oss](https://clawhub.ai/user/nh5gntnf78-oss) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators and operators use this skill to turn copied source material into platform-specific draft posts and posting cues, either once or through clipboard watch mode. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Clipboard watch mode can save sensitive text that the user copies, including private messages, credentials, tokens, or business data. <br>
Mitigation: Use one-shot mode in sensitive environments, avoid running watch mode while copying sensitive data, and periodically delete generated local output folders. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nh5gntnf78-oss/skills/clipboard-content-factory) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, markdown, configuration, guidance] <br>
**Output Format:** [Markdown draft files, JSON summary, and console status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local platform drafts and summary files under Desktop/clipboard_content_factory or a configured output directory.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
