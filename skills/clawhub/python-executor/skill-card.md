## Description: <br>
Execute Python code through inference.sh in a sandboxed Python 3.10 environment with common libraries for data processing, web scraping, media processing, API calls, automation, and file outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[okaris](https://clawhub.ai/user/okaris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to run Python scripts for data analysis, web scraping, media and document generation, API integration, and automation when local execution is not desired. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Python code, inputs, outputs, and files may be processed by the remote inference.sh execution service. <br>
Mitigation: Avoid sending secrets, credentials, private datasets, or confidential generated files unless that remote processing is intended. <br>
Risk: The quick-start installer pipes a remote shell script into the local shell. <br>
Mitigation: Prefer manual installation with checksum verification before running the infsh CLI. <br>
Risk: Agent-generated Python may perform unintended network calls, scraping, or file generation. <br>
Mitigation: Review code before execution and constrain inputs, timeouts, and output handling for the intended task. <br>


## Reference(s): <br>
- [Python Executor on ClawHub](https://clawhub.ai/okaris/skills/python-executor) <br>
- [Running Apps](https://inference.sh/docs/apps/running) <br>
- [App Code](https://inference.sh/docs/extend/app-code) <br>
- [Sandboxed Code Execution](https://inference.sh/blog/tools/sandboxed-execution) <br>
- [CLI Checksums](https://dist.inference.sh/cli/checksums.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON inputs, Python code snippets, stdout text, and returned output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs CPU-only Python with configurable timeout and optional high-memory variant; files saved under outputs/ are returned by the app.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
