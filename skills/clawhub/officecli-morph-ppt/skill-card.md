## Description: <br>
Guides agents to create PowerPoint .pptx decks with smooth cross-slide Morph transitions using officecli-pptx workflows, shape-name pairing, ghosting, helper scripts, style references, and delivery checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iceyliu](https://clawhub.ai/user/iceyliu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and presentation-building agents use this skill when a user explicitly needs a PowerPoint deck with smooth cross-slide motion, shape continuity, and Morph transition choreography. It helps plan the narrative, generate officecli commands or helper-script workflows, choose visual references, and validate deliverables before handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup path can pipe a remote officecli installer script directly into a shell. <br>
Mitigation: Install only from a trusted officecli source, prefer a versioned release download, and verify provenance before running installer commands. <br>
Risk: The skill runs local officecli commands that create, overwrite, and mutate .pptx files. <br>
Mitigation: Work from a backup copy or rerunnable build script, keep the source deck closed during generation, and validate the final deck before delivery. <br>
Risk: Helper cleanup actions can make high-impact changes to a deck. <br>
Mitigation: Run cleanup only on a backup or generated copy and review the resulting deck before replacing any user-owned file. <br>
Risk: Morph motion may not render in LibreOffice, Google Slides web viewers, or static HTML/SVG previews. <br>
Mitigation: Confirm motion in PowerPoint 365, Keynote, or WPS and tell users that unsupported viewers may show static slides or plain fades. <br>
Risk: Incorrect shape naming or missing ghost steps can cause silent fade behavior, visual accumulation, or broken Morph choreography. <br>
Mitigation: Plan paired shape names before building, use the helper verification workflow for longer decks, and run the Morph-specific delivery gates before handoff. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iceyliu/skills/officecli-morph-ppt) <br>
- [OfficeCLI releases](https://github.com/iOfficeAI/OfficeCLI/releases) <br>
- [Morph PPT skill instructions](SKILL.md) <br>
- [PPT planner decision rules](reference/decision-rules.md) <br>
- [Morph PPT design notes](reference/pptx-design.md) <br>
- [Python morph helper library](reference/morph-helpers.py) <br>
- [Shell morph helper library](reference/morph-helpers.sh) <br>
- [Visual style index](reference/styles/INDEX.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with bash and Python command examples, plus file-delivery requirements.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Expected deliverables are a .pptx deck, a rerunnable build script, and brief.md; the skill requires officecli validation before delivery.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata, released 2026-06-30) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
