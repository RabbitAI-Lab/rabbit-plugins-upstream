## Description: <br>
Monitor DX clusters for rare station spots, track active DX expeditions, and get daily band activity digests for amateur radio operators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[capt-marbles](https://clawhub.ai/user/capt-marbles) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External amateur radio operators and their agents use this skill to query DX cluster spots, monitor for new or rare stations, generate daily band activity digests, and set up intentional background monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts external DX cluster servers and may send a callsign. <br>
Mitigation: Install and run it only when external cluster access is intended, and use a callsign only if comfortable sending it to the selected cluster. <br>
Risk: Cron setup can create ongoing background monitoring and local logs or state. <br>
Mitigation: Review cron entries before enabling them, and periodically review or delete /tmp logs and state files as needed. <br>
Risk: The README references a setup script that is not included in the artifact. <br>
Mitigation: Do not run a replacement setup script from another source unless it has been separately inspected. <br>


## Reference(s): <br>
- [NG3K Announced DX Operations](https://www.ng3k.com/misc/adxo.html) <br>
- [DX World](https://www.dx-world.net/) <br>
- [425 DX News](http://www.425dxn.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration guidance] <br>
**Output Format:** [Terminal text and Markdown with optional JSON output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local state and logs under /tmp and supports cron-based monitoring when configured by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
