## Description: <br>
Builds and manages a local RAG system with environment setup, embedding model downloads, text splitting, vector retrieval, multiple knowledge bases, prompt tuning, and a web configuration UI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ldxs001](https://clawhub.ai/user/ldxs001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to set up a local RAG workflow, ingest documents into vector knowledge bases, retrieve context for an agent, or run standalone RAG answers through a configured LLM endpoint. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install Python packages, download embedding models, create and delete RAG data, and run local subprocesses. <br>
Mitigation: Install only in a trusted local environment, review commands before execution, and back up the data directory before deleting knowledge bases. <br>
Risk: The web UI and knowledge-base deletion paths were flagged by the server security summary as under-scoped enough to require review. <br>
Mitigation: Bind the web UI to localhost only, avoid exposing its port to a network, and review or patch validation around knowledge-base and template names before using untrusted inputs. <br>
Risk: Standalone mode can send prompts and retrieved context to a configured LLM endpoint. <br>
Mitigation: Use a trusted local or approved remote LLM endpoint and avoid sending sensitive documents or prompts to endpoints that are not approved for the data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/local-rag-builder) <br>
- [SKILL.md](SKILL.md) <br>
- [Usage guide](references/guide.md) <br>
- [Architecture](references/architecture.md) <br>
- [LLM setup](references/llm-setup.md) <br>
- [Permissions and testing](references/permissions.md) <br>
- [Examples](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON-capable CLI output, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return retrieval context or standalone RAG answers as JSON; local knowledge-base, model, prompt, config, log, and cache files are stored in the skill data directory.] <br>

## Skill Version(s): <br>
1.6.0 (source: ClawHub release evidence; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
