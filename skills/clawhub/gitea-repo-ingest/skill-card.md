## Description: <br>
Ingest public Git repositories or repositories on the configured Gitea server into the Research KB for OpenClaw code understanding, incremental commit comparison, repository overview pages, concept and resource pages, source traceability, and catalog/index updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[myd2002](https://clawhub.ai/user/myd2002) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and research teams use this skill to ingest readable public Git or configured Gitea repositories into a Research KB. It prepares repository context, validates generated pages, writes Markdown knowledge pages, records source traceability, and returns backend JSON for persistence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Repository ingestion may read and pass through secret-bearing .env, key, credential, or token files into analysis or KB summaries. <br>
Mitigation: Install only for repositories approved for OpenClaw analysis, avoid repositories that may contain committed secrets, and exclude or redact sensitive files before ingestion. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/myd2002/skills/gitea-repo-ingest) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown knowledge pages, JSON context and result envelopes, and shell command workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes repository overview, concept, resource, source manifest, catalog, and index updates through the apply workflow; validate-pages checks generated pages before writes.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
