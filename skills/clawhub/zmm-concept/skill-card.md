## Description:

Helps agents prepare Chinese concept-video scripts by locking the audience problem, core definition, theory target, and analogies before drafting and refining the creator's spoken version.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content-production agents use this skill to turn a familiar concept into a short-form script workflow: qualify the topic, lock four core decisions, draft a Markdown script, hand it back for spoken revision, and update related publishing records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases may start the ZMM workflow when the user only wants a general explanation of a concept.

Mitigation: Confirm the user wants this content-production workflow before applying its process or touching local workspace files.

Risk: The workflow can affect local vault drafts, publishing indexes, rules files, cover assets, and calendar follow-ups.

Mitigation: Review proposed target paths and edits before execution, and limit changes to files needed for the active release workflow.

Risk: Several workflow guarantees depend on local reference files outside the packaged artifact.

Mitigation: If required local references are unavailable, stop or clearly disclose which checks cannot be guaranteed.

## Reference(s):

- [锁四样](references/锁四样.md)
- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-concept)
- [Publisher profile](https://clawhub.ai/user/iamzifei)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with tables, checklists, and inline commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local draft, rules, publishing-log, cover, and calendar updates when the workflow is intentionally invoked.]

## Skill Version(s):

0.2.1 (source: server release evidence; artifact frontmatter says 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
