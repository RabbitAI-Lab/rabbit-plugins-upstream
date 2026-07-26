## Description: <br>
Analyzes a Go/Weiqi board photo or text board, runs local KataGo analysis, and recommends the next move at beginner, intermediate, advanced, or all strength levels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[imcaptor](https://clawhub.ai/user/imcaptor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Go players, reviewers, and agents assisting them use this skill to convert a photographed or ASCII 19x19 board into a KataGo-backed next-move recommendation with candidate comparisons, engine metrics, and recognition overlays. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a local KataGo subprocess and reads or writes files selected for analysis and image output. <br>
Mitigation: Use explicit, non-sensitive board inputs and choose output paths carefully, especially in shared workspaces. <br>
Risk: Photo recognition errors or an uncertain side to move can make the recommendation unreliable. <br>
Mitigation: Review the generated recognition overlay, provide the side to move, and treat recommendations as unreliable until the board state is corrected. <br>
Risk: No-capture continuation overlays do not model captures, ko, or ambiguous state changes. <br>
Mitigation: Re-shoot or reset the board after captures or state ambiguity before requesting the next analysis. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/imcaptor/skills/go-next-move) <br>
- [Publisher profile](https://clawhub.ai/user/imcaptor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files, guidance] <br>
**Output Format:** [Markdown response with a recommended move, KataGo metrics, candidate comparisons, JSON helper output, and optional generated image file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write recognition and recommendation images to user-selected paths or a system temporary directory.] <br>

## Skill Version(s): <br>
0.0.16 (source: server release metadata; artifact frontmatter reports 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
