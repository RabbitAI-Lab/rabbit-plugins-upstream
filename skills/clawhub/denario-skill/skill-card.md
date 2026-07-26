## Description: <br>
Automates scientific research workflows by generating ideas, methods, results, papers, and citations with the Denario framework and Z.ai-compatible model access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jmanhype](https://clawhub.ai/user/jmanhype) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
Developers and research teams use this skill to run a staged autonomous research pipeline that drafts research ideas, methodologies, results analysis, papers, and citations. Outputs should be reviewed as research drafts before relying on them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security summary reports an undisclosed hardcoded Perplexity API key. <br>
Mitigation: Remove or rotate the bundled key before use and configure scoped user-owned API keys for external providers. <br>
Risk: The security summary reports that the skill can generate papers using built-in mock results. <br>
Mitigation: Treat generated papers, results, and citations as drafts and require human validation against real research data before publication or decision-making. <br>
Risk: The security guidance warns against sending private research data before external providers and transmitted content are clear. <br>
Mitigation: Review provider endpoints, transmitted content, and organization data-handling requirements before running the workflow on confidential research material. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jmanhype/skills/denario-skill) <br>
- [Skill Documentation](artifact/SKILL.md) <br>
- [Setup Guide](artifact/SETUP.md) <br>
- [Package Metadata](artifact/package.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Terminal output and generated research artifacts from Denario workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or reuse a local Python virtual environment and write project outputs under the configured Denario output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
