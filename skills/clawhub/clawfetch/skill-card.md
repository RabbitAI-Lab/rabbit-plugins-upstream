## Description: <br>
Thin OpenClaw and ClawHub wrapper for the published clawfetch npm CLI, used to fetch web pages, GitHub READMEs, and Reddit threads as markdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ernestyu](https://clawhub.ai/user/ernestyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when an agent needs to fetch ordinary web pages, GitHub README pages, or Reddit threads into markdown for knowledge-base ingestion, source review, or compact reading. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches requested web URLs and returns extracted markdown, so use in restricted environments may expose network access or retrieval policy concerns. <br>
Mitigation: Run it only in environments where the target URLs are approved and review fetched content before using it as trusted source material. <br>
Risk: First use installs and runs a local npm CLI with a headless browser runtime. <br>
Mitigation: Review the clawfetch npm package and dependency chain when supply-chain controls are required, then run the CLI runtime check before fetching pages. <br>
Risk: FlareSolverr support can route protected-page fetching through an external service if enabled. <br>
Mitigation: Keep FlareSolverr disabled by default and enable it only with a trusted, explicitly configured service URL. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ernestyu/skills/clawfetch) <br>
- [Project Homepage](https://github.com/ernestyu/clawfetch) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown content and concise CLI setup or recovery guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The fetched markdown may include metadata sections emitted by the local clawfetch CLI.] <br>

## Skill Version(s): <br>
1.0.12 (source: evidence.release.version, SKILL.md frontmatter, manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
