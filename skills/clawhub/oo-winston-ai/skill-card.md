## Description: <br>
Winston AI (gowinston.ai) helps an agent detect AI-generated text, check plagiarism, compare text similarity, and fact-check claims in text or public URLs through an OOMOL-connected Winston AI account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to run Winston AI analysis for AI text detection, plagiarism checks, text similarity comparison, and fact-checking against user-provided text, public document URLs, or public website URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted text or public URLs are routed through OOMOL and Winston AI for analysis. <br>
Mitigation: Use the skill only for content that is permitted under the user's Winston AI and OOMOL account policies; avoid confidential or regulated data unless those policies allow it. <br>
Risk: The skill can run live Winston AI analyses whose results may affect downstream user decisions. <br>
Mitigation: Treat returned detection, plagiarism, similarity, and fact-checking results as decision support and review important outputs before relying on them. <br>


## Reference(s): <br>
- [Winston AI homepage](https://gowinston.ai) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-winston-ai) <br>
- [Winston AI icon](https://static.oomol.com/logo/third-party/winston_ai.svg) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON response references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include Winston AI analysis results and execution identifiers returned by the OOMOL connector.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
