## Description: <br>
Poink Semantic Search helps agents build and query local document knowledge bases with semantic and hybrid search across PDF, Markdown, TXT, DOCX, ODT, and FODT files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[szemroda](https://clawhub.ai/user/szemroda) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to install and invoke the Poink CLI for indexing local documents and answering search questions over those collections. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Indexing broad paths may process private or sensitive local documents. <br>
Mitigation: Scope ingestion to files and directories that are intended to be indexed before running Poink. <br>
Risk: The skill depends on the external poink-cli package to process documents. <br>
Mitigation: Install and use it only when the package is trusted for the target environment. <br>


## Reference(s): <br>
- [Poink project homepage](https://github.com/szemroda/poink) <br>
- [Poink README](https://github.com/szemroda/poink#readme) <br>
- [ClawHub skill page](https://clawhub.ai/szemroda/skills/poink-semantic-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown or plain text with Poink CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Use JSON output when the agent executes Poink commands directly; prefer text output when suggesting commands for a user.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
