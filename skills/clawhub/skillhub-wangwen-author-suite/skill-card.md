## Description:

Wangwen Author Suite helps Chinese web-novel authors draft outlines and chapters, critique work with a built-in review rubric, create title and blurb copy, and export Markdown chapters to Fanqie-ready TXT.

This skill is ready for commercial/non-commercial use.

## Publisher:

[code-hermit-tao](https://clawhub.ai/user/code-hermit-tao)

### License/Terms of Use:

MIT-0

## Use Case:

External authors and creators use this skill to plan, draft, revise, critique, and package Chinese web-novel chapters for serial publishing workflows. It is especially focused on Fanqie/Tomato-style chapter planning, quality checks, title and blurb generation, and Markdown-to-TXT export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can manage local draft files and run optional Python scripts for word counts or Fanqie TXT export.

Mitigation: Confirm the target book directory before file operations and review generated files before publishing or uploading them.

Risk: The Fanqie export script writes TXT files and removes old per-chapter TXT exports in the selected output folder.

Mitigation: Use a dedicated export folder or back up existing TXT files before running export.

Risk: Broad Chinese writing trigger phrases may activate the skill during general fiction-writing requests.

Mitigation: Confirm the intended mode, such as quick writing, Tomato workflow, review, title copy, or export, before proceeding when the request is ambiguous.

Risk: Generated quality scores, platform checks, and publishing guidance could be mistaken for guaranteed platform acceptance or commercial success.

Mitigation: Treat scores and platform checks as drafting aids only; the author should make final publishing decisions and review current platform rules.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/code-hermit-tao/skills/skillhub-wangwen-author-suite)
- [README](README.md)
- [Examples](examples.md)
- [Quality hard standards](references/quality-hard-standards.md)
- [Tomato line workflow](references/tomato-line.md)
- [Tomato quality checklist](references/tomato-quality-checklist.md)
- [Juzu reviewer](references/juzu-reviewer.md)
- [Fanqie export](references/export-fanqie.md)
- [Title, blurb, and cover copy](references/title-blurb-cover.md)
- [Genre map](references/genres.md)
- [Writing guide](references/writing-guide.md)
- [De-AI and fake prose checks](references/deai-and-fake-prose.md)
- [Platform gate](references/platform-gate.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses, plain text chapter exports, Python command snippets, and generated local Markdown or TXT files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local draft files under novels/<book-name>/ and optional Fanqie export TXT files when the user requests file-based workflows.]

## Skill Version(s):

1.0.1 (source: server release metadata and PUBLISH.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
