## Description: <br>
Guides agents using OpenCLI browser to consume sitemap context lazily, choose adapter or browser fallback paths, resume from state signatures, and mark stale sitemap entries while trusting live browser state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chaoyang78](https://clawhub.ai/user/chaoyang78) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when automating website navigation with OpenCLI browser and sitemap context is available, requested, or needed. It helps reduce blind navigation while keeping live browser state authoritative and recording stale sitemap observations locally. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent toward state-changing browser or adapter actions. <br>
Mitigation: Review website actions before allowing state-changing OpenCLI browser or adapter commands. <br>
Risk: Sitemap entries can be stale or differ from the live website state. <br>
Mitigation: Refresh browser state after navigation, trust the live page over sitemap context, and record stale observations in the local overlay. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and local stale-note snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local sitemap overlay notes when drift or adapter health issues are observed.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
