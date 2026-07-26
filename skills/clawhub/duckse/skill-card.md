## Description: <br>
Duckse helps agents search the web, news, images, videos, and books using the duckse DDGS-based CLI with readable text or JSON results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dwirx](https://clawhub.ai/user/dwirx) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, employees, developers, and research-oriented agents use Duckse to run web, news, image, video, and book searches, including current-events monitoring and fact-checking with source URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill documents installing duckse by piping a mutable remote GitHub script directly into bash. <br>
Mitigation: Review the install script manually or use a pinned, vetted release before installing; do not allow an agent to run the curl-to-bash installer automatically. <br>
Risk: Search commands can retrieve current web content whose accuracy, safety, and licensing vary by source. <br>
Mitigation: Use the returned source URLs for verification and apply safe-search, region, backend, and time filters appropriate to the task. <br>


## Reference(s): <br>
- [Duckse ClawHub skill page](https://clawhub.ai/dwirx/skills/duckse) <br>
- [duckse install script referenced by the skill](https://raw.githubusercontent.com/dwirx/duckse/main/scripts/install.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results may include web URLs, news items, image or video metadata, book results, and optional expanded final URLs.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
