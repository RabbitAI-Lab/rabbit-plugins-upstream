## Description: <br>
Generates and explains medical content for plain-language definitions, public education, clinical document summaries, teaching cases, and draft clinical documentation using a configured medical LLM. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Medical content teams, clinicians, educators, and developers use this skill to turn supplied medical text into auxiliary explanations, summaries, public-facing content, teaching cases, or draft documentation. Outputs require appropriate medical review and are not formal diagnostic decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided medical text is sent to the configured model API. <br>
Mitigation: Use only organization-approved endpoints and workflows, de-identify patient data before submission, and protect the app key. <br>
Risk: Saved JSON or NDJSON output can include the original question, metadata, and generated answer. <br>
Mitigation: Use --output only on approved storage and avoid shared filesystems for sensitive medical content. <br>
Risk: Generated medical content may be incomplete or unsuitable for direct clinical use. <br>
Mitigation: Treat outputs as auxiliary material and require qualified medical review before use in patient-facing or clinical workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-med-content-generation) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/unisound-llm) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Markdown, Shell commands, Configuration] <br>
**Output Format:** [JSON or NDJSON by default, with optional plain text model answers and saved UTF-8 output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports task selection, direct question input, JSON/JSONL/text/stdin input, dry runs, custom model endpoint settings, and optional text-only output.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
