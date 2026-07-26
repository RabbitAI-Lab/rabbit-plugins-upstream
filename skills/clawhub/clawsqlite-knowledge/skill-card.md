## Description: <br>
Knowledge base skill that uses the published clawsqlite CLI for ingest, search, show, and maintenance workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ernestyu](https://clawhub.ai/user/ernestyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to install and operate the pinned clawsqlite knowledge CLI for ingesting, searching, showing, and maintaining a local knowledge base from a configured instance home. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Knowledge records may persist sensitive text or private URLs in the configured local knowledge instance. <br>
Mitigation: Avoid ingesting sensitive content unless persistence is intended, and review content before saving it to the knowledge base. <br>
Risk: Bootstrap installs or updates the pinned clawsqlite==1.0.12 Python package. <br>
Mitigation: Review the pinned PyPI dependency and run bootstrap only in an environment where installing Python packages is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ernestyu/skills/clawsqlite-knowledge) <br>
- [clawsqlite project homepage](https://github.com/ernestyu/clawsqlite) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown instructions with shell command examples and JSON-oriented CLI usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides use of a pinned local CLI and expects commands to be run from a configured knowledge instance home.] <br>

## Skill Version(s): <br>
1.0.12 (source: frontmatter, manifest.yaml, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
