## Description:

A deterministic story-structure tool for creators that supports causal plot reasoning, logic-gap detection, worldbuilding, character consistency checks, and multilingual story bridging.

This skill is for research and development only.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, narrative designers, and other creators use this skill to build, audit, and generate long-form stories, game plots, scripts, and derivative IP while tracking causal consistency, character behavior, and world rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or overwrite audit_report.html in the working directory.

Mitigation: Run it in a working directory where that filename is expected, or move existing report files before generation.

Risk: A connected LLM provider may receive manuscript text and character notes.

Mitigation: Use a vetted provider and avoid sending sensitive draft material unless the provider terms and data handling are acceptable.

Risk: Generated story text, repairs, and logic-audit guidance may be incomplete or misleading for creative decisions.

Mitigation: Review generated plots, repairs, and consistency findings before adopting them.

## Reference(s):

- [Character to Narrative Link](references/CharacterToNarrativeLink.md)
- [Worldview Versioning](references/WorldviewVersioning.md)
- [Long-Narrative Window Management](references/LongNarrativeWindow.md)
- [Story Engine Homepage](https://github.com/nohn3043-arch/story-engine)
- [ClawHub Skill Page](https://clawhub.ai/nohn3043-arch/skills/story-engine-for-creator)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown and Python-oriented guidance, with generated story text and optional HTML audit reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or overwrite audit_report.html in the working directory; an optional LLM provider may process manuscript text and character notes.]

## Skill Version(s):

1.1.1 (source: server release evidence; artifact frontmatter reports 2.0.0 capability metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
