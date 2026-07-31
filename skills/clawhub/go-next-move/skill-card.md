## Description: <br>
Analyzes Go or Weiqi board photos or text board positions, then uses a local KataGo setup to recommend the next move at beginner, intermediate, or advanced strength. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[imcaptor](https://clawhub.ai/user/imcaptor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Go players use this skill to turn a board photo or a 19x19 text board into an auditable next-move recommendation, including candidate moves and analysis details. It is useful when the user wants a move calibrated to a requested playing-strength level rather than only KataGo's strongest move. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Board recognition errors or an incorrect side-to-move can make the recommended move unreliable. <br>
Mitigation: Review the generated source overlay or rendered board, confirm the side to move, and treat the recommendation as unreliable until the board is corrected when recognition looks wrong. <br>
Risk: The skill runs local analysis and may create result images or temporary KataGo logs from user-provided board inputs. <br>
Mitigation: Use it only with intended local board images or text files, and review generated overlays and output paths before sharing or retaining results. <br>
Risk: No-capture continuation overlays can become invalid when captures, ko, state ambiguity, or occupied overlay points are involved. <br>
Mitigation: Re-shoot or reset the board and analyze a fresh position when captures or ambiguous board state are present. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/imcaptor/skills/go-next-move) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON analysis output, and optional generated image file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local Python 3 and KataGo binaries; may create result images and temporary KataGo logs.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
