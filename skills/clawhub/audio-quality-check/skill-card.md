## Description: <br>
Audio Quality Check helps agents analyze local audio recordings for echo, loudness, speech intelligibility, SNR, spectral characteristics, and related quality issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers, engineers, and audio reviewers use this skill to run local recording diagnostics, interpret metrics, and identify likely causes of poor call audio such as echo, bleed, noise, or AEC degradation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Call recordings may contain private speech or sensitive meeting content. <br>
Mitigation: Run the analyzer only on recordings the user is authorized to inspect, and avoid sharing generated reports outside the intended review context. <br>
Risk: The skill depends on local audio-analysis tooling and Python packages that must be installed before use. <br>
Mitigation: Install dependencies from trusted package sources and review the local environment before running analysis commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/audio-quality-check) <br>
- [Project homepage](https://github.com/tenequm/skills/tree/main/skills/audio-quality-check) <br>
- [Apache License 2.0](https://www.apache.org/licenses/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown guidance with bash and Python snippets plus terminal report text from the bundled analyzer] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-selected local audio recordings and ffmpeg/ffprobe; analysis is performed locally according to the reviewed artifacts.] <br>

## Skill Version(s): <br>
0.1.2 (source: evidence.release.version and artifact metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
