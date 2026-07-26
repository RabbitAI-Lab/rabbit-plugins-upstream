## Description: <br>
Provides CLI tools (`wq`) and a specialized Alpha Miner sub-agent for WorldQuant BRAIN, with v1.1.3 evolve-engine. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sebrinass](https://clawhub.ai/user/sebrinass) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and quantitative researchers use WQBuddy to work with WorldQuant BRAIN through CLI commands and an Alpha Miner agent for backtesting, field search, diagnostics, dataset browsing, alpha synchronization, checks, and submission workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: BRAIN credentials are stored in `~/.wq-buddy/config.json`. <br>
Mitigation: Use restrictive file permissions, such as user-only read/write access, and install only on trusted machines. <br>
Risk: Session tokens and the SQLite research database are kept on disk under `~/.wq-buddy`. <br>
Mitigation: Keep the directory private, avoid sharing the database, and remove cached files when access is no longer needed. <br>
Risk: Configured LLM or embedding providers may receive alpha diagnostics or embedding inputs. <br>
Mitigation: Prefer local providers for sensitive research and review provider configuration before enabling LLM or embedding features. <br>
Risk: `wq submit --yes` is documented as an irreversible alpha submission action. <br>
Mitigation: Review alpha IDs and checks carefully before using the submit command. <br>


## Reference(s): <br>
- [WQBuddy on ClawHub](https://clawhub.ai/sebrinass/skills/wqbuddy) <br>
- [sebrinass publisher profile](https://clawhub.ai/user/sebrinass) <br>
- [wq-buddy npm package](https://www.npmjs.com/package/wq-buddy) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, CLI command suggestions, and structured text summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local files under ~/.wq-buddy and optional LLM or embedding provider configuration.] <br>

## Skill Version(s): <br>
1.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
