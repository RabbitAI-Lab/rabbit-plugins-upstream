## Description: <br>
Korean SRT (Super Rapid Train) search, reservation, and booking management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[khj809](https://clawhub.ai/user/khj809) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Travelers and agents use this skill to search Korean SRT trains, attempt reservations, monitor for cancelled-seat availability, list existing reservations, and cancel reservations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use SRT account credentials to make or cancel real train reservations. <br>
Mitigation: Install only when that access is acceptable, keep credentials private, and verify train, reservation, and cancellation details before running commands. <br>
Risk: Monitoring reports, logs, and PID files may expose trip or reservation details. <br>
Mitigation: Use a private Discord channel for reports and keep log, cache, and PID files in a private home or temp directory. <br>
Risk: Successful reservations still require user payment through SRT within a short payment window. <br>
Mitigation: After a reservation succeeds, complete payment through the SRT app or official SRT payment website. <br>


## Reference(s): <br>
- [ClawHub SRT skill page](https://clawhub.ai/khj809/skills/srt) <br>
- [khj809 publisher profile](https://clawhub.ai/user/khj809) <br>
- [SRTrain package on PyPI](https://pypi.org/project/SRTrain) <br>
- [SRTrain source repository](https://github.com/ryanking13/SRT) <br>
- [SRT payment website](https://etk.srail.kr) <br>
- [Skill homepage from frontmatter](https://github.com/khj809/openclaw-srt-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON command output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, uv, SRTrain, and SRT_PHONE/SRT_PASSWORD environment variables; reservation logs, cache, PID files, and rate-limit state are written under the configured data directory.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
