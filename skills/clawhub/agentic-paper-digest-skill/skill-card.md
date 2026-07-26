## Description: <br>
Fetches and summarizes recent arXiv and Hugging Face papers with Agentic Paper Digest. Use when the user wants a paper digest, a JSON feed of recent papers, or to run the arXiv/HF pipeline. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[matanle51](https://clawhub.ai/user/matanle51) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and research teams use this skill to configure and run a local paper-digest workflow that fetches recent arXiv and Hugging Face papers, summarizes them with an LLM provider, and returns digest results for downstream agents or polling workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bootstrap helper downloads project code and installs Python dependencies. <br>
Mitigation: Review the downloaded project before running it and install only when the publisher and linked project are trusted. <br>
Risk: The workflow uses external LLM provider credentials from environment variables or a .env file. <br>
Mitigation: Use a limited API key, keep .env private, and confirm the intended provider configuration before running. <br>
Risk: API mode uses a local service, and the stop helper targets processes on port 8000. <br>
Mitigation: Check what is using port 8000 before starting or stopping the API service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/matanle51/skills/agentic-paper-digest-skill) <br>
- [Project homepage linked by skill](https://github.com/matanle51/agentic_paper_digest) <br>
- [Publisher profile](https://clawhub.ai/user/matanle51) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands; CLI and API runs can return JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The workflow may write a local SQLite data store under PROJECT_DIR and can expose local API endpoints when the API mode is used.] <br>

## Skill Version(s): <br>
0.3.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
