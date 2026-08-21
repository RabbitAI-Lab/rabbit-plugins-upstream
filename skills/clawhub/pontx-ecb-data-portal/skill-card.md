## Description:

Integrates ECB Data Portal statistics through Pontx for dataflows, DSDs, codelists, series keys, frequency-aware periods, bounded or incremental retrieval, availability, and SDMX formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data engineers use this skill to design safe ECB statistics discovery, bounded retrieval, and incremental ingestion workflows through Pontx while preserving SDMX structure and data meaning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A live ECB retrieval could be broader than intended if the request is not bounded and previewed first.

Mitigation: Resolve the current Pontx contract, preview the exact bounded GET request, partition large jobs by non-overlapping keys or periods, and execute only after explicit user approval.

Risk: Credentials or tokens could be exposed through prompts, command arguments, logs, source, or generated examples.

Mitigation: Keep credentials and tokens out of all prompts, arguments, source files, logs, and generated examples.

Risk: ECB observations can be misleading if frequency, revision state, metadata, or transformation context is lost.

Mitigation: Preserve series metadata, report period and revision context, avoid silent frequency aggregation, and document application transformations.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded-request previews, SDMX query design, retrieval approval prompts, and integration guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
