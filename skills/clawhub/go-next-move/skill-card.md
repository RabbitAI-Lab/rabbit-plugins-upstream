## Description: <br>
Analyzes Go/Weiqi board photos or text boards and uses local KataGo analysis to recommend the next move at beginner, intermediate, or advanced playing strength. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[imcaptor](https://clawhub.ai/user/imcaptor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Go players, coaches, and agent users use this skill to analyze a 19x19 Go board from an image or text board, choose the side to move, and receive an auditable KataGo-backed next-move recommendation with candidate comparisons. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local Python/OpenCV code and a local KataGo subprocess run on board images supplied by the user. <br>
Mitigation: Install and run the skill only in a trusted local environment with the required python3 and katago binaries. <br>
Risk: Annotated board images may be written to temporary output paths or to a local recognition-label folder during correction retries. <br>
Mitigation: Use private local output directories for sensitive board images and remove generated overlays or labels when they are no longer needed. <br>
Risk: Incorrect board recognition, side-to-move ambiguity, captures, or ko/state ambiguity can make a move recommendation unreliable. <br>
Mitigation: Confirm the side to move, compare the rendered board and source overlay against the real board, and re-shoot or reset the board when captures or state ambiguity are present. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/imcaptor/skills/go-next-move) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/imcaptor) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, json, image files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON analysis data, and optional annotated image file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Recommendations include the selected move, candidate moves, winrate and score information, principal variation, recognition metadata for image input, and optional overlay/result images.] <br>

## Skill Version(s): <br>
0.1.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
