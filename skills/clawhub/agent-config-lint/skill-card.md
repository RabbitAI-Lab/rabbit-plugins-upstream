## Description: <br>
Agent Config Lint helps developers run the tenken Node CLI to statically check SKILL.md, AGENTS.md, CLAUDE.md, and llms.txt files for portability and reliability problems before publishing or committing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hyuga611](https://clawhub.ai/user/hyuga611) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to check agent configuration files before committing, publishing to ClawHub, or troubleshooting skills that fail to trigger or break on another machine. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs npm package code through npx and reads local agent configuration paths supplied for scanning. <br>
Mitigation: Review the package before installation, run it only in the intended repository scope, and avoid pointing it at unrelated sensitive directories. <br>
Risk: Broad suppressions, ignore paths, or allowed CLI lists can hide real portability problems. <br>
Mitigation: Keep suppressions narrow, document deliberate exceptions, and review ignore or allow entries before publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hyuga611/skills/agent-config-lint) <br>
- [tenken project homepage](https://github.com/hyuga611/tenken) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Text, JSON] <br>
**Output Format:** [Markdown guidance with bash commands; tenken may return plain-text or JSON findings.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No model or API key required; exits 0 when clean, 1 when findings are present, and 2 on bad usage.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
