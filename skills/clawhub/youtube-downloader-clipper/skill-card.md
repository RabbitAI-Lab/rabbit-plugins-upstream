## Description: <br>
Clips and downloads YouTube videos or audio using precise timestamps, quality options, and optional custom filenames. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sandeepyadav1478](https://clawhub.ai/user/sandeepyadav1478) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, content creators, educators, musicians, and researchers can use this skill to extract timestamped YouTube clips, audio segments, or full downloads when they have rights to access and reuse the source media. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads YouTube media and writes files locally, which can create copyright, compliance, or file-management risks. <br>
Mitigation: Use it only for media the user has rights to access and reuse, and run it from a dedicated downloads directory. <br>
Risk: The security scan notes that the skill can silently install a Python package and run generated local scripts from user-provided inputs. <br>
Mitigation: Preinstall yt-dlp in an isolated environment, review generated scripts before execution, and avoid privileged or shared Python environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sandeepyadav1478/skills/youtube-downloader-clipper) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated Python code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write downloaded video or audio files to the current working directory and may install yt-dlp with pip if it is missing.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
