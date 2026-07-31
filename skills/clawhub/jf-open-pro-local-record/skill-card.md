## Description: <br>
杰峰设备本地录像技能（开发版）。支持 TF 卡/硬盘存储设备的录像日历查询、回放列表、录像回放下载、本地报警图片获取、主辅码流切换等功能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operators use this skill to manage JFTech device local recordings on TF card or hard-disk storage, including calendar lookup, playback lists, playback or download URLs, local alarm images, and stream switching. <br>

### Deployment Geography for Use: <br>
China Mainland, Asia, Europe, and North America via the documented JFTech regional API hosts. <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive JFTech account, app, device, and password values are required to access private device recordings. <br>
Mitigation: Provide credentials through a controlled environment, avoid pasting them into shared chats or logs, and rotate exposed tokens or passwords. <br>
Risk: Playback, download, and image URLs can expose private surveillance media while they remain valid. <br>
Mitigation: Treat returned URLs as temporary credentials, share them only with authorized users, and avoid storing them in persistent logs. <br>
Risk: JF_ENDPOINT is configurable and not validated by the script. <br>
Mitigation: Set JF_ENDPOINT only to documented official JFTech regional hosts before running the skill. <br>
Risk: Switching the recording stream changes the quality used for future recordings. <br>
Mitigation: Confirm the desired storage and quality tradeoff before using stream switching actions. <br>
Risk: The current script has a duplicate CLI argument bug that can prevent normal execution. <br>
Mitigation: Review and fix the CLI argument definition before relying on the script operationally. <br>


## Reference(s): <br>
- [JFTech Open Platform documentation](https://docs.jftech.com) <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-local-record) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/jftech) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and console text or URL outputs from Python scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Playback, download, and image URLs should be treated as temporary credentials; device credentials are supplied through environment variables or CLI arguments.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact metadata version is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
