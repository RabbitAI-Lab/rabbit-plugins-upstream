## Description: <br>
Compile legacy documentation on internet into agent-native memory context using the Moltext. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[uditakhourii](https://clawhub.ai/user/uditakhourii) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and autonomous agents use Moltext to compile large web documentation sets into dense Markdown context for tool, library, or application learning. It is intended for documentation ingestion before the agent reads the generated context and acts on the technical material. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Moltext can globally install an npm package, fetch documentation URLs, write local context files, and optionally use LLM API credentials. <br>
Mitigation: Install only in trusted environments, prefer raw mode when no LLM is needed, use scoped API keys for LLM workflows, avoid sensitive private sources unless the data flow is understood, and review compiled output before relying on it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/uditakhourii/skills/moltext) <br>
- [OpenClaw Documentation](https://docs.molt.bot/) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides the agent to run the moltext CLI, fetch documentation URLs, and read the generated Markdown context file.] <br>

## Skill Version(s): <br>
1.2.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
