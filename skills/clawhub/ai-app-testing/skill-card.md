## Description: <br>
LLM/Agent application testing toolkit for L0-L4 evaluation, prompt security auditing, RAG assessment, stress and regression testing, with runnable scripts and test cases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shylamb-token](https://clawhub.ai/user/shylamb-token) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and QA engineers use this skill to generate and run checks for LLM, agent, tool-calling, MCP, RAG, prompt-security, stress, and regression workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Simulated security-audit or MCP compliance outputs may be mistaken for verified compliance evidence. <br>
Mitigation: Treat results as QA signals only and require expert review before using them for security or compliance decisions. <br>
Risk: Online tests can send realistic sensitive fixtures or private RAG corpus text to configured endpoints or judge models. <br>
Mitigation: Use local or trusted endpoints, replace realistic fixtures with clearly fake data, and avoid sending private corpus text to third-party models. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shylamb-token/skills/ai-app-testing) <br>
- [Publisher profile](https://clawhub.ai/user/shylamb-token) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with runnable Python scripts, YAML configuration, JSON test data, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes offline checks and optional online endpoint-based tests.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata; artifact frontmatter: 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
